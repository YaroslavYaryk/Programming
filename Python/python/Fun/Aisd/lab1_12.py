class Text(object):

    def __init__(self, text):
        self.text = text
        self._vowels = ["a", "o", "e","i","u","y"]
        self._work_list = []
        self.__brand_new = []

    def first_oper(self):
        self._work_list = self.text.split()[1::2]
        for word in self._work_list:
            for letter in word:
                if letter not in self._vowels:
                    self.__brand_new.append(letter)
        return self.__brand_new

    @staticmethod
    def remove_th_same(word):
        unique_list = []
        for el in list(word):
            if el not in unique_list:
                unique_list.append(el)
            else:
                continue
        return unique_list


    def get_all(self):
        return sorted(Text.remove_th_same(Text.first_oper(self)))           

text = Text("hello world and everybody")
print(text.get_all())

