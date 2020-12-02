class Dog:
    def __init__(self, name):
        self.name = name
        self.good_dog = True
        self.legs = 4  # For __add__

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __getattr__(self, attr):
        return f"{attr} doesn't exist man"

    # def __setattr__(self, attr, value): # This will cause recursion
    #     self.attr = value

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

    def __add__(self, instance):
        return self.legs + instance.legs

    # def __getitem__(self, item): # This will cause recursion
    #     return self[item]

    def __getitem__(self, item):
        return self.__dict__[item]


maddie = Dog('Maddie')
print(str(maddie))  # Maddie __str__

print(len(maddie))  # Maddie __len__

print(maddie.what_is_up)  # Maddie __getattr__

maddie.new_attr = "This is new"  # Maddie __setattr__
print(maddie.new_attr)

fluffy = Dog('Fluffy')  # Fluffy __add__
print(maddie + fluffy)

print(fluffy['name'])  # Fluffy __getitem__