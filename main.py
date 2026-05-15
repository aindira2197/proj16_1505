class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def info(self):
        print(self.name)
        print(self.subject)

teachers = []

teachers.append(Teacher("Ali", "Python"))
teachers.append(Teacher("Vali", "Math"))
teachers.append(Teacher("Sami", "Physics"))

for teacher in teachers:
    teacher.info()
    print("------")
