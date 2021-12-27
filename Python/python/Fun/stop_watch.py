from time import time
from tqdm import tqdm
from time import sleep
class Stop_watch(object):

    def __init__(self):
        self.__start = 0
        self.__start_all = time()
        self.__stop = 0

    def start(self):
        self.__start = time()

    def stop(self):
        self.__stop = time() - self.__start

    def show(self):
        return f"current time is {self.__stop}" 

    def __del__(self):
        print( f"the whole time is {time() - self.__start_all}")        


def main():
    obj = Stop_watch()
    a = int(input("1 - start\n2 - stop\n3 - finish\n: "))
    while a==1 or a ==  2:
        if a==1:
            print("starting...")
            obj.start()
        else:
            obj.stop()
            print(obj.show())
           
        a = int(input("enter: "))
    
    del obj 
                    
if __name__ == "__main__":
    main()                    

for i in tqdm(list(range(1,20))):
    sleep(0.4)