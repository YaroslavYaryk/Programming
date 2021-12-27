from pprint import pprint
import matplotlib.pyplot as plt


print = pprint

txt = [
    "lambda functions are anonymous functions.",
    "anonymous functions dont have a name.",
    "functions are objects in Python.",
]

mark = map(lambda x: (x, True) if "anonymous" in x else (x, False), txt)
mark2 = [(x, True) if "anonymous" in x else (x, False) for x in txt]
# print(list(mark))
# print("")
# print(mark2)


price = [
    [9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
    [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
    [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
    [7.1, 5.9, 4.8, 4.8, 4.7, 3.9],
]

# print([x[1::2] for x in price])


visitors = [
    "Firefox",
    "corrupted",
    "Chrome",
    "corrupted",
    "Safari",
    "corrupted",
    "Safari",
    "corrupted",
    "Chrome",
    "corrupted",
    "Firefox",
    "corrupted",
]
# print(visitors)


visitors[1::2] = visitors[::2]
# print(visitors)


cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
expected_cycles = cardiac_cycle[1:-2] * 10


# plt.plot(expected_cycles)
# plt.show()

companies = {
    "CoolCompany": {"Alice": 33, "Bob": 28, "Frank": 29},
    "CheapCompany": {"Ann": 4, "Lee": 9, "Chrisi": 7},
    "SosoCompany": {"Esther": 38, "Cole": 8, "Paris": 18},
}

illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
# print(illegal)

column_names = ["name", "salary", "job"]
db_rows = [
    ("Alice", 180000, "data scientist"),
    ("Bob", 99000, "mid-level manager"),
    ("Frank", 87000, "CEO"),
]

db = [dict(zip(column_names, row)) for row in db_rows]

print(db)
