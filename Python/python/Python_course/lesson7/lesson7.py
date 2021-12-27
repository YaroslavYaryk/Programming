import sys
import os.path
# print(sys.argv) #show the full path to current file
# print(sys.path) #show the path of python modules
module = os.path.join("..", "OOP")
sys.path.append(module)
# print(sys.path)
# import Examples_deskriptors
# print(__file__) # show the absolute path to the python file
# print(os.path.abspath("someth")) # the same as above
# os.path.basename() -  відсікає все до останнього "\"
files = "a\\b\\c"
# print(os.path.basename(files))
# os.path.dirname() - відсікає справа до першого "\" "
# print(os.path.dirname(files))

current = os.path.dirname(os.path.abspath(__file__)) # берем папку в якій current файл 
path = os.path.dirname(current) #на рівень вище від тієї папи
module = os.path.join(path, "OOP") # додаєм папку ООП
sys.path.append(module)
import Class
