#import csv

# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
# print(item1_price_total)
# print(type(item1))




# item1 = Item("Phone", 100, 5)
# item1.apply_discount()
# print(item1.price)
# item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5
# print(item1.calculate_total_price())

# print(type(item1.name))

# item2 = Item("Laptop", 1000, 8)
# item2.pay_rate = 0.7 # change rate for different items set it self.pay_rate in the method
# item2.apply_discount()
# print(item2.price)
# item2.name = "Laptop"
#item2.price = 1000
#item2.quantity = 3
# print(item2 .calculate_total_price(item2.price, item2.quantity))

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
# print(Item.pay_rate) # accessing class attribtue
# print(item1.pay_rate) # accessing class attribtue from instance/object
# print(item2.pay_rate) # accessing class attribtue from instance/object

# print(Item.__dict__) # to know all class level attribute
# print(item1.__dict__) # to know all instance level attribute
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)


#Item.instantiate_from_csv()
# print(Item.all)
##****************** I GOT an ERROR SOLVE IT FIRST ##1:03:00


# Accessing static method
# print(Item.is_integer(8.8))


### 1:09:00


# phone1 = Item('Iphone12', 500, 10)
# phone1.broken = 2
# phone2 = Phone('Huawei J12', 650, 14, 4) # same as Item class because it inherited funcs from it.
# phone2.broken = 3
# phone3 = Phone('Samsung pro', 1800, 6, 6)
# print(phone3.calculate_total_price())
# phone3.broken = 0

# print(Item.all)
# print(Phone.all)

## *** 01:30:00




# class Intro:
#     def __init__(self, name: str, gender: str, role: str, hobby: str):
#         self.name = name
#         self.gender = gender
#         self.__role = role
#         self.hobby = hobby

#     def hi(self):
#         return f'Hi! I am {self.name}, a {self.__role}.I speak: English, Swahili, Somali & Arabic.I like science, computer and {self.hobby}'


# me = Intro('Mohamed', 'M', 'Programmer and ICT', 'robotics(Battlebot channel)')
# print(me.hi())
