class student:
    school_name = "TTU"
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {student.school_name}")

    def has_passed(self):
        return self.grade >= 50