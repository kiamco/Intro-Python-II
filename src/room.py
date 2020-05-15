# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from simple_chalk import chalk, green

class Room(Item):
    def __init__(self, name, description, room_items=[]):
        super().__init__(room_items)
        self.name = name
        self.description = description
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def add_item(self, item):
        self.items.append(item)

        
    def __str__(self):
        return f'{self.name}: {self.description}: Room has {chalk.yellow(self.items) if len(self.items) > 0 else "no items"}'