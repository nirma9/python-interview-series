# file = open("data.txt","r")
# content = file.read()
# print(content)
# file.close()

#writing a file
# file = open("notes.txt","w")
# file.write("This is Day 5 of python interview series...\n Thanks for all...")
# file.close()

#appending the file...
# file = open("notes.txt","a")
# file.write("\n Adding more content at the end....")
# file.close()

# with open("notes.txt","r") as file:
#                content  = file.read()
#                print(content)

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist.")


