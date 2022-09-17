# CSCE086-VendingMachine
TSgt Mason Wright
First assignment for AFIT CSCE-086 refresher course.
Should run in nearly any build of Python 3 requiring no additional libraries.
Optional test suite requires unittest.

Sample input/output:
hello                       ->  Unknown command. Enter "help" for a list of commands.
help                        ->  Available commands:
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
                                exit - Exit this interface and send the machine to the void.
balance                     ->  Current balance: $0.00
change                      ->  No change to return.
inventory                   ->  No items currently available.
add item chips two 1.25     ->  Poorly formatted add item. Usage is:
                                    add item itemName quantity price
                                    e.g. add item chips 2 $1.00
add item chips 2 $1.25      ->  Item successfully added/updated: ID: 0  Name:  chips    Quantity: 2     Price: $1.25
add item coke 3 .75         ->  Item successfully added/updated: ID: 1  Name:  coke     Quantity: 3     Price: $0.75
add item snickers 8 .65     ->  Item successfully added/updated: ID: 2  Name:  snickers Quantity: 8     Price: $0.65
inventory                   ->  Available inventory:
                                ID: 0   Name:  chips    Quantity: 2     Price: $1.25
                                ID: 1   Name:  coke     Quantity: 3     Price: $0.75
                                ID: 2   Name:  snickers Quantity: 8     Price: $0.65
buy item chips              ->  Poorly formatted buy item. Usage is:
                                    buy item itemName dollars quarters dimes nickels pennies
                                    e.g. buy item chips 1 2 2 4 3
buy item chip 1 2 2 4 3     ->  Item "chip" not in inventory.
                                Current balance: $1.93
                                Enter "change" to dispense change or buy another item.
buy item chips 0 0 0 0 0    ->  Enjoy your chips!
                                Current balance: $0.68
                                Enter "change" to dispense change or buy another item.
buy item chips 0 0 0 0 0    ->  Not enough money inserted.
                                Price of "chips" is $1.25
                                Current balance: $0.68
                                Enter "change" to dispense change or buy another item.
buy item chips 1 0 0 0 0    ->  buy item chips 1 0 0 0 0
                                Enjoy your chips!
                                Current balance: $0.43
                                Enter "change" to dispense change or buy another item.
buy item chips 0 0 0 0 0    ->  Out of stock.
                                Current balance: $0.43
                                Enter "change" to dispense change or buy another item.
change                      ->  Returning change to user:
                                1 quarters
                                1 dimes
                                1 nickels
                                2 pennies
history                     ->  Transaction history:
                                1. help
                                2. balance
                                3. change
                                4. inventory
                                5. add item chips 2 $1.25
                                6. add item coke 3 .75
                                7. add item snickers 8 .65
                                8. inventory
                                9. but item chip 1 2 2 4 3
                                10. buy item chip 1 2 2 4 3
                                11. buy item chips 0 0 0 0 0
                                12. buy item chips 0 0 0 0 0
                                13. buy item chips 1 0 0 0 0
                                14. buy item chips 0 0 0 0 0
                                15. change
exit