@echo off
cd /d %~dp0
set YYYYmmdd=%date:~0,4%%date:~5,2%%date:~8,2%
set hhmiss=%time:~0,2%%time:~3,2%%time:~6,2%
sqlite3 balance.db ".dump" > balance_%YYYYmmdd%%hhmiss%.sql
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