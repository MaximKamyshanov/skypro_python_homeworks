class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.family = last_name

    def first_name(self):
        print("Имя:", self.name)

    def last_name(self):
        print("Фамилия:", self.family)

    def full_name(self):
        print("Имя и Фамилия:", self.name, self.family)



   