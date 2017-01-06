
#-----------------------Classes and Method --------------------------
#begins the student class
class Student:

#->indent the methods inside of a class
    #constructor to create a student
    def __init__(self, newName, newGrade, newGpa):
        #class variables
        self.name = newName
        self.grade = newGrade
        self.gpa = newGpa

    def setName( self, newName ):
        self.name = newName

    def getName(self):
        return self.name


#end the student class

#create some example students
student1 = Student("Bob", 11, 3.5)
student2 = Student("Sue", 12, 4.0)

print(   student1.getName()      )
print(   student2.getName()      )

student1.setName("Joe");

inputName = input ("Enter a new name")
student2.setName( inputName );

print(   student1.getName()      )
print(   student2.getName()      )

def areaOfACircle( rad ):
    area = rad *rad * 3.14
    return area

