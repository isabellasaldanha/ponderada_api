from abc import ABC, abstractmethod

class Zoologico(ABC):
    def __init__(self):
        self.recintos = []
        self.visitantes_count = 0
    
    @abstractmethod
    def criar_animal(self, nome, especie, nivel_felicidade=10):
        """Cria um animal"""
        pass

    @abstractmethod
    def criar_recinto(self, nome):
        """Cria um recinto"""
        pass

    def atrair_visitantes(self):
        felicidade_total = sum(animal.felicidade for recinto in self.recintos for animal in recinto.animais)
        visitantes = felicidade_total // 10  
        self.visitantes_count += visitantes
        return visitantes

class MeuZoologico(Zoologico):
    def criar_animal(self, nome, especie, nivel_felicidade=10):
        return Animal(nome, especie, nivel_felicidade)

    def criar_recinto(self, nome):
        return Recinto(nome)

class Animal:
    def __init__(self, nome, especie, felicidade=10):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade
    
    def alimentar(self):
        self.felicidade += 10

class Recinto:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)
        animal.felicidade += 10  

