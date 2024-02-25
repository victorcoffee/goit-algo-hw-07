# Модуль 6

import os, re
from collections import UserDict

os.system("cls")


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    # Перевірка номера на коректність - 10 цифр
    def __init__(self, value):
        pattern = r"\d{10}"
        match = re.search(pattern, str(value))
        if match:
            super().__init__(value)
        else:
            print(f"Invalid number, must be 10 digits")
            raise Exception("Invalid number")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Додавання телефону до контакту
    def add_phone(self, phone: Phone):
        phone = Phone(phone)
        self.phones.append(phone)
        print(f"Number {phone} added for {self.name.value}")

    # Видалення телефону до контакту
    def remove_phone(self, phone: Phone):
        phone = Phone(phone)
        for index in range(len(self.phones)):
            if phone.value == self.phones[index].value:
                print(f"Number {phone.value} deleted for {self.name.value}")
                del self.phones[index]
                return
        else:
            print(f"Phone {phone.value} not found - remove_phone")

    # Редагування телефону для контакту
    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        for index in range(len(self.phones)):
            if old_phone.value == self.phones[index].value:
                self.phones[index] = new_phone
                print(f"Number {new_phone.value} updated for {self.name.value}")
                return
        else:
            print(f"Phone {old_phone.value} not found - edit_phone")

    # Пошук телефону у контакта
    def find_phone(self, phone: Phone):
        phone = Phone(phone)
        for item in self.phones:
            if phone.value == item.value:
                print(f"Phone {phone.value} found")
                return f"{self.name.value}: {phone.value}"
        else:
            print(f"Phone {phone.value} not found - find_phone")

    # Формат виведення контакту
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    book = UserDict()

    # Додавання контакту до книги
    def add_record(self, record: Record):
        self.data[record.name] = record

    # Пошук контакту
    def find(self, name: Name) -> Record:
        for key, value in self.data.items():
            if key.value == name:
                print(f"Contact {name} found")
                return self.data[key]
        print(f"Contact {name} not found")
        return

    # Видалення контакту з книги
    def delete(self, name: Name):
        for key, value in self.data.items():
            if key.value == name:
                print(f"{self.data[key]} deleted")
                del self.data[key]
                break
        else:
            print("Contact {name} is absent")


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print("john:", john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"Found phone: {found_phone}")

    # Видалення телефону
    john.remove_phone("5555555555")
    print(john)

    # Спроба видалення неіснуючого телефону
    john.remove_phone("5555555555")
    print(john)

    # Видалення запису Jane
    book.delete("Jane")

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    print("The program is completed")


if __name__ == "__main__":
    main()
