import pytest
from models import *

@pytest.fixture
def sample_items():
    return [
        FoodItem(name="Burger", price=10.0, category="Food", popularity_rating=4.0),
        FoodItem(name="Fries", price=5.0, category="Food", popularity_rating=3.5),
        FoodItem(name="Soda", price=2.5, category="Drink", popularity_rating=4.5),
        FoodItem(name="Coffee", price=3.0, category="Drink", popularity_rating=4.8),
    ]
    
def test_menu_filter_by_category(sample_items):
    menu = Menu(items=sample_items)

    foods = menu.filter_by_category("food")
    assert len(foods) == 2
    assert {item.name for item in foods} == {"Burger", "Fries"}

    drinks = menu.filter_by_category("Drink")
    assert len(drinks) == 2
    assert {item.name for item in drinks} == {"Soda", "Coffee"}

    # invalid category should return empty list
    assert menu.filter_by_category("dessert") == []
    assert menu.filter_by_category("") == []
    
def test_order_add_item_and_total_cost():
    burger = FoodItem(name="Burger", price=10.0, category="Food")
    fries = FoodItem(name="Fries", price=5.0, category="Food")

    order = Order()

    # Add 2 burgers and 1 fries
    order.add_item(burger, quantity=2)
    order.add_item(fries, quantity=1)
    assert order.get_total_cost() == pytest.approx(25.0)

    # Add 1 more burger (should accumulate quantity)
    order.add_item(burger, quantity=1)
    assert order.get_total_cost() == pytest.approx(35.0)

def test_order_add_item_validation():
    burger = FoodItem(name="Burger", price=10.0, category="Food")
    order = Order()

    # invalid quantity must raise
    with pytest.raises(ValueError):
        order.add_item(burger, quantity=0)

    with pytest.raises(ValueError):
        order.add_item(burger, quantity=-1)

    # invalid item type must raise
    with pytest.raises(TypeError):
        order.add_item("not-a-fooditem", quantity=1)
        