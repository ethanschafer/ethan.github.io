# Writing a class with methods

class student:
    def __init__ (self, theName, theGrade, theClass):
        self.name = theName
        self.grade = theGrade
        self.className = theClass
        
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName


student1 = student("Sarah", 12, "Math")
student2 = student("Tim", 11, "Comp Sci")

print ("Example class")
print student1.name
print student2.name
student1.setName("Ellen")
print student1.name



# Forgetting to use self.variable

class otherStudent:
    def __init__ (self, theName, theGrade, theClass):
        self.name = theName
        self.grade = theGrade
        self.className = theClass
        
    def getName(self):
        return self.name
    
    def setName(self, newName):
        name = newName


student3 = otherStudent("Amber", 12, "Math")
print ("\n\nExample setName without using self.name")
print student3.getName()
student3.setName("Victoria")
print student3.getName()

class Car:
    def __init__ (self, theWheel, theSeat, theEngine):
        self.wheel = theWheel
        self.seat = theSeat
        self.engine = theEngine

    def wheelType(self):
        return.wheel

    def seatType(self):
        return.type

toyota = Car("Corolla", 12, "yes"
print ("\n\nExample setName without using self.name")
print Car.wheelType()

