class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def say_first_name(self):
        print("Меня зовут ", self.first_name)
    def say_last_name(self):
        print("Моя фамилия", self.last_name)
    def say_all(self):
        print("Я -", self.first_name, self.last_name)