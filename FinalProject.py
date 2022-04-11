# Linh Pham UH# 2027194
# Final Project part 1
# In this program, we are going to import data from multiple csv files and retrieve output files based on requirement
# We are going to utilize class and list as well as input and output of comma delimited csv file

import csv


# Create class with method and assign instance attributes for class
class Student:
    def __init__(self, student_id, major, first, last, gpa=0, graduation_date=None, disciplinary_action=None):
        self.id = student_id
        self.major = major
        self.first = first
        self.last = last
        self.gpa = gpa
        self.graduation_date = graduation_date
        self.disciplinary_action = disciplinary_action


def main():
    #  Define empty list to read data from all the csv files and add them to the list
    data = []

    # Read Students Major List file
    with open("StudentsMajorsList.csv", "r") as file:
        reader = csv.reader(file, delimeter=",")
        for each in reader:
            student_id = each[0]
            last = each[1]
            first = each[2]
            major = each[3]
            disciplinary_action = each[4]
            stu = Student(student_id=student_id, last=last, first=first, major=major,
                          disciplinary_action=disciplinary_action)
            # Read the file one by one and append the stu in the list data
            data.append(stu)

    #     Read Major
    with open("StudentsMajorsList.csv", "r") as file:
        reader = csv.reader(file, delimeter=",")
        for each in reader:
            student_id = each[0]
            major = each[3]
            for stu in data:
                if stu.id == student_id:
                    stu.major = major

    # Read GPA File
    with open("GPAList.csv", "r") as f:
        reader = csv.reader(f, delimeter=",")

        for each in reader:
            id_ = each[0]
            gpa = each[1]

            for student in data:
                if student.id == id_:
                    student.gpa = gpa

    # Read graduation date file
    with open("GraduationDatesList.csv", "r") as file_:
        reader = csv.reader(file_, delimeter=",")

        for each in reader:
            stu_id = each[0]
            graduation_date = each[1]

            for student_ in data:
                if student_.id == stu_id:
                    student_.graduation_date = graduation_date

    #  EXPORT SECTION
    #  Create a csv output file for entire student information from input files. Students are sorted by first name in
    #  alphabet. Each row contains of student id, major, first name, last name, gpa, graduation date, and disciplinary
    #  action.

    #  Sorting by last name alphabet
    def sorting_key(x):
        return x.first
    data.sort(key=sorting_key)

    #     EXPORT A CSV WITH ALL THE STUDENTS WITH DETAILS
    with open("FullRoster.csv", "w") as file:
        writer = csv.writer(file, delimiter=",")
        for each in data:
            row = [each.id, each.major, each.first, each.last, each.gpa, each.graduation_date, each.disciplinary_action]
            writer.writerow(row)

    #  Create a csv output file for majors. Each major gets its own file. Major is reflected in the name of file
    #  (ex: Computer Information Systems.csv, Computer Science.csv,..). Major sorted by student ID. Each row of the file
    #  contain student id, last name, first name, graduation date and disciplinary action.

    #  Get the difference of majors and types in a list
    major_list = []
    for each in data:
        major_list.append(each.major)      # Add major list to major

    # EXPORT FILES for EACH MAJOR
    def sorting_key(i):      # Sorting by student id
        return i.id
    data.sort(key=sorting_key)

    # Write each major files
    for each in major_list:
        filename = each + ".csv"
        print(filename)
        with open(filename, "w") as f:
            writer = csv.writer(f, delimiter=",")
            for item in data:
                if item.major == each:
                    row = [item.id, item.last, item.first, item.graduation_date, item.disciplinary_action]
                    writer.writerow(row)

    #  Create a csv output file for eligible for scholarship. Any student with gpa 3.8 and higher, without disciplinary
    #  action have not graduate is eligible for scholarship. Each row of the file contains student id, last name, first
    #  name, major and gpa sorted from highest to lowest.

    #  Sorting by highest gpa to lowest gpa with reserve is true
    def sorting_key(y):
        return y.gpa
    data.sort(key=sorting_key, reverse=True)

    with open("ScholarshipCandidates.csv", "w") as file_:
        writer = csv.writer(file_, delimiter=",")
        for each in data:
            #  Condition for scholarship student
            if float(each.gpa) > 3.8 and each.disciplinary_action != "Y":
                row = [each.id, each.last, each.first, each.major, each.gpa]
                writer.writerow(row)

    #  Create a csv output file for student with disciplinary action. Student is sorted by graduation date from oldest
    #  to most recent. Each row contains of student id, last name, first name, and graduation date.

    #  Sorted by graduation date
    def sorting_key(j):
        return j.graduation_date
    data.sort(key=sorting_key)

    with open("DisciplinedStudents.csv", "w") as file:
        writer = csv.writer(file, delimiter=",")
        for each in data:
            if each.disciplinary_action == "Y":    # Condition for disciplined student
                row = [each.id, each.last, each.first, each.graduation_date]
                writer.writerow(row)


if __name__ == "__main__":
    main()
