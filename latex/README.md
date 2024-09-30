## About

Contains informatio on LaTeX. For exampole, how to compile **tex** files with text editors used by me.

### Overleaf

* https://overleaf.com/
	+ whenerver its possible, try to use this particular LaTeX editor

### TexStudio: Command for compiling tex file

Options -> Configure TexStudio -> Commands -> PdfLatex

```text
pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex|makeglossaries %|bibtex %|pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex|pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex|rm %.aux %.bbl %.blg %.dvi %.log %.out %.toc %.synctex.gz
```

Config for TexStudio here [texstudio.txsprofile](texstudio.txsprofile).

### TexMaker: Command for the compiling tex file

```text
pdflatex -synctex=1 -interaction=nonstopmode %.tex|bibtex %|pdflatex -synctex=1 -interaction=nonstopmode %.tex|pdflatex -synctex=1 -interaction=nonstopmode %.tex|pdflatex -synctex=1 -interaction=nonstopmode %.tex|"C:/Program Files (x86)/Adobe/Reader 10.0/Reader/AcroRd32.exe" %.pdf|rm %.aux %.bbl %.blg %.dvi %.log %.out %.toc %.synctex.gz
```

### LaTeX Hints

* Tables
    - Use ```h``` option for better placement
    - Create table in a separate file and then use ```\input{file.tex}```
