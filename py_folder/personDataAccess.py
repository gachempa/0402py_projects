from userMain import User_Info

# opening the file
# x= 1, to read; x = 2 to write

def PersonData(x):
    if x == 1:
        pTxt = open(r"personModel.txt", "r")
        return pTxt.read()

    if x == 2:
        pTxt = open(r"personModel.txt", "a")
        newUser = User_Info()
        print(newUser)
        str1 = ",".join(newUser)
        print(str1)
        pTxt.write("\n")
        pTxt.write(str1)
        pTxt.close()
