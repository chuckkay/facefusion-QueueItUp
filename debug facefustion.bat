cd C:\AI\facefusion-QueueItUp
call conda activate facefusion
echo Running FaceFusion...
python run.py
echo FaceFusion has closed
echo python run.py 
echo       .
cmd /k
choice /C:YN /N /D Y /T 3 >nul