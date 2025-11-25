from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"<{self.name}: {self.phone_number}>"


class Wallet:
    def __init__(self, user: User, amount: int = 0):
        self.user = user
        self.amount = amount

    # def __add__(self, value: int):
    #     return type(self)(self.user, self.amount + value)

    def __iadd__(self, value: int):
        self.amount += value
        return self

    # def __sub__(self, value: int):
    #     return type(self)(self.user, self.amount - value)

    def __isub__(self, value: int):
        self.amount -= value
        return self

    def __gt__(self, other: "Wallet"):
        return self.amount > other.amount

    def __lt__(self, other: "Wallet"):
        return self.amount < other.amount

    def __ge__(self, other: "Wallet"):
        return self.amount > other.amount or self.amount == other.amount


    def __le__(self, other: "Wallet"):
        return self.amount < other.amount or self.amount == other.amount

    def __repr__(self):
        return f"<{self.user}: {self.amount}>"


u1 = User("akbar", "09123456789")
w1 = Wallet(u1, amount=100)
w2 = Wallet(u1)

# print(w1 + 100)
print(w1.amount)
print(id(w1))

w1 += 100
print(id(w1))
print(w1.amount)
print(w1)

w1 -= 50
print(id(w1))
print(w1.amount)

print(w1 > w2)
print(w1 < w2)  # w2 > w1

print(w1 >= w2)
print(w1 <= w2)


class Rectangle:
    def __init__(self, x: int | float, y: int | float):
        self.x, self.y = x, y
        # self.area = x * y

    @property
    def area(self):
        return self.x * self.y

    def __repr__(self):
        return f"{self.x} * {self.y}"


class Square(Rectangle):
    def __init__(self, x: int | float):
        # print(isinstance(super(), Rectangle))
        super().__init__(x, x)


r1 = Rectangle(5, 4)
print(r1)
print(r1.area)

r1.x = 6
print(r1)
print(r1.area)

s1 = Square(x=3)
print(s1)
print(s1.area)


class Courier(User):
    pass


c1 = Courier("asqar", "09123456788")

class Vehicle(ABC):
    def __init__(self, cycle: int):
        self.cycle = cycle

    @abstractmethod
    def speed(self):
        pass

    def delivery(self):
        print("DELIVERED")


class MotorCycle(Vehicle):
    def __init__(self):
        super().__init__(2)

    def speed(self):
        return 100


class PlayMusicMixin:
    def play_music(self):
        print("SOUND")


class AutoMobile(Vehicle, PlayMusicMixin):
    def __init__(self):
        super().__init__(4)

    def speed(self):
        return 80


class Truck(Vehicle, PlayMusicMixin):
    def __init__(self):
        super().__init__(4)

    def speed(self):
        return 50


mc = MotorCycle()
am = AutoMobile()

print(mc.speed())
print(am.speed())

# v = Vehicle(cycle=3)

# t = Truck()

mc.delivery()
am.delivery()

t = Truck()

am.play_music()
t.play_music()
# mc.play_music()


class Base:
    def test(self):
        return "Base"


class Mother(Base):
    def test(self):
        return super().test() + " -> Mother"


class Father(Base):
    def test(self):
        return super().test() + " -> Father"


class Child(Mother, Father):
    def test(self):
        return super().test() + " -> Child"


c = Child()
print(c.test())

print(Child.mro())


def length(value: str | list):
    if isinstance(value, str):
        return 1
    elif isinstance(value, list):
        return 2
    
    return 3

print(length("hello"))
print(length([1,2,3]))
print(length(123))


def func(courier: Courier, vehicle: Vehicle):
    ...
    return vehicle.speed()


print(func(c1, mc))
print(func(c1, am))
print(func(c1, t))
