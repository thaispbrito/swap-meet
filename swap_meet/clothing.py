### Wave 5

from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric
    
    def __str__(self):
        item_message = super().__str__()
        return f"{item_message} It is made from {self.fabric} fabric."