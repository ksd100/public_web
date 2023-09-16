ECHO OFF

C:

CLS

ECHO Launch the application

REM Edit startup time
TIMEOUT /T 180 /NOBREAK


REM Path of the exe folder
cd C:\Users\2023-02-02-XXXX\Develop\Exe

start "" "C:\Users\2023-02-02-XXXX\Develop\Exe\Node150\dafaApp.exe"

EXIT

