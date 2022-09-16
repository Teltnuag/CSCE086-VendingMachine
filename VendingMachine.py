from sys import exit

balance = 0.
history = {}
inventory = {}

# An item to be bought or added
class Item:
    id = 0
    def __init__(self, name):
        self.id = Item.id
        Item.id = Item.id + 1
        self.name = name
        self.quantity = 0
        self.price = 0.0

    def __str__(self):
        return "ID: " + str(self.id) + "\tName:  " + str(self.name) + "\tQuantity: " + str(self.quantity) + "\tPrice: " + "${:,.2f}".format(self.price)

# Show the balance
def getBalance():
    print("Current balance:", balance)
    return

# Prints list of transcations
def getHistory():
    print("Transaction history:")
    for number, command in history.items():
        print(str(number) + ". " + command)
    return

# Prints available items with name and ID
def getInventory():
    print("Available inventory:")
    for item in inventory.values():
        print(item)
    return

# Add an item: name, quantity, price
def add_item(name, quantity, price):
    if name not in inventory:
        inventory[name] = Item(name)
    inventory[name].quantity += quantity
    inventory[name].price = price
    print("Item successfully added/updated:", inventory[name])
    return

# Buys an item with # dollars, quarters, dimes, nickles,
# pennies. It also shows change given and the remaining
# balance with currency distribution. For change, the machine
# uses the largest denominator of curenncy that is available.
def buy_item(name, dollars, quarters, dimes, nickles, pennies):

    return

# Displays help menu with these commands.
def help():
    print("""Available commands:
    help - Display this text.
    balance - Show your balance.
    inventory - Show the iventory of items available.
    add item - Add items to the machine. Price will be updated for any current items.
        usage: add item itemName quantity price
        e.g. add item chips 2 $1.00
    buy item - Buy a single item from the machine.
        usage: buy item itemName dollars quarters dimes nickels pennies
        e.g. buy item chips 1 2 2 4 3
    history - Show the history of commands accepted.
    exit - Exit this interface and send the machine to the void.
    """)
    return

# Calculate the correct change to return to user
def getChange(cost, paid):

    return

# Calculate how much money was given by user
def countMoney(dollars=0, quarters=0, dimes=0, nickels=0, pennies=0):
    return dollars + quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01

# Parse user input to direct program
def parseInput(command):
    tokens = command.split()

    return command

# Main command function
if __name__ == "__main__":
    print("Super Vending Machine Activated")
    validCommands = 0
    while True:
        validCommand = True
        command = parseInput(input("> ").lower())
        tokens = command.split()
        tokenLength = len(tokens)
        if tokenLength == 0:
            continue
        elif tokenLength == 1:
            command = tokens[0]
            if command == "exit":
                exit()
            elif command == "history":
                getHistory()
            elif command == "balance":
                getBalance()
            elif command == "inventory":
                getInventory()
            elif command == "help":
                help()
            else:
                validCommand = False
                print("Unknown command. Enter \"help\" for a list of commands.")
                continue
        elif tokens[0] == "add" and tokens[1] == "item":
            try:
                assert tokenLength == 5
                name = tokens[2]
                quantity = int(tokens[3])
                price = float(tokens[4].replace('$',''))
                assert quantity > 0
                assert price >= 0
            except:
                validCommand = False
                print("Poorly formatted add item. Usage is:\n\tadd item itemName quantity price\n\te.g. add item chips 2 $1.00")
                continue
            add_item(name, quantity, price)
        validCommands = validCommands + 1
        history[validCommands] = command
