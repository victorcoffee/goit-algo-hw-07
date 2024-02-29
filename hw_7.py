# Модуль 6

import os, re, datetime
from collections import UserDict

os.system("cls")


# Декоратор обробляє винятки, що виникають у функціях - handler
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Enter the argument for the command"

    return inner


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
            print("Invalid number, must be 10 digits")
            raise Exception("Invalid number")


class Birthday(Field):
    def __init__(self, value):
        try:
            # Перевірка коректності дати
            value = datetime.datetime.strptime(value, "%d.%m.%Y")
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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
                return f"Number {new_phone.value} updated for {self.name.value}"
        else:
            return f"Phone {old_phone.value} not found - edit_phone"

    # Пошук телефону у контакта
    def find_phone(self, phone: Phone):
        phone = Phone(phone)
        for item in self.phones:
            if phone.value == item.value:
                print(f"Phone {phone.value} found")
                return f"{self.name.value}: {phone.value}"
        else:
            print(f"Phone {phone.value} not found - find_phone")

    # Додавання дня народження до контакту
    def add_birthday(self, date: str):
        try:
            birthday = Birthday(date)
            self.birthday = birthday
            print(f"Birthday {date} added for contact {self.name.value}")
        except Exception as e:
            print("Invalid date format. Use DD.MM.YYYY")

    # Формат виведення контакту
    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday:
            result += "; birthday: " + self.birthday.value.strftime("%d.%m.%Y")
        return result


class AddressBook(UserDict):
    book = UserDict()

    # Додавання контакту до книги
    def add_record(self, record: Record):
        self.data[record.name] = record

    # Пошук контакту
    def find(self, name: Name) -> Record:
        for key, value in self.data.items():
            if key.value == name:
                print(f"Contact {name} found")  # відключити ?
                return self.data[key]
        print(f"Contact {name} not found")  # відключити ?
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

    # Функція повертає список іменинників на найближчі 7 днів
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.datetime.today().date()
        end_week = today + datetime.timedelta(days=7)

        for key, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = datetime.date(
                    today.year, birthday.month, birthday.day
                )

                # Якщо день народження вже був у цьому році, визначаємо наступний
                if birthday_this_year < today:
                    birthday_next_year = datetime.date(
                        today.year + 1, birthday.month, birthday.day
                    )
                    nearest_birthday = birthday_next_year
                else:
                    nearest_birthday = birthday_this_year

                # Перенесення привітання з вихідних  на понеділок
                if nearest_birthday.weekday() == 5:
                    congratulation_date = nearest_birthday + datetime.timedelta(days=2)
                elif nearest_birthday.weekday() == 6:
                    congratulation_date = nearest_birthday + datetime.timedelta(days=1)
                else:
                    congratulation_date = nearest_birthday

                # Якщо день народження у найближчі 7 днів, то додаємо у список
                if today <= nearest_birthday < end_week:
                    person_to_congratulate = {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                    print(
                        record.name, birthday, birthday_this_year, congratulation_date
                    )
                    upcoming_birthdays.append(person_to_congratulate)

        return upcoming_birthdays

    @input_error
    def add_birthday(args, book):
        # реалізація
        pass

    @input_error
    def show_birthday(args, book):
        # реалізація
        pass

    @input_error
    def birthdays(args, book):
        # реалізація
        pass


"""
def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("29.02.2004")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("02.03.2003")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Список привітань на цьому тижні
    upcoming_birthdays = book.get_upcoming_birthdays()
    print("Список привітань на цьому тижні:", upcoming_birthdays)



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
"""


# Парсер команд з 5.4
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Додавання контакту. Зразок із ТЗ
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


# Зміна контакту. Адаптація з 5.4
@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if record:
        message = record.edit_phone(old_phone, new_phone)
        return message
    else:
        return "Contact was not updated"


#  Виведення всіх контаків
@input_error
def show_all(book: AddressBook):
    for name, record in book.data.items():
        message = f"{name}"
        for phone in record.phones:
            message += f", {str(phone.value)}"
        # if record.birtday:
        #     message += f"{record.birthday}"
        print(message)

    return "All list of contacts printed."


# Зразок із ТЗ
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            # реалізація
            pass

        elif command == "all":
            # реалізація
            show_all(book)
            pass

        elif command == "add-birthday":
            # реалізація
            pass

        elif command == "show-birthday":
            # реалізація
            pass

        elif command == "birthdays":
            # реалізація
            pass

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
