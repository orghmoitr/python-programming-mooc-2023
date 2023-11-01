# Write your solution here

passwd = input("Password: ")

while True:
    repasswd = input("Repeat password: ")
    if passwd == repasswd:
        break
    print("They do not match!")
print("User account created!")
