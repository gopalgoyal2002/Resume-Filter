import fitz


def extract_text_from_pdf(Path_of_pdf_file : str):
    """
    Path_of_pdf_file: path of pdf file to extract the text
    return: text
    """
    doc = fitz.open(Path_of_pdf_file)
    text=""
    for page in doc:
        text += page.get_text()

    return text
