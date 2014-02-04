lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students=[lloyd,alice,tyler]

# Add your function below!
def average(lst):
    return float(sum(lst))/len(lst)

def get_average(student):
    hmwrk=0.1
    qz=0.3
    tst=0.6
    score=average(student["homework"])*hmwrk+average(student["quizzes"])*qz+average(student["tests"])*tst
    return score

def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80 and score<90:
        return "B"
    elif score>=70 and score<80:
        return "C"
    elif score>=60 and score<70:
        return "D"
    else:
        return "F"

print get_letter_grade(get_average(lloyd))

def get_class_average(classlist):
    av=0
    for i in classlist:
        av=av+get_average(i)
    return float(av)/len(classlist)

print get_class_average(students)
print get_letter_grade(get_class_average(students))
