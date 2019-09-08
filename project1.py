client_list = []

pen1_price = 95
pen2_price = 105
pen3_price = 120

class client:
    username = ''
    password = ''
    pen1 = 0
    pen2 = 0
    pen3 = 0
    exempt = False

    def __init__(self, usr, passw):
        self.username = usr
        self.password = passw

    def print_invoice(self):
        global pen1_price
        global pen2_price
        global pen3_price
        total = (self.pen1 * pen1_price) + (self.pen2 * pen2_price) + (self.pen3 * pen3_price)
        print(f'User: {self.getuser()}\n'
              f'# of Mechanical Pens: {self.pen1}\n'
              f'# of Mechanical Pens With Inscriptions: {self.pen2}\n'
              f'# of Wingback X Lei Melendres Pens: {self.pen3}\n'
              f'Total Cost: {total}')

    def getuser(self):
        return self.username

    def getpass(self):
        return self.password

    def addpen1(self, quan):
        self.pen1 = self.pen1 + quan

    def addpen2(self, quan):
        self.pen2 = self.pen2 + quan

    def addpen3(self, quan):
        self.pen3 = self.pen3 + quan


def main():
    global pen1_price
    global pen2_price
    global pen3_price
    while True:
        account = input (
            'Welcome! If you have an existing account press Y and then enter. \nIf not press N and then enter. Press Q then enter to quit')
        if account.lower () == 'n':
            username = input ('create Username:')
            password = input ('create Password:')
            c = client (username, password)
            client_list.append (c)
        elif account.lower () == 'q':
            break
        print ('You may login now.')
        username = input ('Username:')
        password = input ('Password:')
        x = 0
        for i in range (len (client_list)):
            cli = client_list[i]
            if cli.getuser () == username:
                if cli.getpass () == password:
                    print ("Login Successful!")
                    x = 1
                    break
            elif i == len (client_list) & (cli.getpass () != password or cli.getuser () != username):
                x = 0
        if x == 1:
            print (f"Welcome {cli.getuser ()}")
            go = True
            while go:
                pen = input("Order a Pen: Mechanical (M), Mechanical with Inscription (MI), or Wingback X Lei Melendres (W). "
                            "\nPress I for an invoice or L to logout")
                if pen.lower() == "m" or pen.lower() == 'mi' or pen.lower() == 'w':
                    quan = input("How many would you like?")
                    if pen.lower() == "m":
                        cli.addpen1(int(quan))
                    if pen.lower() == "mi":
                        cli.addpen2(int(quan))
                    if pen.lower() == "w":
                        cli.addpen3(int(quan))
                elif pen.lower() == 'i':
                    cli.print_invoice()
                elif pen.lower() == 'l':
                    break
                else:
                    print("Invalid Input")

        else:
            print ("Login Incorrect!")

main()
