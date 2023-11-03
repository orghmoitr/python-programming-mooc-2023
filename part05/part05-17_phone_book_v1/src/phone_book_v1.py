# Write your solution here


def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break
        if command == 2:
            name = input("name: ")
            number = input("number: ")
            phonebook[name] = number
            print("ok!")
        if command == 1:
            name = input("name: ")
            found = False
            for person in phonebook:
                if person == name:
                    found = True
                    print(f"{phonebook[person]}")
            if not found:
                print("no number")

    
main()

