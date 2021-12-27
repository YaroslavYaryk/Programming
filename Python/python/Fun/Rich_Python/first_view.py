from rich import print, inspect
from rich.console import Console

#just print make it all easyer to read  

print(inspect('hello', methods = True)) #this one show the whole list of methids that we can 
#use for value in te first arguments
d = {1:1, 2:2, 3:3, 4:4}

# print(locals())

print("[red]hello, [blue]word :joy:") # in a brackets its color and then its an :"emoji":

console = Console()
console.print("[bold red]hello [bold green]world") # show the same as yust print
console.log("[bold red]hello [bold green]world") # show time in the left of the screen

