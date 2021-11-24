# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
# print(item1_price_total)
# print(type(item1))  

class Item:
    pay_rate = 0.8 # the pay rate after20% discount
    all = [] # Creating a list of all objects, each objects represents and instance
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation on argument received
        assert price >=0, f"Price {price} is not greater than or equal to zero" 
        assert quantity >= 0, f"Quantity {quantity} is not greater  than or equal zero!"
        
        
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
        self.price = self.price * self.pay_rate # changed class attribute with self
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)
# item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5
print(item1.calculate_total_price())

# print(type(item1.name))

item2 = Item("Laptop", 1000, 8)
item2.pay_rate = 0.7 # change rate for different items set it self.pay_rate in the method
item2.apply_discount()
print(item2.price)
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
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
for instance in Item.all:
    print(instance.name)