### Uvic Latex Co-op Report

This is the boilerplate I used for my third co-op report at the University of Victoria. An sample can be viewed at https://www.overleaf.com/read/mnrhvvxjwvdj and in the future on my personal website. Any changes are welcome. 

#### Latex Packages

For this report, the following packages of interest

* lwarp (used to create html from latex files)
* standard latex libraries (tables, figures and captions)
* koma-script book class

To view the download the basic latex version (no lwarp), click
[at commit 2.](https://github.com/FriendlyUser/ENGRCoopReportBoilerPlate/archive/194149a318fbc24933cebd162d1741dc8b693f42.zip]) should be identical to the sample found at overleaf.

A sample of lwarp output can be viewed on [github pages]( https://friendlyuser.github.io/ENGRCoopReportBoilerPlate/).

#### Getting started

To get started clone or download this repo, and update/replace my summary in reportContent.tex, as well as the letter of transmittal. Manually modify the word front page template (WTR Title Page Template.docx), and then save to pdf and include using includepdf.

See `WTR Title Page Template.pdf` and WTR Title Page Template.pdf

The letter of transmittal must be typed in using the verbatim tags, so that you can not worry about indents and line breaks, for example

```
\begin{verbatim}
 Faculty of Engineering
 P.O. Box 1800
 Victora, BsdC.
 V8W 2Y2
\end{verbatim}
```
Glossary entries can be added in glossaries.tex and the bibliography is in bibliography.tex.

##### Creating html files from source
If created html files is desired, then uncomment lwarp preamble and that should work fine, or just compile the print version of the latex file.

For more details please view https://ctan.org/pkg/lwarp?lang=en

###### Useful Links

This report template cannot be used without some understand of useful features for report writing available in latex, in particular glossary and reference management.

* https://en.wikibooks.org/wiki/LaTeX/Glossary
* https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management
* https://ctan.org/pkg/lwarp?lang=en

Additional, the sections specified in the UVIC co-op report template are in `summary.tex`,`introduction.tex`, `discussion.tex`, `conclusions.tex` and `reccomendations.tex`.

Keep in mind that summary must appear in the table of contents, this is done using 
```tex
\addcontentsline{toc}{section}{Summary}
```


