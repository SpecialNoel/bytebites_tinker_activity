from models import *

item1 = FoodItem(name="Burger", price=10.99, category="Food", popularity_rating=5.0)
item2 = FoodItem(name="Cola", price=5.99, category="Drink", popularity_rating=4.0)

order = Order()
order.add_item(item1, 3) 
order.add_item(item2, 2) 
print("Items in the order: ", order.to_dict(), "\n") # Part3: add food items to order
print("Total cost for the order: ", order.get_total_cost(), "\n") # Part3: calculate the total cost of the order

menu = Menu()
menu.add_item(item1)
menu.add_item(item2)
print(menu, "\n")
print("Filter by Food: ",menu.filter_by_category("Food"), "\n") # Part3: filter the menu by the category of the food item
print("Sort by price: ",menu.sort_by_price(), "\n") # Part3: sort the menu by price in ascending order
