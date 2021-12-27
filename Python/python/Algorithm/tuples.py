from pprint import pprint
class Text(object):

    def __init__(self, text):
        self.text = text

    def get_most_common(self):
        storage = {}
        for word in self.text.split():
            if word in storage:
                storage[word] +=1
            else:
                storage[word] = 0
        max_key = max(storage, key=storage.get)
        return f"the most common one is '{str(max_key)}', {storage[max_key]} times "

    def get_the_longest(self):
        return(max(self.text.split(), key= len))


    def gett(self):
        return f"{self.get_most_common()}, the longest - {self.get_the_longest()}"    


a = "On July 29, 1958, Eisenhower signed the National Aeronautics and Space Act,\
     establishing NASA. When it began operations on October 1, 1958, NASA absorbed the 43-year-old NACA intact; \
         its 8,000 employees, an annual budget of US$100 million, three major research laboratories (Langley Aeronautical Laboratory,\
              Ames Aeronautical Laboratory,\
     and Lewis Flight Propulsion Laboratory) and two small test facilities. Elements of the Army Ballistic Missile Agency and the United States \
         Naval Research Laboratory were incorporated into NASA. A significant contributor to NASA's entry into the Space Race with the Soviet Union was the technology\
              from the German rocket program led by Wernher von Braun, \
         who was now working for the Army Ballistic Missile Agency (ABMA), which in turn incorporated the technology of American scientist Robert Goddard's earlier works.\
              Earlier research efforts within the US Air Force and many of ARPA's early space programs were also transferred\
     to NASA. In December 1958, NASA gained control of the Jet \ Propulsion Laboratory, a contractor facility operated by the California Institute of Technology." 
obj = Text(a)
pprint(obj.gett())   
