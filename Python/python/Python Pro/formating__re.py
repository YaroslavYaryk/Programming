import re

def remove_spaces(string:str): #remain ony one betveen each word

    string = string.strip()
    string = re.sub(r"\s+", " ", string)
    return string

def normalize(string): #make it in lovercase
    string = string.casefold()
    return string

def remove_quotes(string): #delete quotes
    string = re.sub(r" \"\"+ ", '', string)
    return string

def clean_all(string): #delete every structure
    string = remove_quotes(string)
    string = normalize(string)
    string =remove_spaces(string)
    return string

print(clean_all("HeLLo       WoRlD"))