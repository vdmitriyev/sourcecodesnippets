@echo off
REM @author Viktor Dmitriyev

REM
REM CHANGE THE LOCATIONS !!!!
REM  

echo "Starting copying files from various folders ... "

FOR /R "d:\tmp\data\" %%G in (.) DO (
 pushd %%G
	FOR %%F IN (.) DO copy %%F d:\tmp\backups\
 popd %%G
)

echo "You are done"