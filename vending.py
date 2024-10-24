# Author: Madhiyougi Jain
# Email: mjjain@umass.edu
# Spire ID: 34310217


class VendingMachine:
    def __init__(self):
        self.inventory = []
        self.framework = {"name":'',"price":0.0,"quantity":0}
        self.balance= 0.0
        self.sales=0.0
        self.purchases=[]
    def add_item(self,name,price,quantity):
        if name not in [x["name"] for x in self.inventory]:
            self.framework["name"]=name
            self.framework["price"]=round(price,2)
            self.framework["quantity"]=quantity
            self.inventory.append(dict(self.framework))
        else:
            for x in range(len(self.inventory)):
                if self.inventory[x]["name"]==name:
                    self.inventory[x]["price"]=price
                    self.inventory[x]["quantity"]+=quantity
        print(f'{quantity} {name}(s) added to inventory')
    def get_item_price(self,name):
        for x in self.inventory:
            if x["name"]==name:
                return x["price"]
            else:
                continue
        print("Invalid item")
        return None
    def get_item_quantity(self,name):
        for x in self.inventory:
            if x["name"]==name:
                return x["quantity"]
            else:
                continue
        print("Invalid item")
        return None
    def list_items(self):
        if not self.inventory:
            print("No items in the vending machine")
            return None
        sortedInv=sorted(self.inventory, key=lambda d:d['name'])
        print('Available items:')
        for x in sortedInv:
            print(f'{x["name"]} (${x["price"]}): {x["quantity"]} available')
    def insert_money(self, insAmt):
        if insAmt==1.0 or insAmt==2.0 or insAmt==5.0:
            self.balance+=insAmt
            self.balance=round(self.balance,2)
            print(f"Balance: {round(self.balance,2)}")
        else:
            print("Invalid amount")
    def purchase(self, name):
        if name not in [x["name"] for x in self.inventory]:
            print("Invalid item")
            return

        for y in self.inventory:
            if y["name"]==name:
                if y["quantity"]==0:
                    print(f"Sorry {name} is out of stock")
                    return
                elif y["price"]>self.balance:
                    priceof=y["price"]
                    print(f"Insufficient balance. Price of {name} is {priceof}")
                    return
                else:
                    self.sales+=y["price"]
                    self.balance=self.balance-y["price"]
                    y["quantity"]=y["quantity"]-1
                    print("Purchased " + y["name"])
                    print("Balance: " + str(self.balance))
                    self.purchases.append(name)
                    self.purchases.append(y["price"])
                    return
    def output_change(self):
        if self.balance>0.0:
            print(f"Change: ${self.balance}")
            self.balance=0.0
        else:
            print("No change")
    def remove_item(self, name):
        if name not in [x["name"] for x in self.inventory]:
            print("Invalid item")
            return
        else:
            self.inventory.remove(next(y for y in self.inventory if y["name"]==name))
            print(name,"removed from inventory")
    def empty_inventory(self):
        for x in range(len(self.inventory)):
            self.inventory.pop(0)
        print("Inventory cleared")
    def get_total_sales(self):
        return round(self.sales,2)
    def stats(self, N):
        if not self.purchases:
            print("No sale history in the vending machine")
            return
        else:
            purchaseNum=N
            maxNum=len(self.purchases)/2
            if N>maxNum:
                purchaseNum=maxNum
            purchaseNum=int(purchaseNum)
            print(f"Sale history for the most recent {purchaseNum} purchase(s):")
            indice=int((len(self.purchases)-purchaseNum*2))
            purchaseList=list(self.purchases[indice:])
            purchaseNames=list(purchaseList[::2])
            purchasePrices=list(purchaseList[1::2])
            printReceipt={}
            sortedNames=[]
            for i in range(len(purchaseNames)):
                if purchaseNames[i] not in printReceipt:
                    printReceipt.update({purchaseNames[i]:{'name':purchaseNames[i],'price':purchasePrices[i],'purchases':1}})
                    sortedNames.append(purchaseNames[i])
                else:
                    newPrice=printReceipt.get(purchaseNames[i]).get('price')+purchasePrices[i]
                    newPurchaseNumber=printReceipt.get(purchaseNames[i]).get('purchases')+1
                    printReceipt.update({purchaseNames[i]:{'name':purchaseNames[i],'price':newPrice,'purchases':newPurchaseNumber}})
            sortedNames=sorted(sortedNames)
            for x in range(len(printReceipt)):
                print(f"{printReceipt.get(sortedNames[x]).get('name')}: ${printReceipt.get(sortedNames[x]).get('price')} for {printReceipt.get(sortedNames[x]).get('purchases')} purchase(s)")


vm = VendingMachine()
vm.add_item("Nkqbz", 6.72, 9)
vm.add_item("Bgurriq", 5.42, 2)
vm.insert_money(5.00)
vm.insert_money(1.00)
vm.purchase("Bgurriq")
vm.insert_money(5.00)
vm.insert_money(2.00)
vm.purchase("Nkqbz")
vm.stats(3)







'''
# Create a new vending machine
vm = VendingMachine()

# Add some items to the inventory
vm.add_item('Soda', 1.50, 5)
vm.add_item('Chips', 0.75, 10)
vm.add_item('Candy', 0.50, 15)

# Show the available items
vm.list_items()

# Insert some coins
vm.insert_money(1.00)
vm.insert_money(1.00)

# Purchase an item
vm.purchase('Soda')

# Get the price of an item
print(vm.get_item_price('Chips'))

# Purchase another item
vm.purchase('Chips')

# Get the total sales
print(vm.get_total_sales())

# Insert some coins
vm.insert_money(5.00)
vm.insert_money(5.00)

# Purchase another item
vm.purchase('Chips')
vm.purchase('Chips')
vm.purchase('Chips')
vm.purchase('Candy')
vm.purchase('Candy')
print()

# print stats
vm.stats(3)
print()
vm.stats(5)
print()
vm.stats(6)
print()
# Remove an item
vm.remove_item('Candy')

# Show the available items again
vm.list_items()
'''