class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Ресторан {self.restaurant_name} и кухня {self.cuisine_type}')


    def open_restaurant(self):
        print("Ресторан сейчас открыт.")


restaurant = Restaurant("Фрунзе", "Европейская")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Пишпек", "Азиятская")
restaurant2 = Restaurant("ДоДо пицца", "Итальянская")
restaurant3 = Restaurant("Стейкхаус", "Американская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'Имя {self.first_name}, фамилия {self.last_name}, возраст {self.age}')

    def greet_user(self):
        print(f'привет {self.first_name} {self.last_name}, как дела?')


user1 = User("Адиль", "Таштаналиев", 17)
user2 = User("Атахан", "Орозбеков", 17)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

