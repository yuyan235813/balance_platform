@echo off
cd /d %~dp0
del balance.db
sqlite3 balance.db ".read  balance.sql"
echo.
If errorlevel 1 (
    echo �������󣡣�������������
) Else (
    echo �ɹ����� balance.db
)
echo.
pause