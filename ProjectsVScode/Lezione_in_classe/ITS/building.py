from room import room
class building:
    def __init__(self, name,address,floors: tuple[int,int]) -> None:
        self.name =name
        self.address=address
        self.floor=floors
        self.room=[]
        def get_name(self):
            return self.name
        def get_address(self):
            return self.address
        
        def add_room(self,room:room):
            lower,upper = self.get_floors()
            
            if room not in self.get_room() and lower <= self.get_floors():
                self.rooms.append(room)
                return True
            else:
                return False
        def __str__(self):
            s:str =f"building(name={self.get_name()},address={self.get_address()},floor={self.get_floors()})"
            s += "\n With rooms:\n"
            for room in self.get_rooms():
                s+=room.__str__() + "\n"
            return room[:-1]
                