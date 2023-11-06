# Write your solution here

def read_input(prompt: str, lower_bound: int, upper_bound: int) -> int:
    while True:
        try:
            number = int(input(prompt))
            if number < lower_bound or number > upper_bound:
                print(f"You must type in an integer between {lower_bound} and {upper_bound}")
                continue
            return number
        except ValueError:
            print(f"You must type in an integer between {lower_bound} and {upper_bound}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
