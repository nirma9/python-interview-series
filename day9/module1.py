class underageerror(Exception):
               pass
def apply_for_licence(age):
        if age>18:
                raise underageerror("YOu must be atleast 18 to apply..........")
try:
        apply_for_licence(16) 
except underageerror as e:
        print("caught exception:", e)

class invalidcouponerror(Exception):
        pass
class stocklimitreachederror(Exception):
        pass
class unauthorizeddownloaderror(Exception):
        pass



class apperror(Exception):
        pass
class loginerror(Exception):
        pass
class paymenterror(Exception):
        pass
