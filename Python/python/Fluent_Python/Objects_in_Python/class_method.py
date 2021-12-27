class Voice(object):

    AAA = 123

    @classmethod
    def change_field(cls, value):
        cls.AAA = value


a =Voice()

a.change_field(125)
print(a.AAA)