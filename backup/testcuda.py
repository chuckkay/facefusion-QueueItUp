import time
import numpy as np

try:
    import torch
    import torch.nn as nn
    torch_available = True
    cuda_available = torch.cuda.is_available()
except ImportError:
    torch_available = False
    cuda_available = False

import onnxruntime as ort

if torch_available:
    class SimpleModel(nn.Module):
        def __init__(self):
            super(SimpleModel, self).__init__()
            self.fc = nn.Linear(10000, 5000)

        def forward(self, x):
            return self.fc(x)

def benchmark_pytorch(model, input_tensor, num_iterations=100):
    torch.cuda.synchronize()
    start_time = time.time()
    with torch.no_grad():
        for _ in range(num_iterations):
            output = model(input_tensor)
    torch.cuda.synchronize()
    end_time = time.time()
    return (end_time - start_time) / num_iterations

def benchmark_onnx(ort_session, ort_input, num_iterations=100):
    start_time = time.time()
    for _ in range(num_iterations):
        output = ort_session.run(None, ort_input)
    end_time = time.time()
    return (end_time - start_time) / num_iterations

def main():
    if torch_available and cuda_available:
        input("Press Enter to create and export the PyTorch model...")
        model = SimpleModel().cuda()
        dummy_input = torch.randn(1, 10000).cuda()
        torch.onnx.export(model, dummy_input, "simple_model.onnx", export_params=True)
        print("PyTorch model exported to simple_model.onnx")

        input("Press Enter to run inference with PyTorch...")
        input_tensor = torch.randn(1, 10000).cuda()
        pytorch_time = benchmark_pytorch(model, input_tensor)
        print(f"Average PyTorch inference time: {pytorch_time * 1000:.2f} ms")
    elif torch_available:
        print("PyTorch is installed, but CUDA is not available. Skipping PyTorch tests.")
    else:
        print("PyTorch is not installed in the current virtual environment. Skipping PyTorch tests.")

    input("Press Enter to run inference with ONNX Runtime...")
    ort_session = ort.InferenceSession("simple_model.onnx", providers=['CUDAExecutionProvider'])
    if torch_available and cuda_available:
        input_name = ort_session.get_inputs()[0].name
        ort_input = {input_name: input_tensor.cpu().numpy()}
    else:
        # If PyTorch is not available or CUDA is not available, create a dummy input for ONNX Runtime
        input_name = ort_session.get_inputs()[0].name
        ort_input = {input_name: np.random.randn(1, 10000).astype(np.float32)}
    onnx_time = benchmark_onnx(ort_session, ort_input)
    print(f"Average ONNX Runtime inference time: {onnx_time * 1000:.2f} ms")

    if torch_available and cuda_available and pytorch_time < onnx_time:
        print("PyTorch is faster.")
    else:
        print("ONNX Runtime is faster.")

if __name__ == "__main__":
    main()
