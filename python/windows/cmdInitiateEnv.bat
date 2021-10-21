@echo off
setlocal
:PROMPT
SET AREYOUSURE=N
SET /P AREYOUSURE=Do you want to create new virtual environment (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

SET PATH=C:\Compilers\Python38\Scripts\;C:\Compilers\Python38\;%PATH%
python -m venv .venv
call .\.venv\Scripts\activate.bat
pip install -r requirements.txt

:END
endlocal
