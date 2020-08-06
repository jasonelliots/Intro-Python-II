class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments 

    def __str__(self):
        return 'Welcome to the quarantine store'

    def print_departments(self):
        for id in self.departments:
            print(self.departments[id])
        print()
