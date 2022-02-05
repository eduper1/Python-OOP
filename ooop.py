import csv

# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
# print(item1_price_total)
# print(type(item1))


class Item:
    pay_rate = 0.8  # the pay rate after20% discount
    all = []  # Creating a list of all objects, each objects represents and instance

    def __init__(self, name: str, price: float, quantity: 0):
        # Run validation on argument received
        #assert price >=0, f"Price {price} is not greater than or equal to zero"
        # **** File "/home/sirus/Desktop/Python/oop/ooop.py", line 16, in __init_
        #assert price >=0, f"Price {price} is not greater than or equal to zero"
        # TypeError: '>=' not supported between instances of 'NoneType' and 'int
        # Above error is same error type for quantity _
        #assert quantity >= 0, f"Quantity {quantity} is not greater  than or equal zero!"

        # Assign to self object
        self.price = price
        self.quantity = quantity
        self.name = name

        # Action to excute
        Item.all.append(self)
        # print(f"{name} object created ")
    # def calculate_total_price(self, x, y):
    #     return x * y

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # changed class attribute with self

    # @classmethod
    # def instantiate_from_csv(cls):
    #     with open('items.csv', 'r') as f:
    #         reader = csv.DictReader(f)
    #         items = list(reader)

    #     for item in items:
    #         print(item)
    #         Item(
    #             name=item.get('name'),
    #             price=item.get('price'),
    #             quantity=item.get('quantity'),
    #         )
            # Item(
            #     name=item.get('name'),
            #     price=float(item.get('price')),
            #     quantity=int(item.get('quantity')),
            # )
    # represent all data object/instance in the list in a readable manner
    # @staticmethod
    # def is_integer(num): # static class is more regular function than a class function, it doesn't take self as 1st argument
    #     # count out the floats that are point zero
    #     # for i.e 5.0, 10.0
    #     if isinstance(num, float):
    #         # count out the floats that are point zero
    #         return num.is_integer()
    
    #     elif isinstance(num, int):
    #         return True
    #     else:
    #         return False
        
    
    def __repr__(self):
        # Accesing name of the class from the instance: to differentiate Items instance from Phone Instance
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

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
class Phone(Item):
    # all = []  ** remove class attribute from child class
    def __init__(self, name: str, price: float, quantity: 0, broken=0):
        # call to supper function to have access to all attributes/ method from parent class
        super().__init__(
            name, price, quantity   
        )
        # validation
        assert broken >= 0, f"{broken}: Broken phones must be greater or equal to 0"

        # Assign to self object
        self.broken = broken
        # Action to excute
        # Phone.all.append(self)     remove all parent attribute 

phone1 = Item('Iphone12', 500, 10)
# phone1.broken = 2
phone2 = Phone('Huawei J12', 650, 14, 4) # same as Item class because it inherited funcs from it.
# phone2.broken = 3
phone3 = Phone('Samsung pro', 1800, 6, 6)
print(phone3.calculate_total_price())
# phone3.broken = 0

print(Item.all)
print(Phone.all)

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
