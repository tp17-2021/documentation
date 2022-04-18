import os
import re

import config as c

def insert_code(text):
    """ Find all code commands and replace them with markdown syntax """

    code_cmd = r':::code source="/(.*)" :::'
    codes = re.findall(code_cmd, text)
    for code in codes:
        with open(code, "r") as f:
            code = f"```python\n{f.read()}\n```"
            text = re.sub(code_cmd, code, text)
    return text


def merge_documents() -> None:
    """ Merge all documents """

    output = ""
    for filename in c.FILENAMES:
        with open(filename, "r") as file:
            text = file.read() + "\n"
            text = insert_code(text)
            output += text

    with open("output.md", "w") as file:
        file.write(output)


def create_pdf() -> None:
    """ Create pdf from md """

    os.system("pandoc output.md -V geometry=margin=30mm --listings -H listings-setup.tex --css style.css -o output.pdf")
    # os.system("rm output.md")


if __name__ == "__main__":
    merge_documents()
    create_pdf()


# NOTES
# pandoc output.md -V geometry=margin=30mm --listings -H listings-setup.tex -o output.pdf
# pandoc --from=markdown -V geometry=margin=30mm --output=output.pdf output.md --highlight-style=espresso

# https://tex.stackexchange.com/questions/101717/converting-markdown-to-latex-in-latex