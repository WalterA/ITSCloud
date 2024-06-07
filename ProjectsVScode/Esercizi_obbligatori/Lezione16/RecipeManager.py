class RecipeManager:
    def __init__(self):
        
        self.dizionario = {}
    def create_recipe(self,name, ingredients:list):
        """Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
        Restituisce un dizionario con la ricetta appena creata o
        un messaggio di errore se la ricetta esiste già."""
        self.name = name
        self.ingredients = ingredients
        
        if name in self.dizionario[name]:
            self.dizionario[name] = self.ingredients
            
        return {self.name, self.ingredients}
    
    def add_ingredient(self,recipe_name, ingredient): 
        """Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di 
        errore se l'ingrediente esiste già o la ricetta non esiste."""
        for k,v in self.dizionario:                
            if recipe_name == k:
                if ingredient not in self.dizionario[k]:
                    self.dizionario[k].append(ingredient)
            else:
                f"la ricetta non esiste"
            
            if ingredient in self.dizionario[k]:
                f"l'ingrediente esiste già"
            else:
                self.dizionario[k].append(ingredient)
                
