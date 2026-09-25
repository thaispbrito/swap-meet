# Max helper function
def my_max(my_collection, key):
    max_item = my_collection[0]
    max_value = key(my_collection[0])

    for item in my_collection:
        if key(item) > max_value:
            max_item = item
            max_value = key(item)

    return max_item

### Wave 1

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

    ### Wave 2

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item  
                  
        return None

    ### Wave 3

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    ### Wave 4

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)

    ### Wave 6

    def get_by_category(self, category):
        items_by_category = []

        for item in self.inventory:
            if item.get_category() == category:
                items_by_category.append(item)

        return items_by_category

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)

        if not items_by_category:
            return None
        
        return my_max(items_by_category, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, my_item, their_item)
