import os
import sys


joyce = {
    'name': "Joyce",
    'quizzes': [90.0, 89.0, 88.9, 87.0, 86.5],
    'seatworks': [92.0, 89.0, 88.9, 97.0, 98.5],
    'exams': [94.0, 92.0, 98.9, 97.0, 96.5],
}

angel = {
    'name': "Angel",
    'quizzes': [96.0, 79.0, 78.9, 97.0, 90.5],
    'seatworks': [90.0, 89.0, 82.9, 94.0, 92.5],
    'exams': [95.0, 92.0, 97.9, 87.0, 94.5],
}

roger = {
    'name': "Roger",
    'quizzes': [76.0, 79.0, 78.9, 80.0, 72.5],
    'seatworks': [80.0, 79.0, 72.9, 69.0, 92.5],
    'exams': [75.0, 72.0, 77.9, 77.0, 74.5],
}

def gwa(student):
    total = 0
    for grades in student:
        quiz = sum(student['quizzes']) / len(student['quizzes'])
        seatwork = sum(student['seatworks']) /len(student['seatworks'])
        exam = sum(student['exams']) / len(student['exams'])

        gwa = 0.4 * quiz + 0.10 * seatwork + 0.5 * exam
        return gwa

def letterGrade(gwa):
    if gwa >= 90:
        return "Rating: A"
    elif gwa >= 80:
        return "Rating: B"
    elif gwa >= 70:
        return "Rating: C"
    elif gwa >= 60:
        return "Rating: D"
    elif gwa >= 50:
        return "Rating: E"
    else:
        return "Rating: F"

def printInfo(student):
    thegwa = gwa(student)
    print("Name: "+student['name'])
    print("Average: "+str(gwa(student)))
    print(letterGrade(thegwa))
    return print("---------------------------------------------")

printInfo(joyce)
printInfo(angel)
printInfo(roger)


