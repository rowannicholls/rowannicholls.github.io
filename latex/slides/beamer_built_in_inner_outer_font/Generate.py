"""Generate LaTeX slides."""
import os
from pathlib import Path

root_dir = os.path.dirname(os.path.abspath(__file__))

# Export to RMD file
rmd = open('themes.Rmd', 'w')
rmd_content = """---
title: '<font size="5">Slides in LaTeX:</font><br>Built-In Beamer Themes:<br><font size="5">Inner, Outer and Font Themes</font>'
output:
    html_document:
        theme: paper
        highlight: textmate
        # number_sections: true
        # toc: true
        includes:
            before_body: ../../../google_analytics.html
---

<font size="3">

[⇦ Back](../../../latex.html)

Beamer has:

- 5 built-in **inner themes**: default, circles, inmargin, rectangles and rounded
- 9 built-in **outer themes**: default, infolines, miniframes, shadow, sidebar, smoothbars, smoothtree, split and tree
- 6 built-in **font themes**: default, professionalfonts, serif, structurebold, structureitalicserif, structuresmallcapsserif

The above are demoed on this page. Other themes which Beamer has but which are demoed [here](../beamer_built_in_presentation_colour/themes.html) instead of on this page include:

- 29 built-in **presentation themes** (often just called "themes")
- 19 built-in **colour themes**

See the package page on CTAN [here](https://ctan.org/pkg/beamer) and the full documentation [here](https://mirror.ox.ac.uk/sites/ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf).

{.tabset}
=========
**Inner Themes:**

"""
rmd.write(rmd_content)

tex_content = r"""
% Easy access to the Lorem Ipsum and other dummy texts
\usepackage{lipsum}
% Sophisticated verbatim text
\usepackage{fancyvrb}
% Tune the output format of dates according to language
% - UKenglish: use "ddth MMMM yyyy" format
% - cleanlook: remove the -st/-nd/-rd/-th suffix
\usepackage[UKenglish, cleanlook]{isodate}

% Title material
\title{Example Beamer Slides}
\author{Rowan Nicholls}
\institute{Oxford, England}
\date{\today}

\begin{document}

\begin{frame}[plain]
    \titlepage
\end{frame}

\section{First Section}
\subsection{First Subsection}
\begin{frame}
    \frametitle{Example Slide}
    \framesubtitle{Text, Columns, Lists}
    \begin{columns}
        \column{0.5\textwidth}
        \lipsum[1][1-6]
        \column{0.5\textwidth}
        Itemised list:
        \begin{itemize}
            \item First Item
            \item Second Item
            \begin{itemize}
                \item First Sub-item
                \item Second Sub-item
            \end{itemize}
        \end{itemize}
        Enumerated list:
        \begin{enumerate}
            \item First Item
            \item Second Item
            \begin{enumerate}
                \item First Sub-item
                \item Second Sub-item
            \end{enumerate}
        \end{enumerate}
    \end{columns}
\end{frame}

\section{Second Section}
\subsection{Second Subsection}
\begin{frame}[fragile]
    \frametitle{Example Slide}
    \framesubtitle{Blocks, Tables, Verbatim}
    \begin{block}{Pythagorean Theorem}
        $ a^2 + b^2 = c^2$
    \end{block}
    \begin{table}
        \caption{2022–23 Premier League}
        \begin{tabular}{c | l | c | c | c | c | c }
            Pos & Team & Pld & W & D & L & Pts \\
            \hline \hline
            1 & Manchester City & 38 & 28 & 5 & 5 & 89\\
            2 & Arsenal & 38 & 26 & 6 & 6 & 84\\
            3 & Manchester United & 38 & 23 & 6 & 9 & 75
        \end{tabular}
    \end{table}
    For \texttt{verbatim} to work, you need the \texttt{fragile} frame option:
    \begin{verbatim}
        \begin{frame}
            \frametitle{A Frame Within A Frame}
            Lorem ipsum dolor sit...
        \end\{frame}
    \end{verbatim}
\end{frame}

\appendix
\begin{frame}%[allowframebreaks]
    \frametitle{Bibliography}
    Use \texttt{cite} to create in-text citations\cite{Autor1990, Jemand2000}.
    \vspace{24pt}
    \begin{thebibliography}{10}
        \setbeamertemplate{bibliography item}{\insertbiblabel}
        \bibitem{Autor1990}
            A Autor
            \newblock{\em Introduction to Giving Presentations}.
            \newblock Klein-Verlag, 1990.
        \bibitem{Jemand2000}
            S Jemand
            \newblock On this and that.
            \newblock{\em Journal of This and That}, 2(1):50--100, 2000.
    \end{thebibliography}
\end{frame}

\end{document}
"""

