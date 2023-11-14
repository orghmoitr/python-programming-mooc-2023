# tee ratkaisusi tänne

class Course:

    def __init__(self, course: str):
        self.__course = course
        self.__grade = 0
        self.__credits = 0

    def course(self):
        return self.__course

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def add_grade(self, grade: int):
        self.__grade = grade

    def add_credits(self, credits: int):
        self.__credits = credits


class CourseBook:

    def __init__(self):
        self.__courses = {}

    def add_course(self, course: str, grade: int, credits: int):
        if course not in self.__courses:
            self.__courses[course] = Course(course)
        if grade > self.__courses[course].grade():
            self.__courses[course].add_grade(grade)
        self.__courses[course].add_credits(credits)

    def get_course_data(self, course: str):
        if course not in self.__courses:
            return None
        grade = self.__courses[course].grade()
        credits = self.__courses[course].credits()
        return grade, credits

    def all_entries(self):
        return self.__courses

    def all_credits(self):
        total = 0
        for course in self.__courses:
            total += self.__courses[course].credits()
        return total

    def mean_grade(self):
        sum_grade = 0
        for course in self.__courses:
            sum_grade += self.__courses[course].grade()
        return sum_grade / len(self.__courses)


class CourseBookApplication:

    def __init__(self):
        self.__coursebook = CourseBook()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__coursebook.add_course(course, grade, credits)

    def get_course_data(self):
        course = input("course: ")
        try:
            grade, credits = self.__coursebook.get_course_data(course)
        except TypeError:
            print("no entry for this course")
            return
        print(f"{course} ({credits} cr) grade {grade}")
        return

    def grade_distribution(self):
        print("grade distribution")
        courses = self.__coursebook.all_entries()
        grades = []
        for course in courses:
            grades.append(courses[course].grade())
        count = 0
        for i in range(5, 0, -1):
            count += grades.count(i)
            if count > 0:
                print(f"{i}: {'x' * count}")
            else:
                print(f"{i}: ")
            count = 0
        return
    
    def statistics(self):
        total_courses = len(self.__coursebook.all_entries())
        total_credits = self.__coursebook.all_credits()
        print(f"{total_courses} completed courses, "
              f"a total of {total_credits} credits")
        print(f"mean {self.__coursebook.mean_grade():.1f}")
        self.grade_distribution()
        return


    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()


application = CourseBookApplication()
application.execute()

# coursebook = CourseBook()
# coursebook.add_course("ItP", 3, 5)
# coursebook.add_course("ItP", 5, 5)
# coursebook.add_course("ItP", 1, 5)
# print(coursebook.get_course_data("ItP"))
