@echo off
REM @author Viktor Dmitriyev

REM
REM CHANGE FILE TYPES IF NEEDED
REM

echo "Deleting old file with all bibtex-es."
del _bibtex_library.bib
echo "Creating new collectiong from existing bibtex-es."
copy /b *.bib _bibtex_library.bib
