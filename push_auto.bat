@echo off
set /p message=Message for commit:
git pull origin master
git add --all
git commit -m "%message%"
git push origin master