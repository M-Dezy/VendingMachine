# Vending Machine Simulation

This Python project simulates a **Vending Machine** system that allows users to manage inventory, insert money, purchase items, and track sales. The project demonstrates object-oriented programming (OOP) principles, such as encapsulation and modularity, for handling real-time operations like balance updates, inventory tracking, and purchase history.

## Features

- Add items to the inventory with specified price and quantity
- List available items in the vending machine
- Insert money (supports $1, $2, and $5 denominations)
- Purchase items if enough balance is available
- Output remaining balance and give change
- Remove items from the vending machine
- View recent purchase history and total sales
- Clear the inventory

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vending-machine.git
2. Navigate to the project directory:
   ```bash
   cd vending-machine
3. Run the program:
   ```bash
   python vending_machine.py
4. Use the methods in the VendingMachine class to manage items, make purchases, and track sales.


## Example Usage
   ```bash
      vm = VendingMachine()
      vm.add_item("Soda", 1.50, 5)
      vm.insert_money(5.00)
      vm.purchase("Soda")
      vm.list_items()
