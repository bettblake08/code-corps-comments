from app.sign_up import sign_up
from app.auth import log_in, log_out

def run_main():
    print(""" 
    Code Corps Comment App
    --------------------------------------------

    1. Sign up
    2. Login
    3. Quit
    
    """)

    choice = raw_input("Select option : ")

    if choice == '1':
        sign_up()
        run_main()
    elif choice == '2':
        if log_in():
            run_comment_menu()
        else:
            run_main()
    elif choice == '3':
        return
    else:
        print('Invalid option. Please try again ! ')
        run_main()


def run_comment_menu():
    print(""" 
    Comment Menu
    ---------------------------------------------
    1. Create comment
    2. Edit comment
    3. Delete comment
    4. Reply to comment
    5. Edit reply
    6. Delete reply
    7. Log out

    """)

    choice = raw_input('Select option :')

    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        log_out()


run_main()