# Write your solution here

def read_entries():
    with open("diary.txt", "r") as my_file:
        entries = []
        for line in my_file:
            entries.append(line.strip())
        print("Entries:")
        for entry in entries:
            print(entry)
    

def add_entry():
    entry = input("Diary entry: ")
    with open("diary.txt", "a") as my_file:
        my_file.write(f"{entry}\n")
    print("Diary saved")
    print()


def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        command = int(input("Function: "))
        if command == 0:
            print("Bye now!")
            break
        if command == 1:
            add_entry()
        if command == 2:
            read_entries()


main()

