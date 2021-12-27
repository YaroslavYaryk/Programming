import  string
alphabet = string.ascii_uppercase
class Just:

    __slots__ = ("side")

    def __init__(self, side):
        self.side = side

class Square(Just):
    def draw(self):
        for i in range(self.side):
            print("*   "* self.side)

class Triangle(Just):
    def draw(self):
        for i in range(self.side):
            print()
            for j in range(i):
                print(alphabet[i], end= "   ")


def main():
    square = Square(5)
    triangle = Triangle(5)
    square.draw()

    triangle.draw()


if __name__ == '__main__':
    main()