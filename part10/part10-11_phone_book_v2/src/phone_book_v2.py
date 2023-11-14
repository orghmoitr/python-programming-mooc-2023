# Write your solution here:

class PhoneBook:

    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name].numbers(), self.__persons[name].address()

    def all_entries(self):
        return self.__persons


class PhoneBookApplication:

    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        try:
            numbers, address = self.__phonebook.get_entry(name)
        except TypeError:
            print("address unknown")
            print("number unknown")
            return
        numbers_found = False
        address_found = False
        if len(numbers) > 0:
            numbers_found = True
            for number in numbers:
                print(number)
        elif not numbers_found:
            print("number unknown")
        if address is not None:
            address_found = True
            print(address)
        elif not address_found:
            print("address unknown")
        return


    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


class Person:

    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = ""

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        if self.__address == "":
            return None
        return self.__address

    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address = address


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# phonebook.add_address("Eric", "Linnankatu 75, Turku")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))