# themes = [
#     'default',
#     'boxes',
#     'AnnArbor',
#     'Antibes',
#     'Bergen',
#     'Berkeley',
#     'Berlin',
#     'Boadilla',
#     'CambridgeUS',
#     'Copenhagen',
#     'Darmstadt',
#     'Dresden',
#     'EastLansing',
#     'Frankfurt',
#     'Goettingen',
#     'Hannover',
#     'Ilmenau',
#     'JuanLesPins',
#     'Luebeck',
#     'Madrid',
#     'Malmoe',
#     'Marburg',
#     'Montpellier',
#     'PaloAlto',
#     'Pittsburgh',
#     'Rochester',
#     'Singapore',
#     'Szeged',
#     'Warsaw',
# ]
# colours = [
#     'default',
#     'albatross',
#     'beaver',
#     'beetle',
#     'crane',
#     'dolphin',
#     'dove',
#     'fly',
#     'lily',
#     'monarca',
#     'orchid',
#     'rose',
#     'seagull',
#     'seahorse',
#     'sidebartab',
#     'spruce',
#     'structure',
#     'whale',
#     'wolverine',
# ]
inner_themes = [
    'default',
    'circles',
    'inmargin',
    'rectangles',
    'rounded',
]
outer_themes = [
    'default',
    'infolines',
    'miniframes',
    'shadow',
    'sidebar',
    'smoothbars',
    'smoothtree',
    'split',
    'tree',
]
font_themes = [
    'default',
    'professionalfonts',
    'serif',
    'structurebold',
    'structureitalicserif',
    'structuresmallcapsserif',
]

for inner_theme in inner_themes:
    # Export to RMD file
    rmd.write('## ' + inner_theme + r' {.tabset}' + '\n')
    rmd.write('**Outer Themes:**' + '\n')
    rmd.write('\n')

    for outer_theme in outer_themes:
        # Export to RMD file
        rmd.write('### ' + outer_theme + r' {.tabset}' + '\n')
        rmd.write('**Font Themes:**' + '\n')
        rmd.write('\n')

        for font_theme in font_themes:
            # Export to RMD file
            rmd.write('#### ' + font_theme + r' {.tabset}' + '\n')

            # Create folder
            folder = Path(inner_theme, outer_theme, font_theme)
            print(folder)
            folder.mkdir(parents=True, exist_ok=True)

            #
            # Export to RMD file
            #
            # Images of slides
            rmd.write(
                f'<img src="{inner_theme}/{outer_theme}/{font_theme}/' +
                'Example-1.png" style="width:49%; ' +
                'padding:4px; border:1px solid #000;">' + '\n'
            )
            rmd.write(
                f'<img src="{inner_theme}/{outer_theme}/{font_theme}/' +
                'Example-2.png" style="width:49%; ' +
                'padding:4px; border:1px solid #000;">' + '\n'
            )
            rmd.write(
                f'<img src="{inner_theme}/{outer_theme}/{font_theme}/' +
                'Example-3.png" style="width:49%; ' +
                'padding:4px; border:1px solid #000;">' + '\n'
            )
            rmd.write(
                f'<img src="{inner_theme}/{outer_theme}/{font_theme}/' +
                'Example-4.png" style="width:49%; ' +
                'padding:4px; border:1px solid #000;">' + '\n'
            )
            rmd.write('\n')
            rmd.write('**Code to reproduce these slides:**' + '\n')
            rmd.write('\n')
            # LaTeX code snippets
            rmd.write('```text' + '\n')
            rmd.write(r'\documentclass{beamer}' + '\n')
            rmd.write('\n')
            rmd.write(r'\usetheme{Madrid}' + '\n')
            rmd.write(r'\usecolortheme{seagull}' + '\n')
            rmd.write(r'\useinnertheme{%s}' % inner_theme + '\n')
            rmd.write(r'\useoutertheme{%s}' % outer_theme + '\n')
            rmd.write(r'\usefonttheme{%s}' % font_theme + '\n')
            rmd.write(tex_content)
            rmd.write('```' + '\n')
            rmd.write('\n')
            rmd.write('[⇦ Back](../../../latex.html)' + '\n')
            rmd.write('\n')

            # Check if folder contents already exists
            if 'Example.tex' not in os.listdir(folder):
                # Export to TEX file
                filepath = Path(folder, 'Example.tex')
                file = open(filepath, 'w')
                file.write(r'\documentclass{beamer}' + '\n')
                file.write('\n')
                file.write(r'\usetheme{Madrid}' + '\n')
                file.write(r'\usecolortheme{seagull}' + '\n')
                file.write(r'\useinnertheme{%s}' % inner_theme + '\n')
                file.write(r'\useoutertheme{%s}' % outer_theme + '\n')
                file.write(r'\usefonttheme{%s}' % font_theme + '\n')
                file.write(tex_content)
                file.close()

            # Check if folder contents already exists
            if 'Example.pdf' not in os.listdir(folder):
                # Run LaTeX
                os.chdir(folder)
                os.system('pdflatex -interaction=batchmode Example.tex')
                # os.system('bibtex Example')
                os.system('pdflatex -interaction=batchmode Example.tex')
                # os.system('pdflatex Example.tex')
                # Delete intermediate files
                files = os.listdir()
                to_keep = ('.tex', '.pdf')
                for file in [f for f in files if not f.endswith(to_keep)]:
                    os.system('rm "{}"'.format(file))
                os.chdir(root_dir)

            # Check if folder contents already exists
            if 'Example-4.png' not in os.listdir(folder):
                # Create PNG image
                os.chdir(folder)
                os.system('pdftoppm -png Example.pdf Example')
                os.chdir(root_dir)

rmd.write('</font>' + '\n')
rmd.write('\n')
rmd.close()
