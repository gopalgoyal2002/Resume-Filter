from nlp.extractText import extract_text_from_pdf
from nlp.extractEmail import extract_emails
from nlp.extractPhone import extract_phone_number
from nlp.extractName import extract_name_from_spacy,extract_entities_wih_custom_model
import os


def extract_details(list_of_paths):
    """
    list_of_paths: Takes the path of folder
    return: All details present in resume
    """

    # directory = path_of_folder
    data=[]
    text_data={}
    for filename in list_of_paths:
        f = filename
        # checking if it is a file
        
        text=""
        # try:
        text=extract_text_from_pdf(f)
        text_data[filename]=text
        # except:
        #     continue
        phone_number=extract_phone_number(text)
        email=""
        if(len(extract_emails(text))>=1):
            email=extract_emails(text)[0]
        name=extract_name_from_spacy(text)[0]
        deatils=extract_entities_wih_custom_model(resume_text=text,path_of_model=os.getcwd()+'/mainapp/nlp'+'/model')
        if('Name' not in deatils):
            deatils['Name']=[name]
        deatils['phone_number']=phone_number
        deatils['email']=email
        deatils['file_name']=filename
        data.append(deatils)
        print(" ".join(deatils['Name'][0].split()))
    return data,text_data

if __name__ == '__main__':
    
    path_of_folder='/Users/gopalgoyal/Aryma Labs/ResumeParser/NLP Resumes additional'
    data = extract_details(path_of_folder)
    result=[]
    for i in data:
        result.append(" ".join(i['Name'][0].split()))
    # print(result)
    