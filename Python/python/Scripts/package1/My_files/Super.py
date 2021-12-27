class Parents(object):
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def printa(self):
        print(type(self).__name__)
        print(f"can run: {self.can_run}")
        print(f"can fly: {self.can_fly}")


class Horse(Parents):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Bird(Parents):

    def __init__(self):
        super().__init__()
        self.can_fly = True


class Unicorn(Horse, Bird):
    pass


def main():
    horse = Horse()
    horse.printa()

    bird = Bird()
    bird.printa()

    unicorn = Unicorn()
    unicorn.printa()

if __name__ == "__main__":
    main()