class person :
    def __init__(self , name , yob):
        self.name = name 
        self.yob = yob 
    def describe(self) :
        pass 
class Student(person) :
    def __init__(self, name, yob , grade):
        super().__init__(name, yob)
        self.grade = grade 
    def describe(self):
        print ("student" , ' - ' , 'name: ' , self.name ,' - ' , 'yob: ' , self.yob , ' - ' , 'grade: ' , self.grade)
class Teacher(person) :
    def __init__(self, name, yob , subject):
        super().__init__(name, yob)
        self.subject = subject 
    def describe(self):
        print ("teacher" , ' - ' , 'name: ' , self.name ,' - ' , 'yob: ' , self.yob , ' - ' , 'subject: ' , self.subject) 
class Doctor(person) :
    def __init__(self, name, yob , specialist):
        super().__init__(name, yob) 
        self.specialist = specialist 
    def describe(self):
        print ("doctor" , ' - ' , 'name: ' , self.name ,' - ' , 'yob: ' , self.yob , ' - ' , 'specialist: ' , self.specialist)
class Ward :
    def __init__(self, name):
        self.name = name 
        self.people = [] 
    def addPerson (self , p : person) :
        self.people.append (p) 
    def describe (self) :
        for i in self.people :
            i.describe() 
    def countDoctor (self) :
        count = sum (1 for i in self.people if isinstance(i,Doctor))
        return count 
    def sortAge (self) :
        self.people.sort (key = lambda person : person.yob)
    def aveTeacherYearOfBirth (self) :
         arr = [person.yob for i in self.people if isinstance(i,Teacher)]
         ave = sum (arr) / len(arr) 
    
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1 . addPerson(doctor2)
ward1.describe()
ward1.sortAge() 
ward1.describe()