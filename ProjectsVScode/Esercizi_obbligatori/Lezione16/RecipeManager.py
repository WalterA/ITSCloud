class RecipeManager:
    def __init__(self):
        self.dizionario = {}

    def create_recipe(self, name, ingredients):
        """
        Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
        Restituisce un dizionario con la ricetta appena creata o
        un messaggio di errore se la ricetta esiste già.
        """
        if name in self.dizionario:
            return f"La ricetta '{name}' esiste già."
        else:
            self.dizionario[name] = ingredients
            return {name: ingredients}

    def add_ingredient(self, recipe_name, ingredient):
        """
        Aggiunge un ingrediente alla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se
        l'ingrediente esiste già o la ricetta non esiste.
        """
        if recipe_name in self.dizionario:
            if ingredient not in self.dizionario[recipe_name]:
                self.dizionario[recipe_name].append(ingredient)
                return {recipe_name: self.dizionario[recipe_name]}
            else:
                return f"L'ingrediente '{ingredient}' esiste già nella ricetta '{recipe_name}'."
        else:
            return f"La ricetta '{recipe_name}' non esiste."

    def remove_ingredient(self, recipe_name, ingredient):
        """
        Rimuove un ingrediente dalla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se
        l'ingrediente non è presente o la ricetta non esiste.
        """
        if recipe_name in self.dizionario:
            if ingredient in self.dizionario[recipe_name]:
                self.dizionario[recipe_name].remove(ingredient)
                return {recipe_name: self.dizionario[recipe_name]}
            else:
                return f"L'ingrediente '{ingredient}' non è presente nella ricetta '{recipe_name}'."
        else:
            return f"La ricetta '{recipe_name}' non esiste."
        
    def update_ingredient(self,recipe_name, old_ingredient, new_ingredient): 
        """Sostituisce un ingrediente con un altro nella ricetta specificata. 
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente
        non è presente o la ricetta non esiste."""
        for name, ingredients_list in self.dizionario.items():
            if recipe_name == name:
                for i in range(len(ingredients_list)):
                    if ingredients_list[i] == old_ingredient:
                        ingredients_list[i] = new_ingredient
                        return {recipe_name: self.dizionario[recipe_name]}
                    else:
                        f"L'ingrediente '{old_ingredient}' non è presente nella ricetta '{recipe_name}'."
            else:
                f"{recipe_name}' non esiste."


    def list_recipes(self):
        """Elenca tutte le ricette esistenti."""
        for k in self.dizionario.keys():
            lista= [k]
        return lista

    def list_ingredients(self,recipe_name):
        """Mostra gli ingredienti di una specifica ricetta.
        Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste."""
        for k,v in self.dizionario.items():
            if k == recipe_name:
               return f"{v}"
        else:
            f"la ricetta non esiste."
    def  search_recipe_by_ingredient(self,ingredient): 
        """Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
        Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente."""
        elenco = []
        for k,v in self.dizionario.items():
            for elem in range(len(v)):
                    if v[elem] == ingredient:
                        return self.dizionario
        if elenco:
            return elenco
        else:
            "nessuna ricetta contiene l'ingrediente."

    # Esempi di utilizzo della classe

manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))