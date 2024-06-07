from abc import ABC, abstractmethod
from typing import List

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        """
        Inizializza gli attributi di base di una persona.
        """
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_role(self) -> str:
        """
        Metodo astratto che deve essere implementato dalle sottoclassi
        per restituire il ruolo della persona.
        """
        pass
    
    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa della persona.
        """
        return f"{self.get_role()}: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        """
        Inizializza gli attributi di uno studente, ereditando da Person.
        """
        super().__init__(name, age)
        self.student_id = student_id
        self.courses: list[Course] = []
    
    def get_role(self) -> str:
        """
        Restituisce il ruolo dello studente.
        """
        return "Student"
    
    def enroll(self, course: 'Course') -> None:
        """
        Iscrive lo studente a un corso.
        """
        self.courses.append(course)
    
    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa dello studente,
        inclusi i corsi a cui è iscritto.
        """
        courses_str = ", ".join([course.course_name for course in self.courses])
        return f"{super().__str__()}, Student ID: {self.student_id}, Enrolled in: {courses_str}"

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str, department: str) -> None:
        """
        Inizializza gli attributi di un professore, ereditando da Person.
        """
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses: list[Course] = []
    
    def get_role(self) -> str:
        """
        Restituisce il ruolo del professore.
        """
        return "Professor"
    
    def assign_to_course(self, course: 'Course') -> None:
        """
        Assegna il professore a un corso.
        """
        self.courses.append(course)
    
    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa del professore,
        inclusi i corsi che insegna.
        """
        courses_str = ", ".join([course.course_name for course in self.courses])
        return f"{super().__str__()}, Professor ID: {self.professor_id}, Department: {self.department}, Teaching: {courses_str}"

class Course:
    def __init__(self, course_name: str, course_code: str) -> None:
        """
        Inizializza gli attributi di un corso.
        """
        self.course_name = course_name
        self.course_code = course_code
        self.students: List[Student] = []
        self.professor: List[Professor] = None
    
    def add_student(self, student: Student) -> None:
        """
        Aggiunge uno studente al corso.
        """
        self.students.append(student)
    
    def set_professor(self, professor: Professor) -> None:
        """
        Assegna un professore al corso.
        """
        self.professor = professor
    
    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa del corso,
        inclusi gli studenti iscritti e il professore assegnato.
        """
        students_str = ", ".join([student.name for student in self.students])
        professor_str = self.professor.name if self.professor else "None"
        return f"Course: {self.course_name} ({self.course_code}), Professor: {professor_str}, Students: {students_str}"

class Department:
    def __init__(self, department_name: str) -> None:
        """
        Inizializza gli attributi di un dipartimento.
        """
        self.department_name = department_name
        self.courses: List[Course] = []
        self.professors: List[Professor] = []
    
    def add_course(self, course: Course) -> None:
        """
        Aggiunge un corso al dipartimento.
        """
        self.courses.append(course)
    
    def add_professor(self, professor: Professor) -> None:
        """
        Aggiunge un professore al dipartimento.
        """
        self.professors.append(professor)
    
    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa del dipartimento,
        inclusi i corsi e i professori.
        """
        courses_str = "\n  ".join([str(course) for course in self.courses])
        professors_str = "\n  ".join([str(professor) for professor in self.professors])
        return f"Department: {self.department_name}\nCourses:\n  {courses_str}\nProfessors:\n  {professors_str}"

class University:
    def __init__(self, name: str) -> None:
        """
        Inizializza gli attributi di un'università.
        """
        self.name = name
        self.departments: List[Department] = []
        self.students: List[Student] = []
    
    def add_department(self, department: Department) -> None:
        """
        Aggiunge un dipartimento all'università.
        """
        self.departments.append(department)
    
    def add_student(self, student: Student) -> None:
        """
        Aggiunge uno studente all'università.
        """
        self.students.append(student)
    
    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa dell'università,
        inclusi i dipartimenti e gli studenti.
        """
        departments_str = "\n\n".join([str(department) for department in self.departments])
        students_str = "\n  ".join([str(student) for student in self.students])
        return f"University: {self.name}\nDepartments:\n{departments_str}\nStudents:\n  {students_str}"

# Creazione di istanze di dipartimenti, corsi, professori e studenti
cs_department = Department("Computer Science")
math_department = Department("Mathematics")

cs101 = Course("Introduction to Computer Science", "CS101")
cs102 = Course("Data Structures", "CS102")
math101 = Course("Calculus I", "MATH101")

prof_smith = Professor("Dr. Smith", 45, "P1001", "Computer Science")
prof_johnson = Professor("Dr. Johnson", 50, "P1002", "Mathematics")

student_alice = Student("Alice", 20, "S2001")
student_bob = Student("Bob", 22, "S2002")

# Aggiunta di corsi e professori ai dipartimenti
cs_department.add_course(cs101)
cs_department.add_course(cs102)
cs_department.add_professor(prof_smith)

math_department.add_course(math101)
math_department.add_professor(prof_johnson)

# Creazione di un'università e aggiunta di dipartimenti e studenti
university = University("My University")
university.add_department(cs_department)
university.add_department(math_department)
university.add_student(student_alice)
university.add_student(student_bob)

# Iscrizione degli studenti ai corsi e assegnazione dei professori ai corsi
student_alice.enroll(cs101)
student_alice.enroll(math101)
student_bob.enroll(cs102)

cs101.add_student(student_alice)
cs102.add_student(student_bob)
math101.add_student(student_alice)

cs101.set_professor(prof_smith)
cs102.set_professor(prof_smith)
math101.set_professor(prof_johnson)

prof_smith.assign_to_course(cs101)
prof_smith.assign_to_course(cs102)
prof_johnson.assign_to_course(math101)

# Visualizzazione dello stato dell'università
print(university)
