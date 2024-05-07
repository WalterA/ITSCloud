# class persone:
#     def __init__(self, name , age, peso) -> None:
# #         self.name = name
# #         self.age = age
# #         self.peso = peso
# #         self.hobby={}
# #     def __str__(self) -> str:
# #         return f"persone(nome={self.name}, age={self.age},peso={self.peso})"
# #     def hobby(self, new_hobby):
# #             self.hobby.append(new_hobby)
# #             #self.hobby.add(new_honny)
# #     def remove_hobby (self, old_hobby):
# #          if old_hobby in self.hobby:
# #             self.hobby.remove(old_hobby)
# #     def bulk_set_hobby(self,new_hobbies):
# #         for hobby in new_hobbies:
# #             #self.hobby.append(hobby)
# #             self.hobby(hobby)
# #         # self.hobby=self.hobby.union(set([new_hobbies]))
    
# # alice = persone("alice", 45,342)
# # bob = persone("bob", 55,244)
# # alice.remove_hobby("palla")

# # if alice.age >= bob.age:
# #     print(f"è piu' vecchio {alice.name}")
# # else:
# #     print(f"è piu' vecchio {bob.name}")

# # gigi=persone("gigi",23, 343)
# # fabio=persone("fabio",98,432)

# # lista_persone=[alice,fabio,gigi, persone("claudio",45,423)]


# # min_age = float('inf')
# # index_min_age= 0
# # for i in range(len(lista_persone)):
# #     if lista_persone[i].age < min_age:
# #         min_age = lista_persone[i].age
# #         index_min_age=i
# # person=lista_persone[index_min_age]

# # print(f"{person}")


# class Student:
#     def __init__(self, name:str , studyProgram:str) -> None:
#         self.name = name.capitalize()
#         self.studyProgram = studyProgram.capitalize()
#         self.age = None
#         self.gender = None
#     def new_age (self,age:int, ):
#         self.age = age
        
#     def new_gender (self,gender:str):
#         self.gender = gender

#     def printInfo (self):
#         if self.age and self.gender:
#             return (f"{self.name},{self.studyProgram},{self.age},{self.gender}")
#         else:
#             if self.age:
#                 return(f"{self.name},{self.studyProgram},{self.age}")
#             elif self.gender:
#                 return(f"{self.name},{self.studyProgram},{self.gender}")
#             else:
#                 return (f"{self.name},{self.studyProgram}")
                  
# studente1 = Student ("walter","cloud")
# studente2 = Student ("davide","cloud")
# studente3 = Student ("francesca","cloud")
# studente1.new_age(33)

# print(f"A sinistra c'è {studente3.name}, a destra c'è {studente2.name}, io sono al centro {studente1.name}")


# print(studente1.name)

# print(studente1.printInfo())


# class Student:
#     student_gra=[]
#     def __init__(self, name,grade):
#         self.name= name
#         self.student_gra.append(grade)
#     @classmethod
#     def get_avg (cls):
#         avg = sum(cls.student_gra) / len(cls.student_gra)
#         return avg

# wa=Student("wa",4)
# fra=Student("fra",4)
# avg=Student.get_avg()
# print(avg)

# class Stundent:
#     def __init__(self, name):
#         self.name= name
#         self.mygrade=[]
#     def add(self,grade):
#         self.mygrade.append(grade)
#         self.student_grade
#     def gread_avg(self):
#          return sum(self.mygrade) / len(self.mugrade)
#     @classmethod
#     def get_avg (cls):
#         avg = sum(cls.student_gra) / len(cls.student_gra)
#         return avg

# Student.get_avg()

class animale:
    def __init__(self, animal,legs):
        self.name = animal
        self.legs = legs
    def setLeg(self,x):
        self.legs += x

    def getLegs(self):
        return self.legs
    def printInfo (self):
         if self.name and self.legs:
            return (f"{self.name},{self.legs}")
animale1=animale("ugo",4)
print(animale1.name)
print(animale1.legs)
animale1.setLeg(-2)
print(animale1.legs)
