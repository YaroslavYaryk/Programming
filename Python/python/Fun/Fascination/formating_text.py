import re
"""
REGULAR EXPRESSION

\d  - any digits  [0-9]
\D  - any non digits
\w  - any Alphabet symbol [A-Z, a-z]
\W  - any non alphabet symbols
\s  - breakspace
\S  - non breakspace

'[A-Z][a-z]+' - first letter uppercase second lovercase to the end of the word

"\w+\.\w+"  - like "gmail.com", "ukr.net"
"""



def formaat_string(string:str):

    # string = string.lower().strip()
    string = re.findall(r'\w+\.\w+', string)
    # string = re.sub(r'[\s]', " && ", string)
    # string = re.sub(r'^-+|-+$', "", string)
    return string

print(formaat_string("duhanov2003@gmail.com duhanov2003@ukr.net  "))    


