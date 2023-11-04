# Write your solution here

def filter_solutions():
    with open("solutions.csv") as solutions_file:
        correct_solutions = []
        incorrect_solutions = []
        for line in solutions_file:
            line = line.strip()
            parts = line.split(";")
            if eval(parts[1]) == int(parts[2]):
                correct_solutions.append(line)
            else:
                incorrect_solutions.append(line)
        with open("correct.csv", "w") as correct_file:
            for solution in correct_solutions:
                correct_file.write(solution+"\n")
        with open("incorrect.csv", "w") as incorrect_file:
            for solution in incorrect_solutions:
                incorrect_file.write(solution+"\n")
                
