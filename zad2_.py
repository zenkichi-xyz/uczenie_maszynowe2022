class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if sum(self.marks) / len(self.marks) > 50:
            return True
        return False


s1 = Student('Szymon', [40, 50, 50, 70, 80])
s2 = Student('Jan', [10, 50, 49, 30, 20])


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Miasto: {self.city}, Ulica: {self.street}, Kod pocztowy: {self.zip_code}, Godziny otwarcia: {self.open_hours}, Telefon kontaktowy: {self.phone}'


l1 = Library('Jaworzno', 'Aleja Tysiąclecia', '43-690', '9:00 - 18:00', '530990089')
l2 = Library('Katowice', 'Słoneczna', '45-555', '10:30 - 18:30', '531666124')


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Imię: {self.first_name}, Nazwisko: {self.last_name}, Data zatrudnienia: {self.hire_date}, Data urodzenia: {self.birth_date}, Miasto: {self.city} '\
                f'Ulica: {self.street}, Kod pocztowy: {self.zip_code}, Telefon kontaktowy: {self.phone}'


e1 = Employee('Mateusz', 'Drobny', '11.11.2011', '25.03.1950', 'Kraków', 'Gliniana', '46-551', '123456789')
e2 = Employee('Anna', 'Domagała', '25.04.2010', '17.03.1950', 'Jaworzno', 'Koszarowa', '54-125', '987654321')
e3 = Employee('Szymon', 'Duda', '11.01.2014', '11.09.2019', 'Warszawa', 'Kolorowa', '421-124', '888777666')


class Book:
    def __init__(self, library, author_name, author_surname, publication_date, number_of_pages):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'Autor: {self.author_name} {self.author_surname}, Data publikacji: {self.publication_date}, Liczba stron: {self.number_of_pages}, \nBiblioteka: {self.library}'


b1 = Book(l1, "Anna", "Królewska", "17.03.2005", 666)
b2 = Book(l2, "Stefan", "Czarny", "14.12.1995", 144)
b3 = Book(l1, "Michał", "Szpak", "24.10.1994", 900)
b4 = Book(l2, "Konrad", "Wallenrod", "30.12.2021", 555)
b5 = Book(l1, "Aleksandra", "Michniewicz", "01.01.2001", 430)

print(b1)

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f' Pracownik: {self.employee.__str__()}, Student: {self.student}, {self.books}, Data zamówienia: {self.order_date}'

o1 = Order(e2, "Krzysztof Kononowicz", [b3, b4], "17.03.2001")
o2 = Order(e1, "Przemysław Gęś", [b3, b2], "31.03.2010")
print(o1)
print(o2)

