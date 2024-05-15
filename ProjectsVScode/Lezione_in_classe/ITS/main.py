from building import Building
from course import Course
from group import Group
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
course = Course(name="Python", building=b)
print(course)

cloud = Group(name="cloud", limit_students=5)
fullstack = Group(name="fullstack", limit_students=30)
course.groups[fullstack.name] = fullstack
course.groups[cloud.name] = cloud
# [fullstack, cloud]

student = Student(id="1234", cf="12334cjahdas", name="Bardh", surname="Bianchi", age=28)
walter = Student(id="353535", cf="3612378216bdsahgd", name="Walter", surname="Albano", age=33)
course.register(student)
course.register(walter, "fullstack")
#student.withdraw()
for _ in range(30):
    course.register(Student(id="353535", cf="3612378216bdsahgd", name="Walter", surname="Albano", age=33))

flavio = Professor(id="1234", degree="Informatica", cf="3213213", name="Flavio", surname="Giorgi", age=29)
bardh = Professor(id="1234", degree="Informatica", cf="3213213", name="Bardh", surname="Prenkaj", age=28)
marco = Professor(id="1234", degree="Informatica", cf="3213213", name="Marco", surname="Cascio", age=33)
toni = Professor(id="1234", degree="Informatica", cf="3213213", name="Toni", surname="Mancini", age=48)
cloud.add_professor(bardh)
fullstack.add_professor(flavio)
fullstack.add_professor(marco)
fullstack.add_professor(toni)

print(course)