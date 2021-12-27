def reverse(string):
    text1 = string.lower()
    text2 = text1.replace(" ", "")
    return text2[::-1]

def is_palindrome(string):
    text1 = string.lower()
    text2 = text1.replace(" ", "")
    return text2 == reverse(string)
    
something = input('Введите текст: ')
if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")



    