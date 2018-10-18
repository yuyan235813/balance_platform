@echo off
cd /d %~dp0
sqlite3 balance.db ".dump" > balance.sql
echo.
If errorlevel 1 (
    echo 发生错误！！！！！！！！
) Else (
    echo 成功生成 balance.sql
)
echo.
pause