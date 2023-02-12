# Transaction Class
A Python class for storing transactions and performing operations on them.

## Class Methods

### `__init__(self)`
This method initializes an empty list to store transactions.

### `add_item(self, name, price, quantity)`
This method takes in three parameters: `name`, `price`, and `quantity`, and adds a new transaction to the list with these values.

### `update_item_name(self, old_name, new_name)`
This method takes in two parameters: `old_name` and `new_name`, and updates the `name` of a transaction with `old_name` to `new_name`.

### `update_item_price(self, name, new_price)`
This method takes in two parameters: `name` and `new_price`, and updates the `price` of a transaction with `name` to `new_price`.

### `update_item_quantity(self, name, new_quantity)`
This method takes in two parameters: `name` and `new_quantity`, and updates the `quantity` of a transaction with `name` to `new_quantity`.

### `delete_transaction(self, name)`
This method takes in one parameter: `name`, and deletes the transaction with `name` from the list of transactions.

### `delete_item(self, name)`
This method takes in one parameter: `name`, and deletes the item with `name` from the list of transactions.

### `check_order(self)`
This method checks if the user inputs are correct (e.g. correct variable type, non-blank value).

### `total_price(self)`
This method displays a table with the `name`, `price`, `quantity`, and `total cost` of each transaction. The method also applies discounts to the total cost based on the following conditions:

- If the total cost is greater than `200000` but less than or equal to `300000`, the total cost is discounted by `5%`.
- If the total cost is greater than `300000` but less than or equal to `500000`, the total cost is discounted by `8%`.
- If the total cost is greater than `500000`, the total cost is discounted by `10%`.

## Example
Here's an example of how to use the Transaction class:

