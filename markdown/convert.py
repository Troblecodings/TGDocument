import os
import subprocess

markdownDir = "."
htmlDir = "../docs/html"
mainTexFileName = "main.tex"

mdFileList = [
    fileName for fileName in os.listdir(markdownDir)
    if os.path.isfile(fileName)
    and fileName.endswith(".md")
]


def convertToFormat(outputDir: str, extension: str, inputArgs=None) -> None:
    for mdFile in mdFileList:
        inputPath = os.path.join(markdownDir, mdFile)
        outputPath = os.path.join(
            outputDir, mdFile.replace('.md', extension))
        args = ["pandoc", inputPath, "-o", outputPath]
        if inputArgs is not None:
            args.extend(inputArgs)
        subprocess.run(args)
    print(f"Finished converting to {extension}")


def convertToPdf() -> None:
    pdfFolderPath = os.path.join("..", "pdf")
    args = [
        "pandoc",
        "-o", os.path.join(pdfFolderPath, "main.pdf"),  # output path
        "--standalone",
        "--metadata-file=metadata.yaml",
        "--include-in-header=" + os.path.join(pdfFolderPath, "preamble.tex"),
        "--table-of-contents",
        "--number-sections"
    ]
    args.extend(mdFileList)
    subprocess.run(args)
    print(f"Finished converting to .pdf")


if __name__ == "__main__":
    convertToFormat(htmlDir, ".html", ["--mathjax"])
    convertToPdf()
