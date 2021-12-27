from rich.console import Console
from rich.table import Table
import time 
import sys

sys.setrecursionlimit(10**6)


start1 = time.perf_counter()
def pow_reccursive(num,degree) -> int:
    if degree == 0:
       return num
    else:
        return (num* pow_reccursive(num, degree-1))

pow_reccursive(20,2417)
finish1 = round(time.perf_counter() - start1, 7)

start2 = time.perf_counter()
def pow_simple(num, degree) -> int:
    result = num

    for i in range(1,degree):
        result *= num

    return result

(pow_simple(20,2417))
finish2 = round(time.perf_counter() - start2, 7)



table = Table(title="Time analysing")
table.add_column("method", style = "red", no_wrap=True)
table.add_column("time", style = "cyan", no_wrap=True)

table.add_row("pow_reccursive", str(finish1))
table.add_row("pow_simple", str(finish2))

console = Console()
console.print(table)


