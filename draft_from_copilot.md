classDiagram
class Customer {
+name: String
+purchaseHistory: Order[]
+addOrder(order: Order): void
}
class FoodItem {
+name: String
+price: Double
+category: String
+popularityRating: Double
}
class Menu {
+items: FoodItem[]
+addItem(item: FoodItem): void
+removeItem(item: FoodItem): void
+filterByCategory(category: String): List~FoodItem~
}
class Order {
+customer: Customer
+items: List~FoodItem~
+addItem(item: FoodItem): void
+removeItem(item: FoodItem): void
+getTotalCost(): Double
}
Customer --> Order : has
Menu --> FoodItem : contains
Order --> FoodItem : contains
