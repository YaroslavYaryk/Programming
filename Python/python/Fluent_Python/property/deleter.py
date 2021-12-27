class ChaosKnife:
    
    def __init__(self):
        self.__members = ["hand", "the other hand",
                        "feet", "the other feet"]
        
        self.__phrases = ["it's just a scratch",
                        "it's not a big deal",
                        "i'm immortal",
                        "alright deal with dead heap"]
        
    @property
    def member(self):
        print("the next one is: ")
        return self.__members[0]
    
    
    @member.deleter
    def member(self):
        print(f"Chaos Knife lost {self.__members.pop(0)}\n{self.__phrases.pop(0)}")
            
            
king = ChaosKnife()
print(king.member)  
del king.member          
del king.member
del king.member
del king.member