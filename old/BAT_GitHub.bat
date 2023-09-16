@echo off

cd %~dp0


git add .

rem Enter your commit message
set /p commit_msg=Enter commit message: 
git commit -m "%commit_msg%"

git push

pause