from fuzzywuzzy import fuzz, process

a = fuzz.ratio("hello world", "World Hello ")
print(a)