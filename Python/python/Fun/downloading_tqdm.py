from tqdm import tqdm
from time import sleep

data = list(range(1,101))
for item in tqdm(data):
    sleep(0.1)
print("hello world")    

