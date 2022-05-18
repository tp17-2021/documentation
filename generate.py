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


def find_links(text):
    """
    Find all image links in document, replace them in documents and copy to
    root directory.
    """

    links_to_detele = []
    links = re.findall(r"!\[\]\((.*)\)", text)
    for link in links:
        link = link.split()[0][1:]
        new_link = "".join(link.split("/"))
        # print(new_link)
        text = re.sub(rf"/{link}", new_link, text)
        os.system(f"cp {link} {new_link}")
        links_to_detele.append(new_link)
        
    return text, links_to_detele

def merge_documents() -> list:
    """ Merge all documents and return found links to be deleted """

    output = ""
    links_to_detele = []
    for filename in c.FILENAMES:
        with open(filename, "r") as file:
            text = file.read() + "\n"
            text, links = find_links(text)
            text = insert_code(text)

            links_to_detele.extend(links)
            
            if "/" in filename:
                if "user_guide" in filename:
                    count = filename.count("/")-1
                else:
                    count = filename.count("/")-1

                depth = count * "#"
                headers = re.findall(r"^#.*", text, flags=re.MULTILINE)
                for header in headers:
                    new_header = f"{depth}{header}"
                    # print(header, new_header)
                    text = re.sub(header, new_header, text)

            if filename == "technical_documentation/server/modules/database.md":
                text = re.sub(r"### Databáza", "## Moduly\n### Databáza", text)

            if filename in ["index.md", "technical_documentation/voting_terminal.md", "user_guide/voting_terminal.md"]:
                text = "\\newpage\n" + text

            output += text



    # remove retype order section
    output = re.sub(r"---\n.*", "", output)

    with open("documentation.md", "w") as file:
        file.write(output)

    return links_to_detele


def create_pdf() -> None:
    """ Create pdf from md """

    os.system("markdown-enum documentation.md 1 documentation.md")

    output = ""
    with open("documentation.md") as file:
        text = file.read()
        headers = re.findall(r"^#.*", text, flags=re.MULTILINE)
        for header in headers:
            if header.count("#") >= 4:
                new_header = re.sub(r"\d.", "", header)
                text = re.sub(header, new_header, text)
        output = text

    with open("documentation.md", "w") as file:
        file.write(output)

    os.system("pandoc --pdf-engine=xelatex --toc documentation.md -V geometry=margin=30mm --listings -H listings-setup.tex --css style.css -o documentation.pdf")
    # os.system("rm documentation.md")


def delete_links(links) -> None:
    """ Delete all links from root directory """

    for link in links:
        os.system(f"rm {link}")


if __name__ == "__main__":
    links_to_detele = merge_documents()
    create_pdf()
    delete_links(links_to_detele)



# NOTES
# pandoc output.md -V geometry=margin=30mm --listings -H listings-setup.tex -o output.pdf
# pandoc --from=markdown -V geometry=margin=30mm --output=output.pdf output.md --highlight-style=espresso

# https://tex.stackexchange.com/questions/101717/converting-markdown-to-latex-in-latex