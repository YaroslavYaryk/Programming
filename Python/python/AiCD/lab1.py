from tqdm import tqdm
from time import sleep
import unittest

class Show_vowels(unittest.TestCase):

    # to save our memory and create it only for this method
    __slots__ = ("__text", "__list_storage",
                  "__brand_new", "result")

    def __init__(self, text) -> None:  # inicialization of our class
        self.__text = text
        self.__list_storage = []
        self.__brand_new = []
        self.result = []


    @staticmethod #if there are two equal letters , delete one of them
    def remove_th_same(word) -> list:
        unique_list = []
        for el in list(word):
            if el not in unique_list:
                unique_list.append(el)
            else:
                continue
        return unique_list

    @staticmethod #if there are ywo equal letters , delete both
    def remove_elem(word: list):
        char = []
        for i in word:
            if word.count(i) == 1:
                char.append(i)
        return char

    # makes the main operation , show letters that there is in one word
    #and append to __list_storage
    @property
    def main_opeation(self) -> list:
        lst_word = self.__text.split()
        for word in lst_word:
            self.__list_storage.append(Show_vowels.remove_th_same(word))
        return self.__list_storage

    @property
    def add_to_new_list(self) -> list:  # thats because we need to get rid of the same letters
        for element in self.main_opeation:
            for letter in element:
                self.__brand_new.append(letter)
        self.__brand_new = Show_vowels.remove_elem(self.__brand_new)    
        return self.__brand_new

    @property
    def remove_vawels(self) -> list:
        vowels = ["a", "e", "u", "y", "i", "o"]

        for letter in self.add_to_new_list:
            if letter in vowels:  # remove the vowels from our set()
                self.__brand_new.remove(letter)
        return self.__brand_new

    def show_result(self):  # show the whole infjrmation
        self.result = " ".join(sorted(self.remove_vawels))

        return self.result
    
    @property
    @unittest.expectedFailure
    def test_result(self):
        self.assertCountEqual(self.result , "h w r d" , "NO" )



def main():
    a = input("enter text: ")
    obj = Show_vowels(a)
    print("preparing...")
    # for item in tqdm(list(range(100))):
    #     sleep(0.05)
    print("the letters are - (", obj.show_result(), ")")
    obj.test_result


if __name__ == "__main__":
    main()

    
