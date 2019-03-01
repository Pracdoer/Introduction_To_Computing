## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(total_marks):
    if round(total_marks) >= 90:
        return "A+"
    if round(total_marks) >= 86:
        return "A"
    if round(total_marks) >= 82:
        return "A-"
    if round(total_marks) >= 78:
        return "B+"
    if round(total_marks) >= 74:
        return "B"
    if round(total_marks) >= 70:
        return "B-"
    if round(total_marks) >= 66:
        return "C+"
    if round(total_marks) >= 62:
        return "C"
    if round(total_marks) >= 58:
        return "C-"
    if round(total_marks) >= 54:
        return "D+"
    if round(total_marks) >= 50:
        return "D"
    if round(total_marks) <50:
        return "F"

#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def f(x):
    if  x == ("A+"):
        return 4.00
    if x == ("A"):
        return 4.00
    if x ==("A-"):
        return 3.67
    if x == ("B+"):
        return 3.33
    if x == ("B"):
        return 3.00
    if x == ("B-"):
        return 2.67
    if x == ("C+"):
        return 2.33
    if x == ("C"):
        return 2.00
    if x == ("C-"):
        return 1.67
    if x == ("D+"):
        return 1.33
    if x == ("D"):
        return 1.00
    if x == ("F"):
        return 0.00


def calculate_sgpa(grade1,grade2,grade3):
    total_marks = 0
    total_number_of_subjects = 0
    if grade1 != 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + f(grade1)
    if grade2 != 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + f(grade2)
    if grade3 != 'nothing':
        total_number_of_subjects = total_number_of_subjects + 1
        total_marks = total_marks + f(grade3)
    if total_number_of_subjects ==0:
        return 0
    else:
        SGPA = (total_marks / total_number_of_subjects)
        return SGPA



#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
