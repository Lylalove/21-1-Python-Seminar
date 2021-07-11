class Student:
    # class attribute
    univ_name = "연세대학교"

    def __init__(self, name, major, department, gpa, graduated):
        self.name = name # instance attribute
        self.major = major
        self.department = department
        self.gpa = gpa
        self.graduated = graduated

    def acquire_scholarship(self):
        if self.gpa > 3.5 :
            return True
        else : return False
