# WRITE YOUR SOLUTION HERE:

class ExamResult:

    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
                f', grade2: {self.grade2}, grade3: {self.grade3}')

    def max_grade(self):
        if self.grade1 > self.grade2 and self.grade1 > self.grade3:
            return self.grade1
        elif self.grade2 > self.grade3:
            return self.grade2
        else:
            return self.grade3


def best_results(results: list):
    return [result.max_grade() for result in results]


if __name__ == "__main__":
    result1 = ExamResult("Peter", 5, 3, 4)
    result2 = ExamResult("Pippa", 3, 4, 1)
    result3 = ExamResult("Paul", 2, 1, 3)
    results = [result1, result2, result3]
    print(best_results(results))
