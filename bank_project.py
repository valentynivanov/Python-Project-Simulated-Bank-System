# Initialise dictionary to include users with details of 'name', 'balance', and unique 'user ID'
users = {}

######################################################################

''' Prompts the user to introduce their details'''
def create_account():
    print("=== CREATE AN ACCOUNT ===\n")
    user_ID = input("Please choose a unique user ID: ")
    # Check the user_ID is not already taken, ask the user until a unique one is chosen
    while user_ID in users:
        user_ID = input("That user ID is taken, please choose a different user ID: ")
    name = input("Name: ")
    while True:
        try:
            balance = float(input("Current balance: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the balance.")

    # Stores information in a dictionary within a dictionary
    users[user_ID] = {'name': name, 'balance': balance, 'transactions': []}
    print(f"\nYou have successfully created an account, {users[user_ID]['name']}.")
    return user_ID

######################################################################

''' Gets user details to check if is already in the system, otherwise prompts to create an account'''
def login():
    print("\n=== LOG IN ===")
    current_user = input("\nPlease enter your user ID: ")
    #  Checks user ID input is in the dictionary already to login
    if current_user in users:
        print(f"\nWelcome to your account, {users[current_user]['name']}.")
        # Return current_user so it can be used in other functions
        return current_user
    # Otherwise prompts to create an account
    else:
        print("\nYou are not a user, please create an account.\n")
        return create_account()

######################################################################

''' Transaction menu to handle deposit, withdrawals, balance check, and transaction history'''
def transaction(current_user):
    while True:
        print("\n=== TRANSACTION MENU ===")
        transaction_choice = input("What transaction would you like to perform? \n1) Deposit\n2) Withdraw\n3) Check Balance\n4) Transaction History\n5) Exit to Main Menu\n")
        if transaction_choice == '1':
            try:
                amount = float(input("Deposit amount: £"))
                users[current_user]['balance'] += amount
                print(f'Deposit was successful.\nNew balance: £{users[current_user]["balance"]:.2f}')
                users[current_user]['transactions'].append(f"Deposited: £{amount:.2f}")
            except ValueError:
                print("Invalid input. Please enter a numerical value for the deposit amount.")
        elif transaction_choice == '2':
            try:
                amount = float(input("Withdrawal amount: £"))
                if amount > users[current_user]['balance']:
                    print("Insufficient balance.")
                else:
                    users[current_user]['balance'] -= amount
                    print(f'Withdrawal was successful.\nNew balance: £{users[current_user]["balance"]:.2f}')
                    users[current_user]['transactions'].append(f"Withdrew: £{amount:.2f}")
            except ValueError:
                print("Invalid input. Please enter a numerical value for the withdrawal amount.")
        elif transaction_choice == '3':
            print(f"Current balance: £{users[current_user]['balance']:.2f}")
        elif transaction_choice == '4':
            show_transactions(current_user)
        elif transaction_choice == '5':
            print("Returning to the main menu...")
            return
        else:
            print("Please choose a valid option.")

######################################################################

''' Function to show all transactions'''
def show_transactions(current_user):
    print("\n=== TRANSACTION HISTORY ===")
    print(f"User: {users[current_user]['name']}")
    print(f"Current balance: £{users[current_user]['balance']:.2f}")
    print("\nLATEST TRANSACTIONS:\n")
    for transaction in users[current_user]['transactions']:
        print(transaction)

######################################################################

# MAIN MENU
menu = True
while menu:
        print("\n=== ONLINE BANKING ===\n")
        print("Select an option: \n1) Login\n2) Create an account\n3) Exit\n")
        menu_option = input()
        if menu_option == '1':
            # user gets the value of current_user (return) after calling function login()
            user = login()
            transaction(user)
        elif menu_option == '2':
            create_account()
        elif menu_option == '3':
            print("Thank you for using our banking app. Goodbye!")
            break
        else:
            print("\nPlease choose a valid option.")
