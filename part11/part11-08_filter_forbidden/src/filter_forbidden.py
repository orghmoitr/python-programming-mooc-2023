# WRITE YOUR SOLUTION HERE:

def filter_forbidden(string: str, forbidden: str):
    return "".join([c for c in string if c not in forbidden])


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)
