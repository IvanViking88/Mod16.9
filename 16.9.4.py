class Party:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}, {self.city}. Balance {self.balance}eu.'

    def get_guest(self):
        return f'{self.name} {self.surname}. {self.city}'

human_1 = Party('Jack', 'Vorobei', 'Vorsburg', 700)
human_2 = Party('Liz', 'Blackshield', 'Oakenwood', 1500)
human_3 = Party('Bobster', 'Klawitz', 'Stutgart', 350)

party_list = [human_1, human_2, human_3]

print('These customers will come to the party:\n')
for human in party_list:
    print(human.get_guest())
