# Banking System consisting of :
# 1. Registration system [first_name, last_name, email, password, balance] 
# 2. Login 
# 3. Generate account number 
# 4. Banking Operation 

database = {}

import random 

#--------> initialize the system 
def init():
    print('=' * 30)
    print('Welcome to Bank Py')
    print('Do you have an account with us \n Do you have an account with us \n (1) Yes (2) No ')
    
    init_opt = int(input(' Select an option >> '))

    if init_opt == 1:
        login()

    elif init_opt == 2:
        registration()

    else:
        print('Invalid option selected \n Try again')
        init()
        


#--------> Registration set up 
def registration():
    print('********** REGISTRATION **********')
    print('Please fill in your details ')
    
    first_name = input('What is your first name ? \n')
    last_name = input('What is your last name ? \n')
    email_address = input('E-mail address ? \n')
    password = input('Input password ? \n')
    balance = int('0')

    account_number = generate_acct_no()

    database[account_number] = [first_name, last_name, email_address, password, balance]

    print(database)

    login()



#--------> Generate Account number
def generate_acct_no():
    return random.randrange(1111111111, 9999999999)

generate_acct_no()



#--------> Login to system
def login():
    print('********** LOGIN **********')

    auth_email = input('Input email address \n >>')
    auth_password = input('Input password \n >>')

    for key, value in database.items():
        if auth_email == value[2]:
            if auth_password == value[3]:

                bank_operation()

            else:
                print('Wrong password. Try again')
                continue_transaction()

        
        else:
            print('Try again. Invalid email address')
            continue_transaction()



#---------> Bank operation
def bank_operation():
    for key, value in database.items():
    
        print(f'Welcome to Bank El {value[0]}  " " {value[1]}')
        print('Select an option \n (1) Withdrawl \n (2) Deposit \n (3) Complains')

        bank_opt = int(input('Select an option \n >> '))

        if bank_opt == 1:
        
            withdrwal()


        elif bank_opt == 2:
            
            deposit()

        elif bank_opt == 3: 
            
            complains()



# --------> Withdrawl operation
def withdrwal():
    print('********** WITHDRAWL **********')
    for key, value in database.items():

        user_balance = value[4]

        withdrawl_amoumt = int(input('amount to withdrawl \n >> '))

        if withdrawl_amoumt > user_balance:
            print('Insufficient Balance')
            continue_transaction()
            

        elif withdrawl_amoumt < 500:
            print('withdrawl must be atleast #500')
            continue_transaction()
            

        else:
            user_balance -= withdrawl_amoumt

            print(f'Your balance is #{user_balance}')
            
            transaction()
            


# ---------> Deposit operation
def deposit():
    print('********** DEPOSIT **********')
    for key, value in database.items():

        user_balance = value[4]
        deposit_amount = int(input('amount to deposit \n >> '))

        user_balance += deposit_amount
        print(f'Your balance is #{user_balance}')
        transaction()



# --------> Complains operation
def complains():
    print('Ww are sorry for any issue caused')

    user_complain = input('State your complain \n >> ')
    print('Contact our customer service on 0700-0000-000')
    continue_transaction()



#---------> Transaction success
def transaction():
    print('Transaction successful \n Thank you for Banking with us')
    print('Contact our customer service on 0700-0000-000')
    continue_transaction()



# --------> Does user want to perform another task
def continue_transaction():
    cont_trans = int(input('Do you want to perform another task \n (1) Yes \n (2) No \n >> '))

    if cont_trans == 1: 
        login()

    elif cont_trans == 2 :
        exit 


    
init()