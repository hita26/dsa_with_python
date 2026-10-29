class Student:
    def __init__(self):
        self.name = ""
        self.rno = 0
        self.div = ""
        self.program = ""

    def get(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter Roll No: "))
        self.div = input("Enter Division: ")
        self.program = input("Enter Program: ")

    def put(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Division:", self.div)
        print("Program:", self.program)


student1 = Student()

student1.get()
student1.put()
