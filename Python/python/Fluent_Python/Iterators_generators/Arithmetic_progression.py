


class ArithmeticProggression:
    
    def __init__(self, begin, step, end):
        self.begin = begin
        self.step = step
        self.end = end
        
    def __iter__(self):
        result = type(self.begin + self.step)(self.begin) # if (self.begin + self.step) is float 
        # result will be float as well we just make it the same type as operands(step)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            index +=1
            yield result
            result = self.begin + self.step*index     
            
            
a = ArithmeticProggression(1, .5 ,5)
print(list(a))            