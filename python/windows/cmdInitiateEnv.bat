@echo off
SET PATH=C:\Compilers\Python38\Scripts\;C:\Compilers\Python38\;%PATH%
python -m venv .venv
call .\.venv\Scripts\activate.bat
pip install -r requirements.txt