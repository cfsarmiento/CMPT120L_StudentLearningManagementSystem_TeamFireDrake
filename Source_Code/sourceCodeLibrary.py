'''
'''
def CalculateCourseGrade():
    # to be called in add/edit/remove Assignment.py where indicated by a #comment

    # reads through course___.csv of this course and calculates the course grade
    # writes this course grade back into course___.csv
    
    # reads through course___.csv of all courses and calculates semester GPA
    # writes semester GPA in semesterInfo.csv in this semester

    # reads through semesterInfo.csv of all semesters and calculates cumulative GPA
    # writes the cumulative GPA on the main page
    pass

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
    semesters = os.listdir(os.getcwd())
    mostRecentSemesterFile = ""
    mostRecentYear = 0
    mostRecentSession = 0
    for semester in semesters:
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