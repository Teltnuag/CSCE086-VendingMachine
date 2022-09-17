from sys import exit

class VendingMachine:
    def __init__(self):
        self.balance = 0.
        self.history = {}
        self.inventory = {}

    # An item to be bought or added
    class Item:
        id = 0
        def __init__(self, name):
            self.id = VendingMachine.Item.id
            VendingMachine.Item.id = VendingMachine.Item.id + 1
            self.name = name
            self.quantity = 0
            self.price = 0.0

        def __str__(self):
            return "ID: " + str(self.id) + "\tName:  " + str(self.name) + "\tQuantity: " + str(self.quantity) + "\tPrice: " + "${:,.2f}".format(self.price)

        def getPrice(self):
            return "${:,.2f}".format(self.price)

    # Show the balance
    def getBalance(self):
        print("Current balance:", "${:,.2f}".format(self.balance))
        return

    # Prints list of transcations
    def getHistory(self):
        print("Transaction history:")
        for number, command in self.history.items():
            print(str(number) + ". " + command)
        return

    # Prints available items with name and ID
    def getInventory(self):
        if len(self.inventory) == 0:
            print("No items currently available.")
            return
        print("Available inventory:")
        for item in self.inventory.values():
            print(str(item))
        return

    # Add an item: name, quantity, price
    def add_item(self, name, quantity, price):
        if name not in self.inventory:
            self.inventory[name] = self.Item(name)
        self.inventory[name].quantity += quantity
        self.inventory[name].price = price
        print("Item successfully added/updated:", str(self.inventory[name]))
        return

    # Buys an item with available balance. It also shows change given and the remaining
    # balance with currency distribution. For change, the machine
    # uses the largest denominator of curenncy that is available.
    def buy_item(self, name):
        if name not in self.inventory:
            print("Item \"" + name + "\" not in inventory.")
        else:
            item = self.inventory[name]
            if item.quantity < 1:
                print("Out of stock.")
            elif item.price > self.balance:
                print("Not enough money inserted.\nPrice of \"" + name + "\" is " + item.getPrice())
            else:
                self.balance -= item.price
                item.quantity -= 1
                # dispense the item
                print("Enjoy your " + name + "!")
        self.getBalance()
        if self.balance > 0:
            print("Enter \"change\" to dispense change or buy another item.")
        return

    # Displays help menu with these commands.
    def help(self):
        print("""Available commands:
        help - Display this text.
        balance - Show your balance.
        change - Receive your change.
        inventory - Show the iventory of items available.
        add item - Add items to the machine. Price will be updated for any current items.
            usage: add item itemName quantity price
            e.g. add item chips 2 $1.00
        buy item - Buy a single item from the machine.
            usage: buy item itemName dollars quarters dimes nickels pennies
            e.g. buy item chips 1 2 2 4 3
        history - Show the history of commands accepted.
        exit - Exit this interface and send the machine to the void.""")
        return

    # Calculate the correct change and return to user
    def getChange(self):
        if self.balance == 0.:
            print("No change to return.")
        else:
            dollars = int(self.balance/1)
            self.balance -= dollars
            quarters = int(self.balance/.25)
            self.balance -= quarters*.25
            dimes = int(self.balance/.1)
            self.balance -= dimes*.1
            nickels = int(self.balance/.05)
            self.balance -= nickels*.05
            pennies = int(self.balance/.01)
            self.balance = 0.
            print("Returning change to user:")
            if dollars > 0:
                print(str(dollars) + " dollars")
            if quarters > 0:
                print(str(quarters) + " quarters" )
            if dimes > 0:
                print(str(dimes) + " dimes")
            if nickels > 0:
                print(str(nickels) + " nickels")
            if pennies > 0:
                print(str(pennies) + " pennies")
        return

    # Calculate how much money was given by user
    def countMoney(self, dollars=0, quarters=0, dimes=0, nickels=0, pennies=0):
        return dollars + quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01

    def handleCommand(self, command):
        tokens = command.split()
        tokenLength = len(tokens)
        if tokenLength == 0:
            return
        else:
            command = tokens[0]
            if command == "exit":
                exit()
            elif command == "history":
                self.getHistory()
            elif command == "balance":
                self.getBalance()
            elif command == "change":
                self.getChange()
            elif command == "inventory":
                self.getInventory()
            elif command == "help":
                self.help()
            elif tokenLength > 1 and tokens[1] == "item":
                if tokens[0] == "add":
                    try:
                        assert tokenLength == 5
                        name = tokens[2]
                        quantity = int(tokens[3])
                        price = float(tokens[4].replace('$',''))
                        assert quantity > 0
                        assert price >= 0
                    except:
                        print("Poorly formatted add item. Usage is:\n\tadd item itemName quantity price\n\te.g. add item chips 2 $1.00")
                        return False
                    self.add_item(name, quantity, price)
                elif tokens[0] == "buy":
                    try:
                        assert tokenLength == 8
                        name = tokens[2]
                        dollars = int(tokens[3])
                        quarters = int(tokens[4])
                        dimes = int(tokens[5])
                        nickels = int(tokens[6])
                        pennies = int(tokens[7])
                        assert dollars >= 0
                        assert quarters >= 0
                        assert dimes >= 0
                        assert nickels >= 0
                        assert pennies >= 0
                    except:
                        print("Poorly formatted buy item. Usage is:\n\tbuy item itemName dollars quarters dimes nickels pennies\n\te.g. buy item chips 1 2 2 4 3")
                        return False
                    self.balance += self.countMoney(dollars, quarters, dimes, nickels, pennies)
                    self.buy_item(name)
            else:
                print("Unknown command. Enter \"help\" for a list of commands.")
                return False
        return True

    # Main command function
    def main(self):
        print("Super Vending Machine Activated")
        validCommands = 0
        while True:
            command = input("> ").lower()
            if self.handleCommand(command):
                validCommands = validCommands + 1
                self.history[validCommands] = command

if __name__ == "__main__":
    vm = VendingMachine()
    vm.main()
