class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def email(self):
        return f"{self.full_name()}@gmail.com".replace(' ', '')
    @classmethod
    def fullname_two(cls, first_name, last_name):
        return cls(last_name, first_name)
    def __str__(self):
        return self.full_name

p1 = Person.fullname_two('Hosein', 'Roosta')
print(p1.full_name())
print(p1.email())
print('-'*50)
p2 = Person('Hosein', 'Roosta')
print(p2.full_name())
print(p2.email())