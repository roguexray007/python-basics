class MyClass:
    def __init__(self, number):
        self.myint = number
    
    
    def getNumber(self):
        return self.myint
        
        

myobj = MyClass(8)
print(myobj.getNumber())