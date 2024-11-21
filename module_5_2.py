class House:
    def __init__(self, name, nummers_of_floors):
        self.name = name
        self.number_of_floors = nummers_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-ов этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('Жк Акация', 20)

print(h1)
print(h2)


print(len(h1))
print(len(h2))
