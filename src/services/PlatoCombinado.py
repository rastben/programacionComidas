import random
import json
from src.services.abtracts.Plato import Plato

opcionesComida = json.load(open('src/services/comidas.json'))

class PlatoCombinado(Plato):
     
     def __init__(self):
         self.proteina = ''
         self.carbohidrato = ''
         self.ensalada = ''

     def generarPlato(self):
        self.proteina = random.choice(opcionesComida['proteinas'])
        self.carbohidrato = random.choice(opcionesComida['carbohidratos'])
        self.ensalada = random.choice(opcionesComida['ensaladas'])
        print(f'Plato: {self.proteina} con {self.carbohidrato} y ensalada {self.ensalada}')