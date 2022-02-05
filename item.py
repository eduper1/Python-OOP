import csv

class Item:
    pay_rate = 0.8  # the pay rate after20% discount
    all = []  # Creating a list of all objects, each objects represents and instance

    def __init__(self, name: str, price: float, quantity: 0):
        # Run validation on argument received
        # assert price >=0, f"Price {price} is not greater than or equal to zero"
        # **** File "/home/sirus/Desktop/Python/oop/ooop.py", line 16, in __init_
        # assert price >=0, f"Price {price} is not greater than or equal to zero"
        # TypeError: '>=' not supported between instances of 'NoneType' and 'int
        # Above error is same error type for quantity _
        # assert quantity >= 0, f"Quantity {quantity} is not greater  than or equal zero!"

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity'),
            )
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
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