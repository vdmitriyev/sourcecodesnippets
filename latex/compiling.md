### About

How to compile **tex** files with text editors used by me.

### TexStudio: Command for compiling tex file

Options -> Configure TexStudio -> Commands -> PdfLatex

```text
pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex|makeglossaries %|bibtex %|pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex|pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex|rm %.aux %.bbl %.blg %.dvi %.log %.out %.toc %.synctex.gz
```

### TexMaker: Command for the compiling tex file

```text
pdflatex -synctex=1 -interaction=nonstopmode %.tex|bibtex %|pdflatex -synctex=1 -interaction=nonstopmode %.tex|pdflatex -synctex=1 -interaction=nonstopmode %.tex|pdflatex -synctex=1 -interaction=nonstopmode %.tex|"C:/Program Files (x86)/Adobe/Reader 10.0/Reader/AcroRd32.exe" %.pdf|rm %.aux %.bbl %.blg %.dvi %.log %.out %.toc %.synctex.gz
```
