from rich.progress import track
from time import sleep
# from tqdm import tqdm

for  i in track(range(1,100)): # the same as tqdn but it looks a bit atractive
    sleep(0.1)
    
# for  i in tqdm(range(1,100)):
#     sleep(0.1)    