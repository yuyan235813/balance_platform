@echo off
cd /d %~dp0
sqlite3 balance.db ".dump" > balance.sql
echo.
If errorlevel 1 (
    echo �������󣡣�������������
) Else (
    echo �ɹ����� balance.sql
)
echo.
pause