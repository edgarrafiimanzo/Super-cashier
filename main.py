from module import *


# Example usage:
trnsct_123 = Transaction()
trnsct_123.add_item("mobil",1, 1000000)
trnsct_123.add_item("motor",1, 10000)
trnsct_123.delete_item("motor")
trnsct_123.reset_transaction()
trnsct_123.add_item("moge", 10_000_000, 1)
trnsct_123.add_item("pisang", 5000, 1000)
trnsct_123.total_price()