@echo off
cd /d %~dp0
del balance.db
sqlite3 balance.db ".read  balance.sql"
echo.
If errorlevel 1 (
    echo 发生错误！！！！！！！！
) Else (
    echo 成功生成 balance.db
)
echo.
pause