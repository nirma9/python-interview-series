# def decorator(original_function):
#                def wrapper():
#                               print("before execution...")
#                               original_function()
#                               print("After execution")
#                return wrapper
# @decorator
# def greet():
#         print("hello pthon Developer...")
# greet()
                       
def repeat(n):
               def decorator(func):
                       def wrapper():
                               for _ in range(n):
                                       func()
                       return wrapper
               return decorator

@repeat(8)
def say_hello():
        print("hello")
print(say_hello())