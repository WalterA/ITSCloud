class Film:
    def __init__(self, id, title):
        self.__id = id
        self.__title = title
    
    def setID(self, id):
        self.__id = id
    
    def setTitle(self, title):
        self.__title = title
    
    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def isEqual(self, otherFilm):
        return self.__id == otherFilm.getID()



# class Film:
#     def __init__(self, id, title) -> None:
#         self.id = id
#         self.title = title
#     def setID(self,id):
#         self.id = id
#     def setTitle(self, title):
#         self.title = title
#     def getID(self):
#         return self.id
#     def getTitle(self):
#         return self.title
#     def isEqual(self,otherFilm):
#         while otherFilm == self.getID():
#             return True

# hotel = Film(123,"gigi")
# hotel.setID(456)
# hotel.setTitle("fefe")
# print(hotel.getID())
# print(hotel.getTitle())
# print(hotel.isEqual(456))
            
        