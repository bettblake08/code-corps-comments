from db import users

def log_in():
    """Login"""
    print('*******************************Login*******************************')
    #get data from data structure

    username = raw_input('Enter your name: ')
    password = raw_input('Enter your password: ')
    #check in dict for user
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                #update status to True
                user['status'] = True

                #get user details
                id = user['id']
                username = user['username']
                role = user['role']
                status = user['status']
                user = [id, username, role, status]
                message = 'You are successfully logged in'
                return True
            else:
                message = "Ooops! Wrong Password"

            break
        else:
            message = "Ooops! No user with that Name"

    print(message)
    print('*******************************************************************')

def log_out():
    """Logout"""
    #check in dict for user
    for user in users:
        if user['id'] == id:
            #update status to False
            user['status'] = False
            print("You are successfully logout")
            return True