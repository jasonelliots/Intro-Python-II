# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'{self.name}. {self.description}'

    # def add(self, item):
    #     self.items.append(item)

    def add(self, item, player_items):
        for i in player_items:
            if i.name == item:
                self.items.append(i)

    def remove(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)

    def print_items(self):
        print('Items in this room:')
        for i in self.items:
            print(f"{i.name}: {i.description}")
        return ""