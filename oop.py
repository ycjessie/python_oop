class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hi! My name is {self.name}')
    
    def hello_class():
        print("hello everyone")

me = User('Jessie')
me.greet()