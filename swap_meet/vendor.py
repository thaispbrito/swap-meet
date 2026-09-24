class Vendor:

    def __init__(self, inventory=None):
        
        self.inventory = [] if inventory is None else inventory

    def add(self, item):

        self.inventory.append(item)

        return item

    def remove(self, item):

        if item not in self.inventory:
            return None
        
        self.inventory.remove(item)

        return item

    def get_by_id(self, item_id):

        for item in self.inventory:
            if item.id == item_id:
                return item
            
        return None

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    def swap_first_item(self, other_vendor):

        if  not self.inventory or not other_vendor.inventory:
            return False

        my_item = self.inventory.pop(0)
        their_item = other_vendor.inventory.pop(0)

        self.inventory.insert(0, their_item)
        other_vendor.inventory.insert(0, my_item)
        
        return True




        
        
