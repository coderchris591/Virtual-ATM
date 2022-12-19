
import os

class Client:
    def __init__(self, first_name, last_name, balance, pin):
        # assign values
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.pin = pin

    def checkUser(self):
        new_user = True
        with open('client_data.txt', 'r') as file:
            filesize = os.path.getsize('client_data.txt')
            if filesize == 0:
                return new_user
            for line in file:
                split_data = line.split()
                # print(split_data)
                # print(self.pin)
                if self.pin == int(split_data[2]):
                    new_user = False
            print(new_user)
        return new_user

    def appendData(self):
        # open or create txt file
        with open('client_data.txt', 'a') as file:
            # write data to file
            file.write(f'{self.first_name} {self.last_name} {self.pin}\n')
        return

    def display_balance(self):
        currency_format = "{:,.2f}"
        print(f"\nAccount Summary\nName: {self.first_name.title()} {self.last_name.title()}\n"
              f"Balance: ${currency_format.format(self.balance)}")
        return

print("\nClient Information")

fn = input("\nWhat is your first name? ")
ln = input("Last name? ")
pin = int(input("PIN: "))
balance = 100.00


client = Client(fn, ln, balance, pin)
new_user = client.checkUser()
if new_user:
    client.appendData()
client.display_balance()



