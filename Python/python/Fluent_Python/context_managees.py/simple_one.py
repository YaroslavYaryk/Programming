class File(object):
    
    def __init__(self, file, mode):
        self._filenale = file
        self.mode = mode
        
    def __enter__(self):
        self.__file = open(self._filenale, self.mode)
        return self.__file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.__file.close()
        
        
with File("hello.txt", "a") as f:
    for word in ("hello world, bro").split():
        f.write(word + '\n' )
                
        