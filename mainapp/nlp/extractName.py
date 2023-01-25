import os
import spacy
from spacy.matcher import Matcher
from nlp.extractText import extract_text_from_pdf
def extract_name_from_spacy(resume_text):
    """
    resume_text: text to find name in string formet using spacy model
    return: Name of the presons
    """
    names=[]

    nlp = spacy.load('en_core_web_sm')
    try:
        matcher=Matcher(nlp.vocab)
        text=nlp(resume_text)
        NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
        pattern = [NAME_PATTERN]
        matcher.add('NAME', None, *pattern)

        matches = matcher(text)

        for _, start, end in matches:
            span = text[start:end]
            if 'name' not in span.text.lower():
                names.append(span.text)
    except:
        return [" "]
    if(len(names)==0):
        names.append(" ")
    return names

def extract_entities_wih_custom_model(resume_text,path_of_model):
    """
    resume_text: text to find name in string formet using custom spacy model
    return: Name of the presons
    """
    print(path_of_model)
    nlp = spacy.load(path_of_model)
    custom_nlp_text=nlp(resume_text)
    entities = {}
    for ent in custom_nlp_text.ents:
        if ent.label_ not in entities.keys():
            entities[ent.label_] = [ent.text]
        else:
            entities[ent.label_].append(ent.text)
    for key in entities.keys():
        entities[key] = list(set(entities[key]))
    return entities