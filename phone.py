from item import Item
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