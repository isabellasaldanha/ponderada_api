import unittest
from zoologico import MeuZoologico, Animal, Recinto

class TestZoologico(unittest.TestCase):
    def test_criar_animal(self):
        zoo = MeuZoologico()
        animal = zoo.criar_animal('Cobra', 'Réptil', 50)

        self.assertEqual(animal.felicidade, 50)
        
    def test_criar_recinto(self):
        zoo = MeuZoologico()
        recinto = zoo.criar_recinto('Floresta')

        self.assertEqual(recinto.nome, 'Floresta')

    def test_atrair_visitantes(self):
        zoo = MeuZoologico()
        recintoA = Recinto('Floresta')
        recintoB = Recinto('Savana')
        animalA = Animal('Cobra', 'Réptil', 40)
        animalB = Animal('Girafa', 'Herbívoro', 60)
        recintoA.adicionar_animal(animalA)
        recintoB.adicionar_animal(animalB)
        zoo.recintos.extend([recintoA, recintoB])
        visitantes = zoo.atrair_visitantes()

        self.assertEqual(visitantes, 12)  

class TestAnimal(unittest.TestCase):
    def test_alimentar(self):
        animal = Animal('Cobra', 'Réptil', 40)
        felicidade_anterior = animal.felicidade
        animal.alimentar()
        self.assertEqual(animal.felicidade, felicidade_anterior + 10)


class TestRecinto(unittest.TestCase):
    def test_adicionar_animal(self):
        recinto = Recinto('Savana')
        animal = Animal('Girafa', 'Herbívoro')  

        felicidade_anterior = animal.felicidade
        recinto.adicionar_animal(animal)
        self.assertEqual(animal.felicidade, felicidade_anterior + 10)
