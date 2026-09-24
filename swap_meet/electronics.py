from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
    
    def __str__(self):
        item_message = super().__str__()
        return f"{item_message} This is a {self.type} device."


if __name__ == "__main__":
    test = Electronics()

    print(test.get_category())

    # print(test)