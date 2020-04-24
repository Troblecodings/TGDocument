import os
import subprocess

markdownDir = "markdown"
latexDir = "crosscompiled/latex"
htmlDir = "crosscompiled/html"
mainTexFileName = "main.tex"


def convertToFormat(outputDir: str, extension: str, inputArgs=None) -> None:
    for mdFile in os.listdir(markdownDir):
        inputPath = f"./{markdownDir}/{mdFile}"
        outputPath = f"./{outputDir}/{mdFile.replace('.md', extension)}"
        args = ["pandoc", inputPath, "-o", outputPath]
        if inputArgs is not None:
            args.extend(inputArgs)
        subprocess.run(args)


if __name__ == "__main__":
    convertToFormat(latexDir, ".tex")
    convertToFormat(htmlDir, ".html", ["--mathjax"])
