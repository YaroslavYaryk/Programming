def funk(text):
    new_text = []
    main_text = text.strip(".").split()
    for word in main_text[1:]:
        if word != main_text[0]:
            new_text.append((word))
    
    for i in range(len(new_text)):
        if new_text[i][-1] == new_text[i][-2]:
            return (new_text[i])
   
    return "empty" 

    
print(funk(input("text: ")))

