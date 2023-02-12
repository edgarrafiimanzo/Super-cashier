# Super-cashier
Submission for Pacmann's Python module


Transaction Class
A Python class to store transactions and calculate the total cost of items.

Table of Contents
Methods
__init__
add_item
update_item_name
update_item_price
update_item_quantity
delete_transaction
delete_item
check_order
total_cost
Methods
__init__
Initialize the class with an empty list to store items.

add_item
Add an item to the transaction.

Arguments:
name: The name of the item.
price: The price of the item.
quantity: The quantity of the item.
update_item_name
Update the name of an item in the transaction.

Arguments:
index: The index of the item in the transaction.
name: The new name for the item.
update_item_price
Update the price of an item in the transaction.

Arguments:
index: The index of the item in the transaction.
price: The new price for the item.
update_item_quantity
Update the quantity of an item in the transaction.

Arguments:
index: The index of the item in the transaction.
quantity: The new quantity for the item.
delete_transaction
Delete all items in the transaction.

delete_item
Delete a specific item from the transaction.

Arguments:
name: The name of the item to be deleted.
check_order
Check if the input is valid.

Arguments:
*args: One or more values to be checked.
total_cost
Calculate the total cost of all items in the transaction.

Returns:
The total cost of all items in the transaction.
