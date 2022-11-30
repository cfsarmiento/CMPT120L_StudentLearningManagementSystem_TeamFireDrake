'''
Title: Source Code Library
Author: Ethan Morton
Class: CMPT120L
Professor: Reza Sadeghi
Goal: This is a library for certain functions that will be used multiple times throughout the source code. This prevents repetition and redundancy.
Other Requirements: none.
'''
# calculates grades and updates the GUI
def CalculateCourseGrade(course):
    import os
    import csv
    mostRecentSemesterDirectory = GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)
    courseGrade = 0
    courseWeight = 0
    courseInfo = []
    with open("course"+course+".csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            courseInfo.append(row)
            if (i != 0):
                courseGrade += float(row[1]) * float(row[2])
                courseWeight += float(row[2])
    courseInfo[0][2] = "Grade: " + str(courseGrade / courseWeight)
    with open("course"+course+".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(courseInfo)
    CalculateSemesterGPA()

# calculates semester and cumulative GPA and updates the GUI
def CalculateSemesterGPA():
    import os
    import csv
    mostRecentSemesterDirectory = GetMostRecentSemesterDirectory()
    os.chdir(mostRecentSemesterDirectory)
    courseGrades = []
    courseCredits = []
    for courseFile in os.listdir(mostRecentSemesterDirectory):
        if (os.path.isfile(os.path.join(mostRecentSemesterDirectory,courseFile)) and courseFile != "semesterInfo.csv"):
            with open(courseFile, "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    courseGrades.append(float(row[2][row[2].rindex(" ")+1:]))
                    courseCredits.append(float(row[1][row[1].rindex(" ")+1:]))
                    break
    semesterGPA = 0
    for i, g in enumerate(courseGrades):
        semesterGPA += GradeToGPA(g) * courseCredits[i]
    semesterGPA /= sum(courseCredits)
    semesterInfo = []
    with open("semesterInfo.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            semesterInfo = row
            break
    semesterInfo[2] = "GPA: " + str(semesterGPA)
    semesterInfo.append("Total Course Credits: " + str(sum(courseCredits)))
    with open("semesterInfo.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(semesterInfo)
    CalculateCumulativeGPA()

def CalculateCumulativeGPA():
    import os
    import pathlib
    import csv
    mostRecentSemesterDirectory = GetMostRecentSemesterDirectory()
    os.chdir(pathlib.Path(mostRecentSemesterDirectory).parent)
    cumulativeGPA = 0
    cumulativeCredits = 0
    i = 0
    for semesterFolder in os.listdir(pathlib.Path(mostRecentSemesterDirectory).parent):
        if (os.path.isdir(os.path.join(pathlib.Path(mostRecentSemesterDirectory).parent,semesterFolder))):
            os.chdir(pathlib.Path(os.path.join(pathlib.Path(mostRecentSemesterDirectory).parent,semesterFolder)))
            with open("semesterInfo.csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    cumulativeGPA += float(row[2][row[2].rindex(" ")+1:])
                    cumulativeCredits += float(row[3][row[3].rindex(" ")+1:])
                    i += 1
                    break
    cumulativeGPA /= cumulativeCredits
    os.chdir(pathlib.Path(mostRecentSemesterDirectory).parent.parent)
    loginInfo = []
    with open("loginInfo.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            loginInfo.append(row[0])
            loginInfo.append(row[1])
            loginInfo.append("GPA: " + str(cumulativeGPA))
            break
    with open("loginInfo.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(loginInfo)

# converts a grade in 0-100 scale to GPA in 0-4 scale
def GradeToGPA(grade):
    gpa = 0
    if (grade >= 93):
        gpa=4.0
    elif(grade >= 90):
        gpa=3.7
    elif(grade >= 87):
        gpa=3.3
    elif (grade >= 83):
        gpa=3.0
    elif(grade >= 80):
        gpa=2.7
    elif(grade >= 77):
        gpa=2.3
    elif(grade >= 73):
        gpa=2.0
    elif(grade >= 70):
        gpa=1.7
    elif (grade >= 67):
        gpa=1.3
    elif(grade >= 65):
        gpa=1.0
    elif(grade < 65):
        gpa=0.0
    return gpa

def GetAccountDirectory():
    import os
    import csv
    import pathlib
    os.chdir(pathlib.Path(__file__).parent.resolve())
    accountFile = ""
    cumulativeGPA = 0
    with open("currentLogin.csv", "r", newline = "") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            accountFile = line[0]
            cumulativeGPA = line[1]
    os.chdir(os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile))
    #if not os.path.exists("Semesters"):
    #    os.makedirs("Semesters")
    return {"accountPath": accountFile,"cumulativeGPA": cumulativeGPA,"semestersPath": os.path.join(pathlib.Path(__file__).parent.parent, "Accounts", accountFile, "Semesters")}
    

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
    #if not os.path.exists("Semesters"):
    #    os.makedirs("Semesters")
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