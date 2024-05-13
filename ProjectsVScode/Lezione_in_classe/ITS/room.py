class room:
    def __init__(self, name:str,floor:int,num_steats:int) -> None:
        pass
    def set_name(self,name:str):
        self.name = name
    def set_floor(self,floor:int):
        self.floor = floor
    def set_num_steats(self, num_steats:int):
        self.num_steats = num_steats
        
    def get_name(self)->str:
        return self.name
    def get_floor(self)->int:
        return self.floor
    def get_num_steats (self)->int:
        return self.num_steats
    
    #def __str__(self) -> str:
        