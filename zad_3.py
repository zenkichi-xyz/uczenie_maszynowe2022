class Property:
    def __init__(self, area, rooms: int, price: int, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Adres: {self.address}, Pokoje: {self.rooms}, Powierzchnia: {self.area}m2, Cena: {self.price}zł'


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}, Plot: {self.plot}'


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}, Floor: {self.floor}'


house1 = House(50, 1, 100000, 'Jaworzno', 400)
flat1 = Flat(55, 5, 450000, 'Kraków', 550)
print(house1)
print(flat1)
