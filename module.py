class Transaction():

    """A class to store transactions and calculate the total cost of items.
    """
    
    def __init__(self):

        """Initialize the class with an empty list to store items."""

        self.items = []

    def add_item(self, name, price, quantity):

        """Add an item to the transaction.

        Args:
        name (str): The name of the item.
        price (float): The price of the item.
        quantity (int): The quantity of the item.
        """

        if self.check_order(name, price, quantity):
            self.items.append({'name': name, 'price': price, 'quantity': quantity})
            print(f'successfully added {name}, by {quantity}, with price of {price} each')
        else:
            print("Error: Invalid input")

    def update_item_name(self,index,name):

        """Update the name of an item in the transaction.

        Args:
        index (int): The index of the item in the transaction.
        name (str): The new name for the item.
        """

        if self.check_order(name):
            self.items[index]['name']=name
        else:
            print("Error: Invalid input")

    def update_item_price(self,index,price):

        """Update the price of an item in the transaction.

        Args:
        index (int): The index of the item in the transaction.
        price (float): The new price for the item.
        """

        if self.check_order(price):
            self.items[index]['price']=price
        else:
            print("Error: Invalid input")

    def update_item_qty(self,index,quantity):

        """Update the quantity of an item in the transaction.

        Args:
        index (int): The index of the item in the transaction.
        quantity (int): The new quantity for the item.
        """

        if self.check_order(quantity):
            self.items[index]['quantity']=quantity
        else:
            print("Error: Invalid input")

    def reset_transaction(self):

        """Delete all items in the transaction."""

        self.items.clear()
        print("Successfully deleted every item in transaction")

    def delete_item(self, name):

        """Delete a specific item from the transaction.

        Args:
        name (str): The name of the item to be deleted.
        """

        for i in range(len(self.items)):
            if self.items[i]['name'] == name:
                self.items.pop(i)
                break
        print(self.items)

    def check_order(self,*args):

        """Check if the input is valid.

        Args:
        *args: One or more values to be checked.

        Returns:
        bool: True if all inputs are valid, False if else"""

        for arg in args:
            if arg=='' or arg==None or (type(arg) not in (int,float,str)):
                return False
        return True

    def total_cost(self):

        """Calculate the total cost of all items in the transaction.

        Returns:
        float: The total cost of all items in the transaction.
        """

        return sum(item['price'] * item['quantity'] for item in self.items)

    def total_price(self):

        """Calculate the total price after discounts of all items in the transaction.

        Returns:
        float: The total cost of all items in the transaction.
        """

        total_cost = self.total_cost()
        if total_cost > 200000 and total_cost <= 300000:
            discount = 0.05
        elif total_cost > 300000 and total_cost <= 500000:
            discount = 0.08
        elif total_cost > 500000:
            discount = 0.1
        else:
            discount = 0
        print("Item Name\tPrice\tQuantity\tDiscount\tTotal Cost")
        for item in self.items:
            print(f"{item['name']}\t\t{item['price']}\t{item['quantity']}\t{discount*100}\t{item['price']*item['quantity']*(1-discount)}")
        print(f"Total Cost: {total_cost*(1-discount)}")