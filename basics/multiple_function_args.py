def fixedArgFunction(arg1, arg2):
    print("fixedArgFunction - ")
    print(arg1, arg2)
    

def variableArgFunction(*args):
    print("variableArgFunction - ")
    for arg in args:
        print(arg, end=" ")
    print()
    

def keywordArgFunction(**kwargs):
    print("keywordArgFunction - ")
    for key, value in kwargs.items():
        print(key, value)
        
    
    
fixedArgFunction(1, 2)
variableArgFunction(1, 2, 3, 4, 5)
keywordArgFunction(name="John", age=25, city="New York")



