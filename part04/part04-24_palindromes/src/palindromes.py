# Write your solution here

def palindromes(string: str) -> bool:
    i = 0
    while i < len(string):
        if string[i] != string[len(string)-i-1]:
            return False
        i += 1
    return True

def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print(f"that wasn't a palindrome")

main()

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
