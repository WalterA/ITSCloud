from building import Building
from courses.java import JavaCourse
from courses.python import PythonCourse
from group import Group
from materials.python.basics import PythonBasics
from materials.python.classes import ClassesInPythonLesson
from person import Professor, Student
from room import Room

r = Room(name="213", floor=2, num_seats=30)
r1 = Room(name="312", floor=0, num_seats=12)
r2 = Room(name="612", floor=-28327317271372173218362187321683, num_seats=5)
print(r)
print("#" * 50)
b = Building(name="SMI", address="Via Sierra Nevada 60", floors=[-2,2])
print(len(b.get_rooms()))
add = b.add_room(r)
print(f'Add = {add} --> {r}')
add = b.add_room(r1)
print(f'Add = {add} --> {r1}')
add = b.add_room(r2)
print(f'Add = {add} --> {r2}')
remove = b.remove_room(r)
print(f'Remove = {remove} --> {r}')
print("#" * 70)

python_course = PythonCourse(name="Python", building=b)
java_course = JavaCourse(name="Java", max_age=48)

python_basics = PythonBasics()
classes_in_python = ClassesInPythonLesson(previous_lesson=python_basics)
for i in range(10):
    
    print("Ciao")
    
cloud = Group(name="cloud", limit_students=5)
fullstack = Group(name="fullstack", limit_students=30)
python_course.add_group(cloud)
python_course.add_group(fullstack)
fullstack.add_material(python_basics)
cloud.add_material(python_basics)
fullstack.add_material(classes_in_python)
# [fullstack, cloud]

student = Student(id="1234", cf="12334cjahdas", name="Bardh", surname="Bianchi", age=28)
walter = Student(id="353535", cf="3612378216bdsahgd", name="Walter", surname="Albano", age=33)
python_course.register_student(student)
python_course.register_student(walter)
#student.withdraw()
for _ in range(30):
    python_course.register_student(Student(id="353535", cf="3612378216bdsahgd", name="Walter", surname="Albano", age=33))

flavio = Professor(id="1234", degree="Informatica", cf="3213213", name="Flavio", surname="Giorgi", age=29)
bardh = Professor(id="1234", degree="Informatica", cf="3213213", name="Bardh", surname="Prenkaj", age=28)
marco = Professor(id="1234", degree="Informatica", cf="3213213", name="Marco", surname="Cascio", age=33)
toni = Professor(id="1234", degree="Informatica", cf="3213213", name="Toni", surname="Mancini", age=48)
cloud.add_professor(bardh)
fullstack.add_professor(flavio)
fullstack.add_professor(marco)
fullstack.add_professor(toni)

print(python_course)
common_subjects: set[str] = python_course.common_subjects(fullstack, cloud)
print(f'Le aree in comune sono\n{common_subjects}')
areas_in_cloud = python_course.difference_subjects(fullstack, cloud)
print(f'Le aree che solo Cloud impara sono\n{areas_in_cloud}')


i: int = 10

i = "ciao"


