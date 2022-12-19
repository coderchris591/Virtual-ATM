# Chris Martinez
# CIS 135 Python
# Week 16 HW

# code summary: This App begins by asking the user to enter their first name, last name, and PIN.
# If the user does not already exists in the txt file, a new account will be created with 100 dollars in the account.
# From there, the user has the option to view their account balance, make a deposit,
# make a withdraw, or exit the program.

import client_object

currency_format = "{:,.2f}"


def main():
    # welcome message
    print('\nWelcome to the ATM Application')
    exit_loop = False
    while not exit_loop:
        print('\nPlease select an option:')
        print('\t1) Display Account Balance\n\t2) Make a deposit\n\t3) Make a withdraw\n\t4) Exit the system')
        # get user input (selected option)
        option = input('>> ')
        # prompt user for name, quantity, and value
        if option == '1':
            displayBalance()
        elif option == '2':
            makeDeposit()
        elif option == '3':
            makeWithdraw()
        elif option == '4':
            exit_loop = True
            print("Thank you for using the ATM Application")
    return

def displayBalance():
    print("ACCOUNT BALANCE")
    print(f"The balance for this account is: ${currency_format.format(client_object.balance)}")
    return

def makeDeposit():
    print("\nDEPOSIT")
    while True:
        try:
            deposit_amount = float(input("Please enter the amount you wish to deposit: "))
            break
        except ValueError:
            print("Entry not valid")
    client_object.balance = client_object.balance + deposit_amount
    print(f"New Balance: ${currency_format.format(client_object.balance)}")
    return

def makeWithdraw():
    print("\nWITHDRAW")
    while True:
        try:
            withdraw_amount = float(input("Please enter the amount you wish to withdraw: "))
            if withdraw_amount > client_object.balance:
                print("\nSorry, that amount is larger than your current balance.")
                print(f"Current Balance: ${currency_format.format(client_object.balance)}\n")
            else:
                break
        except ValueError:
            print("Entry not valid")
    client_object.balance = client_object.balance - withdraw_amount
    print(f"New Balance: ${currency_format.format(client_object.balance)}")
    return


main()

