def User_Info():

    firstName: str = input("  What is your first name: ")
    lastName: str = input("  What is your last name: ")
    email: str = input(" What is your email ID: ")
    mobilePhoneNo: str = input(" What is your mobile phone number: ")
    user = [firstName, lastName, email, mobilePhoneNo]
    return user