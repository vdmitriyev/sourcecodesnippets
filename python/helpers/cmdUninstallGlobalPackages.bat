@ECHO OFF

ECHO Please choose a Python version to manage: (e.g., 37, 38, 39, 310, 311, 312)
SET /P version=

CALL :ManagePythonVersion %version%
GOTO :END

REM Define a function to manage Python versions
:ManagePythonVersion version

SET PATH=C:\Compilers\Python%version%\Scripts\;C:\Compilers\Python%version%\;%PATH%

echo %version%
pip config set global.require-virtualenv False
pip freeze > %version%_all_packages.txt
cat %version%_all_packages.txt | grep -v "pip" > %version%_uninstall.txt

pip uninstall -r %version%_uninstall.txt -y

pip freeze > %version%_all_packages_left.txt
pip config set global.require-virtualenv True

ECHO Finished managing Python version %version%

EXIT /B 0  ; Exit the function after execution

:END
