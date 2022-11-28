'''
Title: Source Code Library
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: This is a library for certain functions that will be used multiple times throughout the source code. This prevents repetition and redundancy.
Other Requirements: none.
'''
# calculates grades, GPA, and updates the GUI
def CalculateCourseGrade():
    import os
    import pathlib
    import csv
    # this will be called in add/edit/removeAssignment.py where indicated by the #comment
    # this function may need to take an argument to get the name of the course
    # 1)
    # reads through course___.csv of this course and calculates the course grade
    # writes this course grade back into course___.csv
    # 2)
    # reads through course___.csv of all courses in this semester and calculates semester GPA
    # writes semester GPA in semesterInfo.csv in this semester
    # 3)
    # reads through semesterInfo.csv of all semesters and calculates cumulative GPA
    # writes the cumulative GPA in the mainPage.py

# returns the directory of the most recent semester
def GetMostRecentSemesterDirectory():
    import os
    import pathlib
    import csv
    os.chdir(pathlib.Path(__file__).parent.resolve())
    accountFile = ""
    with open("currentLogin.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            accountFile = line[0]
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters"))
    mostRecentSemesterFile = ""
    mostRecentYear = 0
    mostRecentSession = 0
    for semester in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), semester)):
            year = int(semester[semester.index("_")+1:semester.rindex("_")])
            session = 0
            match semester[semester.rindex("_")+1:].lower():
                case "fall":
                    session = 1
                case "autumn":
                    session = 1
                case "winter":
                    session = 2
                case "spring":
                    session = 3
                case "summer":
                    session = 4
            if (year > mostRecentYear):
                mostRecentYear = year
                mostRecentSemesterFile = semester
            elif (year == mostRecentYear):
                if (session > mostRecentSession):
                    mostRecentSession = session
                    mostRecentSemesterFile = semester
    return os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters", mostRecentSemesterFile)
