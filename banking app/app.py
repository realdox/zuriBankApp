import random

# entry point 
# register page firstName LastName
# login page ,userName , account_number, Passsword
# account number generation
# banking operation
# database = dictionary {}

database = {}

def init():
    print("welcome to Zuri Bank\n Do you have account with us?\n","1. Register \n","2. Login.\n")
    haveAccount = int(input("press the key that match your interest:\n"))
    if haveAccount == 1:
        register()
    elif haveAccount == 2:
        login()
    else:
        print("wrong input")

def register():
    print("Welcome to Register Page\nplease fill in the detail below\n")
    firstName = input("Enter your FirstName:")
    lastName =  input("Enter your LasttName:")
    userName =  input("Enter your UsertName:")
    account_number = account_no_generator()
    print(account_number)
    database[account_number] = [firstName,lastName,userName] 
    return database   

def login():
    print("welcome to login Page kindly fill in your Data below to login to your account\n")


def account_no_generator():
    print("here is your account number:\n")
    return random.randrange(1111111111,9999999999)



init()
print(database)cd