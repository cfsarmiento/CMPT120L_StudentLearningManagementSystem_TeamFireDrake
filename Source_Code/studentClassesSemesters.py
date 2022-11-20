
assignments = {}  # empty dict to save all assignments by class
class studentClasses:
    '''Defines student classes as an object for management'''
    def __init__(self, abrv_level,
                 homework=False, tests=False, projects=False, papers=False, quizzes=False,
                 oneCredit=False,threeCredits=False, fourCredits=False,
                 assign_name='none', grade=0):

        self.abrv_level = abrv_level  # Abbreviation & Level (Ex. CMPTL 120)

        # Assignment Types
        self.homework = homework
        self.tests = tests
        self.projects = projects
        self.papers = papers
        self.quizzes = quizzes

        # Credit for Class (only one should be true)
        self.oneCredit = oneCredit
        self.threeCredits = threeCredits
        self.fourCredits = fourCredits

        # Assignment Input Info
        self.assign_name = assign_name
        self.grade = grade

    assignments[self.abrv_level] = {}  # assignments by class

    # Name for The Object
    def __str__(self):
        return f'{self.abrv_level}'

    # Weights for Each Assignment
    def getWeights(self, homework, tests, projects, papers, quizzes):
        assign_types = {'homework': self.homework, # dict of all assignment types (T & F)
                        'tests': self.tests,
                        'projects': self.projects,
                        'papers': self.papers,
                        'quizzes': self.quizzes}

        for token in assign_types:  # for each assign type s
            if assign_types[token] == True:  # if the assignment type is selected
                assignments[self.abrv_level][token] = {}  # each assignment type gets its own dict within class

                # FIXME: figure out weight input


    # Add Assignments - FIXME
    def addAssignments(self, assign_name, grade, assign_type):  # assign_type = selected type to add assignment
        assign_type.lower()
        assign_types = {'homework': self.homework,  # dict of all assignment types (T & F)
                        'tests': self.tests,
                        'projects': self.projects,
                        'papers': self.papers,
                        'quizzes': self.quizzes}

        for token in assign_types:
            if assign_type == token:  # checks which assignment type
                assignments[self.abrv_level][assign_type][assign_name] = grade
                break

    # Edit Assignments - FIXME
    def editAssignments(self, assign_name, grade, assign_type):
        assign_type.lower()  # insures input is lowercase
        assign_types = {'homework': self.homework,  # dict of all assignment types (T & F)
                        'tests': self.tests,
                        'projects': self.projects,
                        'papers': self.papers,
                        'quizzes': self.quizzes}

        try:
            for token in assign_types:
                if assign_type == token:  # checks which assignment type
                    if assignments[self.abrv_level][assign_type][assign_name] in assignments:  # if entry exists
                        assignments[self.abrv_level][assign_type][assign_name] = grade  # edits entry
                        break
                    else:
                        raise ValueError

        except ValueError:
            # FIXME: prompt user that input was invalid
            pass

    # Remove Assignments - FIXME
    def removeAssignments(self, assign_name, assign_type):
        assign_type.lower()  # insures input is lowercase
        assign_types = {'homework': self.homework,  # dict of all assignment types (T & F)
                        'tests': self.tests,
                        'projects': self.projects,
                        'papers': self.papers,
                        'quizzes': self.quizzes}

        try:
            for token in assign_types:
                if assign_type == token:  # checks which assignment type
                    if assignments[self.abrv_level][assign_type][assign_name] in assignments:  # if entry exists
                        del assignments[self.abrv_level][assign_type][assign_name]  # deletes entry
                        break
                    else:
                        raise ValueError

        except ValueError:
            # FIXME: prompt user that input was invalid
            pass


    # Calculate Class GPA - FIXME - get weights first
    def classGPA(self):
        assign_types = {'homework': self.homework,  # dict of all assignment types (T & F)
                        'tests': self.tests,
                        'projects': self.projects,
                        'papers': self.papers,
                        'quizzes': self.quizzes}

        assignment_grades = {}
        for token in assign_types:
            for grade in assignments[self.abrv_level][token]:
                # save entries as assignment_type: grade for those assignments

                pass

    # Drop & Withdrawl - FIXME
    def dropWithdrawal(self):
        pass

    # Write Info to CSV - FIXME
    with open('assignments.csv', 'a', 'newline') as file:
        csvWriter = csv.writer(file)
        pass

semesters = {  # Keeps track of semester, by year
    sessions: {},  # year: session (2022: 'Fall')
    classes: {},
    gpa: {}
}

class studentSemester(studentClasses):
'''Class to Save Classes to Semesters'''
    def __init(self, abrv_level, year, session):
        __init__(self, abrv_level)
        self.year = year
        self.session = session


    def semesterClasses(self):
        pass

    def semesterGPA(self):
        pass

    def accumulativeGPA(self):
        pass

    def finalizeSemester(self):
        pass

    def addPastGPA(self):
        pass

    # Write Info to CSV - FIXME
    with open('assignments.csv', 'a', 'newline') as file:
        csvWriter = csv.writer(file)
        pass


