# the code block below is for collecting user information and printing

from personDataAccess import PersonData

# These are our current members, stored in a text file
def CurrentMembers():
    ourUserList1 = PersonData(1)
    print(ourUserList1)

print("Current members:")
CurrentMembers()

print("Let's add a user to the text file:")
PersonData(2)
CurrentMembers()


