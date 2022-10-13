class Customer:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Balance: {self.balance}Eu.'

Ivan_s = Customer('Ivan', 'Supov', 'Dusseldorf', 7800000000)

print(Ivan_s)