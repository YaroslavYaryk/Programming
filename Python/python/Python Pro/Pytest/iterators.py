class My_range(object):

    def __init__(self, start, end = None, step = 1):
        if end == None:
            self.start = 0
            self.end = start
        else:
            if start < end:
                self.start = start
                self.end = end
            else:
                self.start = end
                self.end = start 
        if step != 0:
            self.step = step
        else:
            raise ValueError("step cannot be zero")    

    def __iter__(self):
        curr = self.start
        while self.start < self.end:
            yield self.start
            self.start += self.step
                     


nums = My_range(4,5)
for u in nums:
    print(u)