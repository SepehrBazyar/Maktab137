class User:
    users = []

    def __init__(
        self,
        username: str,
        password: str,
        phone_number: str,
        age: int | None = None,
    ):
        self.username = username
        self.__password = password
        self.phone_number = phone_number
        self.age = age
        self.addresses = []
        type(self).users.append(self)

    def login(self, username: str, password: str):
        return self.username == username and self.password == password

    def __repr__(self):
        return f"<{self.username}: {self.phone_number}>"


class Address:
    def __init__(self, user: User, description: str, zip_code: str):
        self.zip_code = zip_code
        self.description = description
        self.user = user
        self.user.addresses.append(self)

    @staticmethod
    def is_valid_zip_code(zip_code: str) -> bool:
        return len(zip_code) == 10

    @property
    def zip_code(self):
        return self._zip_code[:5] + "-" + self._zip_code[5:]

    @zip_code.setter
    def zip_code(self, value: str):
        if not self.is_valid_zip_code(value):
            raise ValueError("Invalid Zip Code")

        self._zip_code = value

    def __eq__(self, value: "Address"):
        return self.zip_code == value.zip_code

    def __repr__(self):
        return f"<{self.user}: {self.zip_code}>"


u1 = User("sepehr", "1234", "09123456789", age=24)
u2 = User(password="abcd", username="akbar", phone_number="09123456788")

# print(u1)
# print(u2)

# users = [
#     u1,
#     u2,
# ]

a1 = Address(u1, "test", "1234567890")
a2 = Address(u1, "test", "1234567891")
a3 = Address(u2, "test", "1234567890")

# print(a1.user)
# print(u1.addresses)
# print(u2.addresses)

d = {}
for user in User.users:
    for address in user.addresses:
        users_of_address = d.get(address.zip_code, [])
        users_of_address.append(user.phone_number)
        d[address.zip_code] = users_of_address

print(d)

print(u1.__class__)
print(u2.__class__)

print(type(u1))

# a4 = Address(u1, "test", "12")

print(a1.zip_code)

# a2.zip_code = "123"

# print(a2.zip_code_format)

# print(u1._User__password)

print(a1._zip_code)


class ProUser(User):
    def set_default_address(self, address: Address):
        self.default_address = address


pu1 = ProUser("pro", "pro", "09123456787", 18)
a4 = Address(pu1, "test-pro", "1234567890")
# print(pu1.default_address)
pu1.set_default_address(a4)
print(pu1.default_address)

# u1.set_default_address()

print(User.users)

print(a1 == a2)
print(a1 == a3)


class City:
    def __init__(self, prefix: str):
        self.prefix = prefix

    def __contains__(self, address: Address):
        return address.zip_code.startswith(self.prefix)


tehran = City(prefix="22")
print(a1 in tehran)

