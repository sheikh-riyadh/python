class Family:
    def __init__(self, father,mother):
        self.father = father
        self.mother = mother

    def show_details(self, *args):
        for value in args:
            print(value)

class School:
    def __init__(self, roll, name):
        self.name = name
        self.roll = roll


class Sports:
    def __init__(self, game ):
        self.game = game



class Student(Family, School, Sports):
    def __init__(self, name, roll, father, mother, game):
        Family.__init__(self, father, mother)
        School.__init__(self,roll,name)
        Sports.__init__(self, game)
        Family.show_details(self,name,roll,father,mother,game)
    





st1 = Student("Sheikh muhammad riyadh hasan", 350883, "Abbas ali", "Hasida begum","Footbal")
# print(st1.name)


st2 = Student("Akram gazi", 350883, "Shopon gazi", "Monzu","Cricket")
st2.show_details()