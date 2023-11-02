# Write your solution here

def first_word(sentence):
    return sentence[0:sentence.find(" ")]

def second_word(sentence):
    i = sentence.find(" ")
    j = sentence.find(" ", i+1)
    if j != -1:
        return sentence[i+1:sentence.find(" ", i+1)]
    else:
        return sentence[i+1:]

def last_word(sentence):
    index1 = -1
    i = 0
    while i < len(sentence):
        index2 = sentence.find(" ", i)
        if index2 != -1:
            index1 = index2
        i += 1
    return sentence[index1+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was"

    print(second_word(sentence)) # was
    print(last_word(sentence)) # was
