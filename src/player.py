# Write a class to hold player information, e.g. what room they are in
# currently.
from simple_chalk import chalk, green


from item import Item
class Player(Item):
    def __init__(self,room, items=[]):
        super().__init__(items)
        self.room = room
        
    def set_room(self,new_room):
        self.room = new_room
        return self
    
    def add_item(self, room_item):
        self.items.append(room_item)
        
    def __str__(self):
        return f'\t{chalk.magenta("Current Room ---> ")} {self.room} \n\t{chalk.yellow("items")} ---> player holding {self.items if len(self.items) > 0 else "no items"} '