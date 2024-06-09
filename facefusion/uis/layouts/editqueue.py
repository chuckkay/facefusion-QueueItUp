import gradio
from typing import Optional

from facefusion.uis.components import frame_processors, frame_processors_options, execution, execution_thread_count, source
ABOUT_BUTTON = gradio.Button(
    value = "COMING SOON QueueItUp-3",
    variant = 'primary',
    link = 'https://github.com/chuckkay/QueueItUp-2.6.9'
    )
DONATE_BUTTON = gradio.Button(
    value = "DONATE",
    link = 'https://www.paypal.com/paypalme/CharlesKadish',
    size = 'sm'
    )

def pre_check() -> bool:
    return True


def pre_render() -> bool:
    return True
    
def render() -> gradio.Blocks:
    with gradio.Blocks() as layout:
        with gradio.Row():
            with gradio.Column(scale = 2):
                with gradio.Blocks():
                    ABOUT_BUTTON.render()
                    DONATE_BUTTON.render()
    return layout

def listen() -> None:
    frame_processors.listen()

def run(ui : gradio.Blocks) -> None:
	ui.launch(show_api = False, inbrowser = facefusion.globals.open_browser)
