from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    phone_number: str


@dataclass
class Product:
    title: str
    price: int


@dataclass
class ProductItem:
    product: Product
    count: int

    @property
    def total_price(self):
        return self.count * self.product.price


@dataclass
class BasketCartItems:
    items: list[ProductItem]
    index: int = field(
        init=False,
        default=0,
    )

    # def __init__(self, items):
    #     self.items = items
    #     self.index = 0

    @property
    def total(self):
        summation = 0
        for item in self.items:
            summation += item.count

        return summation

    def __next__(self):
        if self.index == len(self.items):
            raise StopIteration("End of Iteration")

        item = self.items[self.index]
        self.index += 1
        return item


@dataclass
class BasketCart:
    user: User
    items: BasketCartItems

    def __iter__(self):
        return self.items


user = User(name="sepehr", phone_number="09123456789")

ps5 = Product(title="PS5", price=1_000)
mobile = Product(title="IPhone", price=2_000)

item_1 = ProductItem(product=mobile, count=2)
item_2 = ProductItem(product=ps5, count=1)

items = BasketCartItems(
    items=[
        item_1,
        item_2,
    ],
)

print(items.total)

basket_cart = BasketCart(user=user, items=items)

for item in basket_cart:
    print(item.total_price)

# for item in basket_cart.items.items:
#     print(item.total_price)
