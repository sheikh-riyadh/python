# Here we are going to learn how to declear constructor in class using python:

class Student :

    # if we make a constructor first of all define def keyword and double underscore init double underscore then argument it's roles to make constructor example below:

    def __init__(self, name, email, department, roll, session):
        self.name= name
        self.email = email
        self.department = department
        self.roll = roll
        self.session = session



student_1 = Student("Anik","anik@gmail.com","Computer",350880,2016)
print(student_1.name)