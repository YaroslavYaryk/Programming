

class Point(object):
    def __init__(self):
        self.a = 10
    def pou(self):
        return self.a 

    def __str__(self):
        return str(self.a)    

if __name__ == '__main__':
    an = Point()
    print(an.pou())
    print("hello.world")
    print("hey")
    print(an)