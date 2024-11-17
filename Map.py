class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # def print_student(self):
    #     print (f"My name is {self.name} and I scored {self.score} in the exam")

students = [Student ("John",0.72), Student ("Yanbo", 1.0), Student ("Sara", 0.5)]

#for student in students:
    #print(f"{student.name}, {student.score}")

student_results = []

#or student in students:

    # if student.score >= 0.7:
    #     student_results.append(f"{student.name} passed")
    # else:
    #     student_results.append(f"{student.name} failed")


    #student_results.append(f"{student.name} passed") if student.score >=0.7 else student_results.append(f"{student.name} failed") #this line of code does the same as the code block above

#map(lambda student: student_results.append(f"{student.name} passed") if student.score >= 0.7 else student_results.append(f"{student.name} failed"), students) # this line doesn't yield the expected result

map_results = list(map(lambda student: f"{student.name} passed" if student.score >= 0.7 else f"{student.name} failed", students))

print(map_results)


# challenge
# use map to multiply all these numbers by 2

numbers = [1, 2, 3, 4, 5]

print(list(map(lambda num: num * 2, numbers)))
