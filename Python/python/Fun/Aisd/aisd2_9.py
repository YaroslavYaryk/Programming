def remove_th_same(word):
        unique_list = []
        for el in list(word):
            if el not in unique_list:
                unique_list.append(el)
            else:
                continue
        return unique_list


def funk(text:str):
    notepad = text.split()
    x = [remove_th_same(i) for i in notepad]
    y = [j for i in x  for j in i if j not in "oeuiya"]
   
    result = sorted([i for i in y if y.count(i) == 1])
    

    print("letters are: " ,"".join(remove_th_same(result)))

funk(input("enter text:  "))    