from datetime import date

import dill


ADULT_AGE = 16


class User:
    def __init__(self, name: str, phone_number: str, birth_date: date):
        self.name = name
        self.phone_number = phone_number
        self.birth_date = birth_date

    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365

    @property
    def is_adult(self):  # for adult products
        return self.age >= ADULT_AGE

    def __repr__(self):
        return f"<{self.name}: {self.phone_number}>"


class Wallet:
    def __init__(self, user: User, balance: int, password: str):
        self.user = user
        self.balance = balance
        self.__password = password

    def __isub__(self, value: int):
        assert value <= self.balance, "Not Enough!"

        self.balance -= value
        return self

    def check_password(self, new_password: str):
        return self.__password == new_password

    def __repr__(self):
        return f"<{self.user}: {self.balance}>"


class Product:
    def __init__(self, title: str, inventory: int, price: int):
        self.title = title
        self.inventory = inventory
        self.price = price

    def __repr__(self):
        return f"<{self.title}: {self.inventory} ({self.price} $)>"


class BasketCart:
    def __init__(self, product: Product, count: int):
        self.product = product
        self.count = count

    def __enter__(self):
        self.product.inventory -= self.count
        return self

    def payment(self, wallet: Wallet, password: str):
        """Charge a user's wallet for the items in this basket.

        This method verifies the provided password against the wallet, then
        deducts the total price (product.price * count) from the wallet using
        the wallet's in-place subtraction operator. It does not perform any
        further validation (for example, it assumes inventory has already been
        reserved by the context manager entry).

        Args:
            wallet (Wallet): The wallet to charge. Must be associated with the
                buyer and support `check_password` and in-place subtraction
                (`__isub__`) for numeric values.
            password (str): Plain-text password to authenticate the wallet.

        Raises:
            AssertionError: If the provided password does not match the
                wallet's password or if the wallet has insufficient balance
                (the wallet's `__isub__` will assert on insufficient funds).

        Side effects:
            - Calls `wallet.check_password(password)` to authenticate.
            - Mutates `wallet.balance` via `wallet -= amount`.

        Returns:
            None
        """
        assert wallet.check_password(password), "INVALID"
        wallet -= (self.count * self.product.price)

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            print("FAILED", exc_value)
            self.product.inventory += self.count
        else:
            print("congratulations")

        return True


p1 = Product("PS5", 100, 1000)
user = User("akbar", "09123456789", date(2000, 11, 25))
w1 = Wallet(user, 5_000, "1122")
o1 = BasketCart(p1, 20)

print(dill.dumps([user, p1, w1, o1]))

# with o1:
#     o1.payment(w1, "1122")

# print(w1)
# print(p1)
