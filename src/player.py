class Player:
    def __init__(self, location, hp=100, items=['apple', 'sword', 'lucky socks']):
        self.location = location 
        self.hp = hp
        self.items = items

    def __str__(self):
        return f'Location: {self.location}, HP: {self.hp}, Items:{self.items}'

    def location(self):
        print(f'Current location is: {self.location}')
