class Roster:
    def __init__(self):
        self.roster = []

    def add(self,person):
        self.roster.append(person)

    def size(self):
        return len(self.roster)

    def remove(self,person):
        self.roster.remove(person)

    def getPerson(self,name):
        for person in self.roster:
            if person.name == name:
                return person
        return None
    
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def setAge(self,n):
        self.age = n

    def getName(self):
        return self.name

    
class Student(Person):

    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def getGrade(self):
        return self.grade

    def changeGrade(self,n):
        self.grade = n

class Staff(Person):

    def __init__(self,name,age,position):
        super().__init__(name,age)
        self.position = position

    def getPosition(self):
        return self.position

    def changePositon(self,position):
        self.position = positions

roster = Roster()
person = Person("a",1)
student = Student("b",2,100)
staff = Staff("c",3,"TA")
roster.add(person)
roster.add(student)
roster.add(staff)
print(roster.getPerson("a").getAge())