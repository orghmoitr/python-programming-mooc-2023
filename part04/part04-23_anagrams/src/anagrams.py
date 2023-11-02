# Write your solution here

def anagrams(string1, string2) -> bool:
    list1 = sorted(string1)
    list2 = sorted(string2)
    return list1 == list2

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
