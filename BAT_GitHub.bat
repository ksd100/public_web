@echo off
setlocal
set /p comment="commit message:"
cd %~dp0
git add . && ^
git commit -m %comment% && ^
git push -u origin main
pause
exit /b 0