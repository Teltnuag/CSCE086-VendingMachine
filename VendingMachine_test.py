import unittest
from unittest.mock import patch, call
import VendingMachine

class VendingMachineTest(unittest.TestCase):
    @patch("VendingMachine.print")
    @patch("VendingMachine.input")
    def testSuite(self, mockInput, mockOutput):
        commands = [
            ("hello", [call("""Unknown command. Enter "help" for a list of commands.""")]),
            ("help", [call("""Available commands:\n        help - Display this text.\n        balance - Show your balance.\n        change - Receive your change.\n        inventory - Show the iventory of items available.\n        add item - Add items to the machine. Price will be updated for any current items.\n            usage: add item itemName quantity price\n            e.g. add item chips 2 $1.00\n        buy item - Buy a single item from the machine.\n            usage: buy item itemName dollars quarters dimes nickels pennies\n            e.g. buy item chips 1 2 2 4 3\n        history - Show the history of commands accepted.\n        exit - Exit this interface and send the machine to the void.""")]),
            ("balance", [call("""Current balance:""", """$0.00""")]),
            ("change", [call("""No change to return.""")]),
            ("inventory", [call("""No items currently available.""")]),
            ("add item chips two 1.25", [call("""Poorly formatted add item. Usage is:\n\tadd item itemName quantity price\n\te.g. add item chips 2 $1.00""")]),
            ("add item chips 2 $1.25", [call("""Item successfully added/updated:""", """ID: 0\tName:  chips\tQuantity: 2\tPrice: $1.25""")]),
            ("add item coke 3 .75", [call("""Item successfully added/updated:""", """ID: 1\tName:  coke\tQuantity: 3\tPrice: $0.75""")]),
            ("add item snickers 8 .65", [call("""Item successfully added/updated:""", """ID: 2\tName:  snickers\tQuantity: 8\tPrice: $0.65""")]),
            ("inventory", [call("""Available inventory:"""), call("""ID: 0\tName:  chips\tQuantity: 2\tPrice: $1.25"""), call("""ID: 1\tName:  coke\tQuantity: 3\tPrice: $0.75"""), call("""ID: 2\tName:  snickers\tQuantity: 8\tPrice: $0.65""")]),
            ("buy item chips", [call("""Poorly formatted buy item. Usage is:\n\tbuy item itemName dollars quarters dimes nickels pennies\n\te.g. buy item chips 1 2 2 4 3""")]),
            ("buy item chip 1 2 2 4 3", [call("""Item "chip" not in inventory."""), call("""Current balance:""", """$1.93"""), call("""Enter "change" to dispense change or buy another item.""")]),
            ("buy item chips 0 0 0 0 0", [call("""Enjoy your chips!"""), call("""Current balance:""", """$0.68"""), call("""Enter "change" to dispense change or buy another item.""")]),
            ("buy item chips 0 0 0 0 0", [call("""Not enough money inserted.\nPrice of "chips" is $1.25"""), call("""Current balance:""", """$0.68"""), call("""Enter "change" to dispense change or buy another item.""")]),
            ("buy item chips 1 0 0 0 0", [call("""Enjoy your chips!"""), call("""Current balance:""", """$0.43"""), call("""Enter "change" to dispense change or buy another item.""")]),
            ("buy item chips 0 0 0 0 0", [call("""Out of stock."""), call("""Current balance:""", """$0.43"""), call("""Enter "change" to dispense change or buy another item.""")]),
            ("change", [call("""Returning change to user:"""), call("""1 quarters"""), call("""1 dimes"""), call("""1 nickels"""), call("""2 pennies""")]),
            ("history", [call("""Transaction history:"""), call("""1. help"""), call("""2. balance"""), call("""3. change"""), call("""4. inventory"""), call("""5. add item chips 2 $1.25"""), call("""6. add item coke 3 .75"""), call("""7. add item snickers 8 .65"""), call("""8. inventory"""), call("""9. buy item chip 1 2 2 4 3"""), call("""10. buy item chips 0 0 0 0 0"""), call("""11. buy item chips 0 0 0 0 0"""), call("""12. buy item chips 1 0 0 0 0"""), call("""13. buy item chips 0 0 0 0 0"""), call("""14. change""")]),
            (Exception("Break Loop"), None)
        ]
        mockInput.side_effect = [command[0] for command in commands]
        
        vm = VendingMachine.VendingMachine()
        with self.assertRaises(Exception):
            vm.main()
        mockOutput.mock_calls.pop(0) # pop welcome message
        for i in range(len(commands)-1):
            for expectedOutput in commands[i][1]:
                receivedOutput = mockOutput.mock_calls.pop(0)
                assert expectedOutput == receivedOutput, "Input:\n" + commands[i][0] + "\n\nExpected:\n" + str(expectedOutput) + "\n\nReceived:\n" + str(receivedOutput)