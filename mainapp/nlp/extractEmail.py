import re
 
from nlp.extractText import extract_text_from_pdf
 
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
 
 
def extract_text_from_pdf(pdf_path):
    return extract_text_from_pdf(pdf_path)
 
 
def extract_emails(resume_text):
    """
    resume_text: text to find email in string formet
    return: email
    """
    emails=re.findall(EMAIL_REG, resume_text)
    return emails
 
 
if __name__ == '__main__':
    # text = extract_text_from_pdf('resume.pdf')
    text=""
    emails = extract_emails(text)
 
    if emails:
        print(emails[0])