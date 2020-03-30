from typing import Dict

my_products = {
    "apple": 1.09,
    "bananas": 2.15,
    "onions": 0.50
}

class ShoppingBasket:
    def __init__(self, products):
        print("Hello from init method")
        print(products)
        self.prod = products

    def display_products(self):
        for product, cost in self.prod.items():
            print(f"Product name: {product} | Product cost {cost}")


my_shopping_baket = ShoppingBasket(my_products)
print(my_shopping_baket.prod)
my_shopping_baket.display_products()

your_produccts = {"carrots": 1.01, "cabbage": 0.10}
your_basket = ShoppingBasket(your_produccts)
print(your_basket.prod)
your_basket.display_products()


def calculate_cost_of_products(products: Dict[str, float]):
    sum = 0
    for item, cost in products.items():
        sum = sum+ cost
    return sum



total = calculate_cost_of_products(my_products)
print(total)
