import re
from db import users

def sign_up():
    print("Please input your details:")
    
    name = enter_name()
    password = enter_password()
    roleId = enter_role()

    users.append({
        "id":len(users) + 1,
        "username":name,
        "password":password,
        "role":roleId,
        'status':False,
        "lastLoggedIn":None
    })

    print("Sign up succeeded!")
    print(users)

def enter_name():
    name = raw_input("What is your name?")

    if name == "":
        print("Invalid username. Please re-enter details")
        enter_name()

    return name

def enter_password():
    password = raw_input(
        "What is your password? Password should include 1 uppercase,1 lowercase, 1 digit and 1 special character [@$#.]")

    if password == "" or not test_password(password):
        print("Invalid password")
        enter_password()

    return password

def test_password(password):
    """ This function tests the validity of the password by running it through a regex expression.
    Args:
        -   password (string)
    Returns:
        bool:   Return True if password passes, False if password fails or reg_type is invalid
    """

    pattern = re.compile(
            r"((?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@\$#.]).{8,16})"
        )

    return bool(pattern.match(password, 0))

def enter_role():
    role = raw_input("What is your role?")

    roleId = 0

    if role == "user":
        roleId = 1
    elif role == "moderator":
        roleId = 2
    elif role == "admin":
        roleId = 3
    else :
        print('Invalid role id! Please re-enter details')
        enter_role()

    return roleId

sign_up()