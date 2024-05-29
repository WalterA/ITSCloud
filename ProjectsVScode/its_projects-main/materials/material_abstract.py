from abc import ABC, abstractmethod

from person import Student

class AbstractLesson(ABC):
    
    def __init__(self, 
                 name: str,
                 subjects: list[str],
                 duration: float,
                 difficulty: int):
        super().__init__()
        self.name: str = name
        self.subjects: list[str] = subjects
        self.duration: float = duration
        self.difficuly: int = difficulty
        
    @abstractmethod
    def grade_student(self, student: Student) -> float:
        pass
    
    def __str__(self) -> str:
        return f'Lesson(name={self.name}, subjects={self.subjects},'\
            +f' duration={self.duration}, difficulty={self.difficuly})'