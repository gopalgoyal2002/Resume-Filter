import re
import subprocess  # noqa: S404
 
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
 
 
def extract_phone_number(resume_text):
    """
    resume_text: text to find phone_number in string formet
    return: phone number
    """
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])
 
        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None
 
 
if __name__ == '__main__':
    text = ""
    phone_number = extract_phone_number(text)
 
    print(phone_number)  # noqa: T001