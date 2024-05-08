class Food:
    def __init__(self, name: str, price: float, description: str = None):
        self.name: str = name
        self.price: float = price
        self.description: str = description

    def __str__(self) -> str:
        return f'{self.name.capitalize()}(price={self.price}, descr={self.description})'

class Menu:
    def __init__(self, foods: list[Food] = []):
        self.foods:list[Food] = foods
    
    def addFood(self, food: Food):
        # food_name in self.foods
        count: int = 0
        for food_menu in self.foods:
            if food.name == food_menu.name:
                count += 1
                food_menu.price = food.price
        if count == 0:
            self.foods.append(food)

    def removeFood(self, food: Food):
        if food in self.foods:
            self.foods.remove(food)
    
    def getAvgPrice(self) -> float:
        total_sum: float = 0
        for food in self.foods:
            total_sum += food.price
        # divido per la lunghezza della lista foods
        avg_price: float = total_sum/ len(self.foods)
        return avg_price

    def __str__(self) -> str:
        repr: str = ""
        for food in self.foods:
            repr += food.__str__() + "\n"
        avg_price: float = self.getAvgPrice()
        repr += "_" * 30 + "\n"
        repr += f'Prezzo medio = {avg_price}'
        return repr
    

carbonara = Food(name="Carbonara", price=10.5, description="La carbonara è buona")
cacio_e_pepe = Food(name="cacio_e_pepe", price=15.48)
un_altra_carbonara = Food(name="Carbonara", price=10.5, description="La carbonara è buona")

menu = Menu()
menu.addFood(carbonara)
menu.addFood(cacio_e_pepe)
menu.addFood(un_altra_carbonara)
print(menu.__str__())