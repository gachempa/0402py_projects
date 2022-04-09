from TestMain import user_info

NumberOfUsers = int(input("How many users do you want to collect the information from?"))
OurUserList = user_info(NumberOfUsers)
print("Your first name is ", (OurUserList[1])[0])

