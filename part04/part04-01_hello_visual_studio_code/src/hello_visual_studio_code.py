# Write your solution here

while True:
    editor = input("Editor: ")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif editor.lower() == "emacs" or editor.lower() == "vim" or editor.lower() == "atom":
        print("not good")
    else:
        print("awful")

