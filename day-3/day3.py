# # class car:
# #                def __init__(self,brand):
# #                        self.brand = brand
# # car1 = car("Toyota")
# # print(car1.brand)


# # #what is object
# # car2 = car("Honda")
# # print(car2.brand)

# # #what is inheritance
# # class parent:
# #         def greet(self):
# #                 print("Hello from parent...")
               
# # class child(parent):
# #         pass
# # c = child()
# # c.greet()

# #what is polymorphism
# class dog:
#                def speak(self):
#                        print("bark...")
# class cat:
#         def speak(self):
#                 print("Meow")
# for animal in (dog(),cat()):
#         animal.speak()

#what  is encapsulation
class account:
        def __init__(self):
                self.__balance = 0
        def deposit(self,amount):
                self.__balance += amount
        def get_bal(self):
                return self.__balance
acc=account()
acc.deposit(500)
print(acc.get_bal())


#what is abstaction
from abc import ABC,abstractmethod

class vehicle(ABC):
        @abstractmethod
        def start_engine(self):
                pass
        
class car(vehicle):
        def start_engine(self):
                print("car engine started....")
v = car()
v.start_engine()
