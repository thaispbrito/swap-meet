import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):

        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        descriptions = {
            0 : "poor",
            1 : "heavily used",
            2 : "used",
            3 : "gently used",
            4 : "like new",
            5 : "mint"
        }
        return descriptions[self.condition]
