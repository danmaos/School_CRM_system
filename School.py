class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Human):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

class Student(Human):
    def __init__(self, name, age, group, address):
        super().__init__(name, age)
        self.group = group
        self.address = address


def new_person():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    while True:
        if age.isdigit():
            age = int(age)
            break
        age = input("Enter your age in digits: ")
    return [name, age]

def teacher_registration():
    subject = input("Enter your subject: ")
    experience = input("Enter your experience in years: ")
    while True:
        if experience.isdigit():
            experience = int(experience)
            break
        experience = input("Enter your age in digits: ")
    return [subject, experience]

def student_registration():
    group = input("Enter your study group: ")
    address = input("Enter your home address: ")
    return [group, address]

def main():
    position = input("Are you teacher or student?: ").capitalize()
    while True:
        if position == "Teacher" or position == "Student":
            break
        position = input("Enter only teacher or student?: ").capitalize()
    person_info = new_person()
    if position == "Teacher":
        person_info += teacher_registration()
    return person_info

print(main())




