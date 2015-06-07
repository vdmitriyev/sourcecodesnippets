@echo off
REM @author Viktor Dmitriyev

REM @about Test checker that do following things:
REM		1. Sets path variable
REM		2. Compiles current solution
REM		3. Iterates test sub folder by copying test files as an input for solution
REM     4. Compare output of the solution with template output 

set path=%PATH%;.;D:\Contests\compilers\cpp\bin\;D:\Contests\compilers\fpc\2.2.4\bin\i386-win32\;D:\Contests\compilers\Java\jdk1.6.0_19\bin\;
if exist a.exe (del /F a.exe 2 > temp.temp)
g++ a.cpp
if not exist "a.exe" do (exit)
for %%t in (tests\??) do (
	cls
	echo --------------------------------- TEST %%t
	del /f input.txt output.txt > nul
	copy %%t input.txt > nul
	a.exe
	fc.exe %%t.a output.txt
	pause
)