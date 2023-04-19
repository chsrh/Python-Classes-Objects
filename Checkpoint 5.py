#Class Point3D:
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        return (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point.coordinates())


#Class Rectangle:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


my_rectangle = Rectangle(4, 3)
print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())


#Class Circle:
import math

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def isInside(self, point):
        distance = math.sqrt((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False


my_circle = Circle((0, 0), 5)
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())
print("(2, 2) is inside the circle?", my_circle.isInside((2, 2)))
print("(6, 6) is inside the circle?", my_circle.isInside((6, 6)))


#Class Bank:
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            return self.balance


my_account = Bank(1000)
print("Current balance:", my_account.balance)

my_account.deposit(500)
print("Current balance after deposit:", my_account.balance)

my_account.withdraw(200)
print("Current balance after withdrawal:", my_account.balance)

my_account.withdraw(1500)
print("Current balance after withdrawal with insufficient funds:", my_account.balance)

