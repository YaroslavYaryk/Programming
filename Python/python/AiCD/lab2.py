def funk(text):
    new_text = []
    main_text = text.strip(".").split()
    for word in main_text[:-1]:
        if word !=main_text[-1]:
            new_text.append(list(word))
             
    for i in range(len(new_text)):
        new_text[i].append(new_text[i][0])
        new_text[i].remove(new_text[i][0])

    for word in new_text:
        for letter in word:
            print(letter, end='')
        print(end= " / ")    

def main():
    print()
    a = input("enter the text separated ( ): ")
    print("the words are: ", end='  ' )
    funk(a)
    print()            

if __name__ == '__main__':
    main()
