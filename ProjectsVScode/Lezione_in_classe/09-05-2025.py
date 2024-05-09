class person():
class dipendente(person):
    def __init__(self) -> None:
        super().__init__()
        self.ore=100
        self.paga=10
    def calcolastipendio(self):
        return self.ore * self.paga