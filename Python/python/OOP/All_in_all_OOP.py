from Examples_deskriptors import  NonNegative , Check_int_float, Check_string
class Person(object):

    storage = []
    style = ""

    __slots__ = ("_name", "_surname", "_age", "_someth_else")

    def __init__(self, name=None, surname=None, age=None, someth=None):

        if Person.__isstr(name, surname) and Person.__isint(age):
            self._name = name
            self._surname = surname
            self._age = age
            self._someth_else = someth

    @staticmethod
    def __isint(var):
        return isinstance(var, int)

    @staticmethod
    def __isstr(var, num="sss"):
        return isinstance(var, str) and isinstance(num, str)

    @property
    def pers(self):

        return f"Person( {self._name} {self._surname} {self._age} {self._someth_else} )"

    @pers.setter
    def pers(self, *args):

        assert len(args) != 0
        for elem in args:
            for g in elem:

                Person.storage.append(g)
        self._name = Person.storage[0]
        self._surname = Person.storage[1]
        self._age = Person.storage[2]
        self._someth_else = " ".join(Person.storage[3:])




class Teacher(Person):

    style = "teacher"

    # __slots__ = ("__pay")

    __pay = NonNegative()
    __pay = Check_int_float()

    def __init__(self, name=None, surname=None, age=None, someth=None, pay=None):
        super().__init__(name, surname, age, someth)
        self.__pay = pay

    @property
    def tech(self):
        return f"Teacher( {self._name} {self._surname} ({self._age} age - {Teacher.style}) (about: {self._someth_else}) (salary: {self.__pay}) )"

    def can_do(self):
        return f"I - {self._name} {self._surname} can do nothing and get {self.__pay} salary as a {Teacher.style} "



class Student(Person):

    style = "student"

    # __slots__ = ("__stypend")

    __stypend = NonNegative()
    __stypend = Check_int_float()


    def __init__(self, name=None, surname=None, age=None, someth=None, stypend=0):
        super().__init__(name, surname, age, someth)
        self.__stypend = stypend

    @property
    def study(self):

        return f"Teacher( {self._name} {self._surname} ({self._age} age - {Student.style}) (about: {self._someth_else}) (stypend: {self.__stypend}) )"

    def can_do(self):
        return f"I - {self._name} {self._surname} gotta do everyth to prove that i'm a great {Student.style}"

class Pupil(Person):

    style = "pupil"

    # __slots__ = ("__behavior")

    __behavior = Check_string()

    def __init__(self, name=None, surname=None, age=None, someth=None, behavior = None ):
        super().__init__(name, surname, age, someth)
        self.__behavior = behavior 

    @property
    def school(self):

        return f"Schoolmate( {self._name} {self._surname} ({self._age} age - {Pupil.style}) (about: {self._someth_else}) (behavior: {self.__behavior}) )"

    def can_do(self):
        return f"I - {self._name} {self._surname} have to work as hard as i can to learn everything that i need as {Pupil.style}"


class Programmer(Student):

    # __slots__ = ("__pr_lang", "styl?e_of_programming")

    __pr_lang = Check_string()

    def __init__(self, name=None, surname=None, age=None, someth=None, pr_lang=None):
        super().__init__(name, surname, age, someth)
        self.__pr_lang = pr_lang
        self.style_of_programming = None

    @property
    def pro(self):

        return f"Programmer( {self._name} {self._surname} ({self._age} age - {Programmer.style}) (about: {self._someth_else}) (salary: much) )"

    def can_do(self):
        if self.style_of_programming is None:
            if self.__pr_lang == "Python":
                self.style_of_programming = "great job bro Python is a powerful programming language"
            elif self.__pr_lang == "C++":
                self.style_of_programming = "great job bro but you have to work hard to succeed in C++"
            elif self.__pr_lang == "Java":
                self.style_of_programming = "great job bro a don't know mach about Java. but good luck"
            else:
                self.style_of_programming = "great job bro have a good way of programming"
        

        return f"I - {self._name} {self._surname} - {self.style_of_programming}"
    


teacher1 = Teacher("Yaroslav", "Dyhanov", 33, "teacher of Math", 10000)
teacher2 = Teacher("Olha", "Dyhanova", 25, "teacher of biology", 15000)

student1 = Student("Yaroslav", "Dyhanov", 17, "study softwere ingeneering", 0)
pupil = Pupil("Olha", "Dyhanova", 15, "study chemical technology", "Pretty good")

progarammer1 = Programmer("Ilon", "Musk", 45, "the creator of Tesla", "Python")
progarammer2 = Programmer("Yaroslav", "Dyhanov", 24, "working softwere ingeneering", "C++")

a = [teacher1, teacher2, student1, pupil, progarammer1, progarammer2]
for i in a:
    print(i.can_do())
