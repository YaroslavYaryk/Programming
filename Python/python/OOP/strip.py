class Strip_string(object):

    __slots__ = ("_storage")

    def __init__(self, storage):
        self._storage = storage

    def __call__(self, *args):
        if not isinstance(args[0], str):
            raise ValueError("must be string")
        else:
            return args[0].strip(self._storage)    
        
p1 = Strip_string("!.,;: ?")
print(p1("??hello world!!"))


def String_Strip(char):
    def Strings(stringle):
        if not isinstance(stringle, str):
            raise ValueError("must be string")
        else:
            return stringle.strip(char)
    return Strings

p1 = Strip_string("!.,;: ?")
print(p1("  ??Have fun!!"))
              