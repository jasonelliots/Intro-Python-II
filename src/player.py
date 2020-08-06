class Player:
    def __init__(self, location, hp=100, items=[]):
        self.location = location 
        self.hp = hp
        self.items = items

    def __str__(self):
        return f'Location: {self.location.name} \n HP: {self.hp} \n Items:{self.items} \n'

    def get(self, item):
        for i in self.location.items:
            if i.name == item:
                self.items.append(i)
        print(f'You picked up {item}!')

    def drop(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
        print(f'You dropped {item}!')

    def print_items(self):
        print('Your items:')
        for i in self.items:
            print(f"{i.name}: {i.description}")
        return ''
