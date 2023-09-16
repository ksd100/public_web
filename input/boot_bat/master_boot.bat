ECHO OFF

C:

CLS

ECHO Launch the application

REM Edit startup time
TIMEOUT /T val_Time /NOBREAK


REM Path of the exe folder
cd val_ExePath

start "" "val_ExePath\Nodeval_Node\val_App.exe"

EXIT

