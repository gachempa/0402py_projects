

from jan22_functions.userInfo import personalInformation
#"""#""" the code block below is for collecting user information and printing

#from jan22_functions.personDataAccess import PersonData

from TestMain import user_info

NumberOfUsers = int(input("How many users do you want to collect the information from?"))
OurUserList = user_info(NumberOfUsers)
print("Your first name is ", (OurUserList[1])[0])

#print(OurUserList[1])

# """ the code block below is for reading from a file

#print(PersonData(2))

# """





# class OurUsers:
#     pass


# OurUsers = [personalInformation()]
#
# print(OurUsers[0])

# print(personalInformation())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
