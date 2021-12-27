employees = {
    "Alice": 100000,
    "Bob": 99817,
    "Carol": 122908,
    "Frank": 88123,
    "Eve": 93121,
}

print([(key, value) for key, value in employees.items() if value >= 100000])


text = """Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""

a = [[i for i in j.split() if len(i) > 3] for j in text.split("\n")]
# print(a)


a = """
filename = readFileDefault.py
f = open(filename)
lines = []
for line in f:
	lines.append(line.strip())

print(lines)
"""

b = [w.strip() for w in a]
print(b)
