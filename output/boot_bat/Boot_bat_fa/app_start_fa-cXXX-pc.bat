ECHO OFF

C:

CLS

ECHO 専用アプリケーションを起動します。

REM 起動時間を編集
TIMEOUT /T val_Time /NOBREAK


REM エグゼフォルダの場所
cd val_ExePath

start "" "val_ExePath\Spv\Nodeval_Node\SPV250d.exe"

EXIT

