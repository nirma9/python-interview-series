# try:
#                a = 10/0
# except ZeroDivisionError :
#         print("Division by zero error....")
# else:
#         print("Division successfully....")
# finally:
#         print("operation ended....")


# try:
#                x = int("abc")
# except ValueError:
#         print("invalid value...")
# except ZeroDivisionError:
#         print("division error")

class negativevalue(Exception):
               pass
value = -10
try:
        if value <0:
                raise negativevalue("NEgative values r not allowed..")
except negativevalue as e:
        print("caught custom error:",e)