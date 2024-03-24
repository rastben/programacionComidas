import json
import random
from src.services.abtracts.Plato import Plato

opcionesComida = json.load(open('src/services/comidas.json'))

class PlatoCompleto(Plato):

     def generarPlato(self):
        plato = random.choice(opcionesComida['platosCompletos'])
        print(f'Plato: {plato}')
        