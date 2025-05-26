# a decorator is just another function which takes a functions and returns one.

def myDecorator(func):
    def wrapper(*args, **kwargs):
        print("something is happening before the function is called")
        func(*args, **kwargs)
        print("something is happening after the function is called")
    return wrapper

@myDecorator
def hello(name):
    print(f"hello {name}")


hello("Sekiro")





