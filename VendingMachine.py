balance = 0
history = {}
inventory = {}

# Show the balance
def balance():

    return

# Prints list of transcations
def history():

    return

# Prints available items with name and ID
def inventory():

    return

# Add an item: name, quantity, price
def add_item(name, quantity, price):

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
    help - display this text
    balance - show your balance
    inventory - show iventory of items available
    add item - add items to machine
        usage: add item itemName quantity price
        e.g. add item chips 2 $1.00
    buy item - buy items
        usage: buy item itemName dollars quarters dimes nickels pennies
        e.g. buy item chips 1 2 2 4 3
    history - show history of transactions
    exit - exit this interface
    """)
    return

# Exit the vending machine.
def exit():

    return

# Calculate the correct change to return to user
def getChange(cost, paid):

    return

# Calculate how much money was given by user
def countMoney(dollars=0, quarters=0, dimes=0, nickels=0, pennies=0):
    return dollars + quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01

# Parse user input to direct program
def parseInput(command):

    return

# Main command function
def main():
    print("Super Vending Machine Activated")
    return

if __name__ == "__main__":
    main()