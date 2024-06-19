class Room:
    
    def __init__(self, name: str, floor: int, num_seats: int):
        self.set_name(name)
        self.set_floor(floor)
        self.set_num_seats(num_seats)
        
    def set_name(self, name: str):
        self.name = name
    
    def set_floor(self, floor: int):
        self.floor = floor
        
    def set_num_seats(self, num_seats: int):
        self.num_seats = num_seats
        
    def get_name(self) -> str:
        return self.name
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_num_seats(self) -> int:
        return self.num_seats
    
    def __str__(self) -> str:
        return f'Room(name={self.get_name()}, floor={self.get_floor()}, num_seats={self.get_num_seats()})'