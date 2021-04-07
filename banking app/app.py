import random
# entry point
#register
#account number generation
#login
#validation
# Bank operation
# database
# exit


# database = [] it would have been great but in the end i have to make choice so i go with dictionary
database = {}



def init():
    print("*******  welcome to ZURI Bank******\n thanks for banking with us\n")
    isUser = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    if isUser == 1:
        login()
    elif isUser == 2:
        register()
    else:
        print("wrong input")
        init()

def register():
    print("welcome to ZURI BANK register page\n")
    firstName = input("enter your firstname:")
    lastName = input("enter your lastname:")
    email = input("enter your email:")
    password = input("choose your password:")
    print("Account created successfully\n")
    print(" == ==== ====== ===== ===")
    account_number = accountNumberGen()
    print("account number: {}".format(account_number))
    # database creation(thought of using this but i will loose my data because i will love to display the lastname in the login page
    # database.append({account_number:[firstName,lastName,email]})
    database[account_number] = [firstName,lastName, email, password]
    login()


def login():
    print("*********Welcome to Zuri Bank Login Page kindly fill in your details *********** ")
    account_number = int(input("enter your Account number:\n"))
    password = input("enter your password:\n")

    for userAccountNo,userData in database.items():
        if userAccountNo == account_number:
            if userData[3] == password:
                print("welcome {}".format(userData[1]))
                bankingOperation()


    print('Invalid account or password')
    login()




def accountNumberGen():
    return random.randrange(1111111111,9999999999)

def bankingOperation():
    print(" what transaction would you like to perform?\n")
    print("1. withdraw\n","2.deposit\n","3. complaint\n","4.Balance\n","5.logout")
    choice = int(input("select your choice from the above:\n"))
    if choice == 1:
        print("SELECT AMOUNT YOU WISH TO WITHDRAW\n","1. 1000\n","2.5000\n","3.10,000\n")
        value = int(input("press button that correspond to your choice\n:"))
        if value == 1:
            print("take your 1000")
        elif value == 2:
            print("take your 5000")
        else:
            print("#10,000 withdraw")
    elif choice == 2:
        print("SELECT AMOUNT YOU WISH TO DEPOSIT\n","1.# 1000\n","2.#5000\n","3.#10,000\n")
        credit = int(input("press button that correspond to your choice\n:"))
        if credit == 1:
            print("you deposit 1000")
        elif credit == 2:
            print("you deposit 5000")
        else:
            print("you deposit 20000\n")

    elif choice == 3:
        complain = input("logged your compaint here and get response in 30 mins:\n\n")
        print("thanks for contacting us at Zuri we will get back to you, kindly check your zuriboard for response\n")
    elif choice == 5:
        logout()

    else:
        print("zero account go hustle bro ,money no dey grow from three")


def logout():
    print("you have been logout kindly login to perform another banking operation")
    return login()


# initialization of bank app

init()
