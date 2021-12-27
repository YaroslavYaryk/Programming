import diamond

class A():

    def ping(self):
        print("ping ", self)


class B(A):

    def pong(self):
        print("pong ", self)


class C(A):

    def pong(self):
        print("PONG ", self)


class D(B, C):

    def ping(self):
        A.ping(self)
        print("ping-pong ", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()      
        C.pong(self)


d = D()
# C.pong(d)    
# d.pingpong()         