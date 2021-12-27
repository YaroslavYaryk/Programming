from types import MappingProxyType

d = {1 : "123"}
d_unchanged = MappingProxyType(d)
d[123] = "dsd"
# d_unchanged[123] = "dsd"

print(d)
print(d_unchanged)