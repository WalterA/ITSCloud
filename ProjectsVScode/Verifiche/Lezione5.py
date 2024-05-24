"""Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e 
viceversa a seconda del parametro to_fahrenheit.
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit."""
def convert_temperature(temp, to_fahrenheit=True):
    if to_fahrenheit:
        return temp * 9/5 + 32
    else:
        return (temp - 32) * 5/9