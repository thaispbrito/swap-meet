### Wave 2 

import uuid

class Item:

    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    ### Wave 3
       
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    ### Wave 5

    def condition_description(self):
        if not 0 <= self.condition <= 5:
            raise ValueError("Condition must be between 0 and 5!")

        if self.condition == 0:
            description = "disgusting"
        elif self.condition < 1:
            description = "heavily used"
        elif self.condition < 2:
            description = "moderately used"    
        elif self.condition < 3:
            description = "used"
        elif self.condition < 4:
            description = "gently used"
        elif self.condition < 5:
            description = "like new"
        else:
            description = "brand new"

        return description