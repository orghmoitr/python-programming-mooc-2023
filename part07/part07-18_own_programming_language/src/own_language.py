# Write your solution here

from string import ascii_uppercase

def initial_values(variables: dict):
    for letter in ascii_uppercase:
        variables[letter] = 0

def get_value(expression: str, variables: dict) -> int:
    if expression in ascii_uppercase:
        return variables[expression]
    else:
        return int(expression)

def run(program) -> list:
    prints = []
    variables = {}
    initial_values(variables)

    indices = []
    for i in range(len(program)):
        if ":" in program[i]:
            indices.append((i, program[i][:-1]))
    
    i = 0
    while i < len(program):
        expression = program[i].split(" ")
        command = expression[0]
        if command == "PRINT":
            value = expression[1]
            first = get_value(value, variables)
            try:
                prints.append(variables[first])
            except:
                prints.append(first)
        elif command == "MOV":
            first = expression[1]
            value = expression[2]
            second = get_value(value, variables)
            variables[first] = second
        elif command == "ADD":
            first = expression[1]
            value = expression[2]
            second = get_value(value, variables)
            variables[first] += second
        elif command == "SUB":
            first = expression[1]
            value = expression[2]
            second = get_value(value, variables)
            variables[first] -= second
        elif command == "MUL":
            first = expression[1]
            value = expression[2]
            second = get_value(value, variables)
            variables[first] *= second
        elif command == "END":
            break
        elif command == "IF":
            value = expression[1]
            first = str(get_value(value, variables))
            operator = expression[2]
            value = expression[3]
            second = str(get_value(value, variables))
            result = eval(first + operator + second)
            if result:
                action = expression[5]
                for index in indices:
                    if action == index[1]:
                        i = index[0]
                        break
        elif command == "JUMP":
            action = expression[1]
            for index in indices:
                if action == index[1]:
                    i = index[0]
                    break
        i += 1

    return prints

if __name__ == "__main__":
    program5 = []
    program5.append("PRINT A")
    program5.append("END")
    result = run(program5)
    print(result)
