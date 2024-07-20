import math
from datetime import datetime
from app.car import Car


class Customer:
    def __init__(
            self, name: str, product_cart: dict,
            location: list, money: float, car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, shop_location: dict) -> float:
        return math.sqrt(
            (shop_location[0] - self.location[0])
            ** 2 + (shop_location[1] - self.location[1]) ** 2)

    def travel_cost(self, distance: float, fuel_price: float) -> float:
        return (distance * self.car.fuel_consumption / 100) * fuel_price

    def purchase_cost(self, shop_products: dict) -> float:
        total_cost = 0
        for product, quantity in self.product_cart.items():
            total_cost += shop_products[product] * quantity
        return total_cost

    def print_receipt(self, shop_name: str, shop_products: dict) -> None:
        print(f"Date: {datetime(
            2021, 4, 1, 12, 33, 41
        ).strftime("%m/%d/%Y %H:%M:%S")}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in self.product_cart.items():
            cost = shop_products.get(product, 0) * quantity
            total_cost += cost
            formatted_cost = f"{cost: .2f}".rstrip("0").rstrip(".")
            print(f"{quantity} {product}s for{formatted_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
