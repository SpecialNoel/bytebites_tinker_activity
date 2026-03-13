# Classes designed:
# - Customer: each customer has a name, can view and add orders to their purchase history
# - FoodItem: each food item has a name, a price, a category indicating whether it is a drink or food, and a popularity rating based on customer reviews
# - Menu: each menu has a list of food items. The manager of the app can edit the list, and the customer can view and filter the list.
# - Order: each order has a list of food items, a total price for all the food in this order, and can edit food items in the order.

class FoodItem:
    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float = 0.0,
    ):
        self.name: str = name.strip()
        if not self.name:
            raise ValueError("name must be non-empty")

        self.price: float = float(price)
        self.category: str = category.strip()
        if not self.category:
            raise ValueError("category must be non-empty")

        self.popularity_rating: float = float(popularity_rating)
        self._validate()

    def _validate(self) -> None:
        if self.price < 0:
            raise ValueError("price must be >= 0")

        if not (0.0 <= self.popularity_rating <= 5.0):
            raise ValueError("popularity_rating must be between 0.0 and 5.0")

    def update_rating(self, rating: float) -> None:
        """Adjust the popularity rating (0.0–5.0)."""
        self.popularity_rating = float(rating)
        self._validate()

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "popularity_rating": self.popularity_rating,
        }

    def __repr__(self) -> str:
        return (
            f"FoodItem(name={self.name!r}, price={self.price:.2f}, "
            f"category={self.category!r}, rating={self.popularity_rating:.1f})"
        )

class Order:
    def __init__(self, items: list[FoodItem] | None = None):
        self.items: list[FoodItem] = []
        if items:
            for item in items:
                self.add_item(item)

    def add_item(self, item: FoodItem) -> None:
        if not isinstance(item, FoodItem):
            raise TypeError("item must be a FoodItem")
        self.items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        self.items.remove(item)

    def get_total_cost(self) -> float:
        return sum(item.price for item in self.items)

    def get_item_count(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return not self.items

    def to_dict(self) -> dict[str, object]:
        return {
            "items": [item.to_dict() for item in self.items],
            "total_cost": self.get_total_cost(),
        }

    def __repr__(self) -> str:
        return f"Order(items={len(self.items)}, total={self.get_total_cost():.2f})"
    

class Customer:
    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Customer name must be non-empty")
        self.name: str = name.strip()
        self.purchase_history: list[Order] = []

    def add_order(self, order: Order) -> None:
        self.purchase_history.append(order)

    def get_orders(self) -> list[Order]:
        return list(self.purchase_history)

    def get_total_spent(self) -> float:
        return sum(order.get_total_cost() for order in self.purchase_history)

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r}, orders={len(self.purchase_history)})"
        
class Menu:
    def __init__(self, items: list[FoodItem] | None = None):
        self.items: list[FoodItem] = []
        if items:
            for item in items:
                self.add_item(item)

    def add_item(self, item: FoodItem) -> None:
        if not isinstance(item, FoodItem):
            raise TypeError("Menu items must be FoodItem instances")
        self.items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        self.items.remove(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        category_norm = category.strip().lower()
        return [
            item
            for item in self.items
            if item.category.strip().lower() == category_norm
        ]

    def get_categories(self) -> set[str]:
        return {item.category for item in self.items}

    def find_by_name(self, name: str) -> list[FoodItem]:
        name_norm = name.strip().lower()
        return [item for item in self.items if item.name.strip().lower() == name_norm]

    def __repr__(self) -> str:
        return f"Menu(items={len(self.items)})"
    