# Write your solution here


def find_names(phonebook):
    name = input("name: ")
    found = False
    for person in phonebook:
        if person == name:
            found = True
    if found:
        for number in phonebook[name]:
            print(number)
    else:
        print("no number")

        
def add_names(phonebook):
    name = input("name: ")
    number = input("number: ")
    if name not in phonebook:
        phonebook[name] = [number]
    else:
        phonebook[name].append(number)
    print("ok!")

    
def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break
        if command == 2:
            add_names(phonebook)
        if command == 1:
            find_names(phonebook)

    
main()

