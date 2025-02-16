class Student:
    def __init__(self, name, class_name, id):
        self.name=name
        self.class_name = class_name
        self.id=id
    


class Teacher:
    def __init__(self, name, subject, id):
        self.name=name
        self.subject = subject
        self.id = id
        


class School:
    def __init__(self,name):
        self.name=name
        self.teachers = []
        self.students = []
    

    def add_teacher(self, name, subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
    

    def add_student(self, name, class_name, id):
        id = len(self.students)+1
        student = Student(name,class_name,id)
        self.students.append(student)

        