@echo off

echo ------------------------------------------- UPLOAD: --------------------------------------------
cd .\build\
".\tools\python\Scripts\python" .\upload.py
echo ------------------------------------------------------------------------------------------------

echo.
pause
