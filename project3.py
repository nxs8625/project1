import getpass

class client:
    model1 = 0
    model2 = 0
    model3 = 0

    def __init__(self, usr, passw):
        self.username = usr
        self.password = passw

    def print_invoice(self):
        
        global model1_price
        global model2_price
        global model3_price

        total = (self.model1 * model1_price) + (self.model2 * model2_price) + (self.model3 * model3_price)
        print(f'User: {self.getuser()}\n'
            f'# of Model 3: {self.model1}\n'
            f'# of Model S: {self.model2}\n'
            f'# of Model X: {self.model3}\n'
            f'Total Cost: {total}')
    
    def getuser(self):
        return self.username

    def getpass(self):
        return self.password
    
    def addmodel1(self, quan):
        self.model1 = self.model1 + quan

    def addmodel2(self, quan):
        self.model2 = self.model2 + quan

    def addmodel3(self, quan):
        self.model3 = self.model3 + quan

    def addinventory(self):
        Model().stock += '%d'

    def removeinventory(self):
        Model().stock += '%d'


client_list = [client("",""), client("","")]

model1_price = 35000
model2_price = 75000
model3_price = 81000

class Accounts:
    def create(self):
        print("Please enter these fields...")
        username = input("Username: ")
        password = ""
        while True:
            password = getpass.getpass("Password: ")
            _password = getpass.getpass("Password (again): ")

            print()

            if password != _password:
                print("Please enter matching passwords.\n")
            else:
                break

        print("Account created succesfully!\nYou may now login.\n")
        acc = client(username, password)
        client_list.append(acc)

    def isValidAccount(self, acc):
        return any(
            acc.getuser() == account.getuser() and acc.getpass() == account.getpass()
            for account in client_list
        )

    def login(self):
        print("Enter your credentials...")
        while True:
            username = input("Username: ")
            password = getpass.getpass("Password: ")

            acc = client(username, password)

            print()

            if self.isValidAccount(acc):
                print("Login successful!\n")
                print(f"Welcome {username}!")
                return acc
            else:
                print(
                    "Login error: Incorrect username/password.\n\nPlease try again..."
                )

def main():

    print("Welcome!\n")

    curr_user = ""

    while True:
        option = input("Please select an option:\n[1] Login\n[2] Create an account\n> ")
        print()
        if option == "1":
            curr_user = Accounts().login()
            break
        if option == "2":
            Accounts().create()
            curr_user = Accounts().login()
            break
        else:
            print(f"Invalid option: {option}\nTry again...\n")
           
    while True:
        model = input(
            "Pick a Model: Model 3 (M3), Model S (MS), or Model X (MX). "
            "\nPress A to add items back, R to remove items, I for Invoice or L to Logout: "
        )
        print()
        if model.lower() == "m3" or model.lower() == "ms" or model.lower() == "mx":
            quan = input("How many would you like? ")
            if model.lower() == "m3":
                curr_user.addmodel1(int(quan))
            if model.lower() == "ms":
                curr_user.addmodel2(int(quan))
            if model.lower() == "mx":
                curr_user.addmodel3(int(quan))
        elif model.lower() == 'a' or model.upper()== 'A':
            Type = input('Which model would you like to add back to the inventory? ')
            if Type == 'm3':
                curr_user.addinventory('M3')
            if Type == 'ms':
                curr_user.addinventory('MS')
            if Type == 'mx':
                curr_user.addinventory('MX')
        elif model.lower() == 'r' or model.upper() == 'A':
            Type = input('Which model would you like to remove from the inventory? ')
            if Type == 'm3':
                curr_user.removeinventory('M3')   
            if Type == 'ms':
                curr_user.removeinventory('MS')   
            if Type == 'mx':
                curr_user.removeinventory('MX')   
        elif model.lower() == "i":
            curr_user.print_invoice()
        elif model.lower() == "l":
            break
        else:
            print("Invalid Input")

        print()

main()

class Model:
    def __init__(self, name, color, stock, price):
        self.name = name
        self.color = color
        self.stock = stock
        self.price = price

    # Car string format: "%Color %Name x%Stock"for %Price
    def __repr__(self):
        stock = "%-3d" % (self.stock)
        return f"{self.color} {self.name} x{stock} for {self.price}"


class Warehouse:
    def __init__(self):
        self.models = [
            Model("Model 3", "Black", 69, "35k"),
            Model("Model S", "Black", 420, "75k"),
            Model("Model X", "Black", 911, "81k"),
        ]

    def __repr__(self):
        return "\n".join(map(str, self.models))
    def addinventory(self):
        Model().stock + 1
        return str('Added Sucessfully!')
    def removeinventory(self):
        Model().stock - 1
        return str('Removed Successfully!')

print(Warehouse())

