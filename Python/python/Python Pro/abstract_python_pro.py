from abc import ABC, abstractmethod

class Predator(ABC):

    @abstractmethod
    def eat(self, prey):
        pass

class Bear(Predator):
    def eat(self, prey):
        print(f'Терзает {prey}!')

    def roar(self):
        print(f'can roar')    
    
class Owl(Predator):
    def eat(self, prey):
        print(f'Налетает на {prey}!')


class Chameleon(Predator):
    def eat(self, prey):
        print(f'Выстреливает язык в {prey}!')


if __name__ == '__main__':
    bear = Bear()
    bear.eat('оленя')
    bear.roar()
    owl = Owl()
    owl.eat('мышь')
    chameleon = Chameleon()
    chameleon.eat('муху')    