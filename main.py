# class Human:
#     print('я родился')

# Human

# class HondaCar:

# class Car:
#     '''это описание класса Car
#     ОН принимает в аргументы цвет, бренд, модель и год'''
#
#     def __init__(self, colour, brand, model, year=2022):
#         '''он принимает увет бренд модель и год выпуска'''
#         self.colour = colour
#         self.year = year
#         self.brand = brand
#         self.model = model
#
#     def info(self):
#         print(f'{self.colour}')
#         print(f'{self.year}')
#         print(f'{self.brand}')
#         print(f'{self.model}')
#
#     def __str__(self):
#         print(f'{self.colour}')
#         print(f'{self.year}')
#         print(f'{self.brand}')
#         print(f'{self.model}')
#         return f'{self.colour} {self.model}'
#
#
# car_1 = Car('White', 'BMW', 'X7')
# car_2 = Car('Black', 'Mercedes-Benz', 'GlE450')
#
# print(car_1.__dict__)
# print(car_2.__dict__)
#
# car_1.info()
# car_2.info()
#
# print(help(car_1))
# print(dir(car_1))

# class Human:
#     def __init__(self, language, name):
#         self.language = language
#         self.name = name
#
#     def speech(self):
#         if self.language == 'kg':
#             return f'Салам, менин атым {self.name}'
#         elif self.language == 'ru':
#             return f'Привет, меня зовут {self.name}'
#         else:
#             return f'Hello, my name is {self.name}'
#
#
# person_1 = Human('kg', 'adil')
# person_2 = Human('ru', 'adil')
# person_3 = Human('eng', 'adil')
#
# print(person_1.speech())
# print(person_2.speech())
# print(person_3.speech())


