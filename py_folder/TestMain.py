def user_info(x):
    Users = []
    y = 1

    while x > 0:
        print("You are our user number",y)
        FirstName: str = input("  What is your first name: ")
        LastName: str = input("  What is your last name: ")
        user = [FirstName, LastName]
        Users.append(user)
        x = x-1
        y = y+1

    return Users