
import unittest

class Complejo(object):
    def __init__(self, real, imaginario = 0):
        self.real = real
        self.imaginario = imaginario

    def sumar(self, otro):
        suma = Complejo(self.real + otro.real, self.imaginario + otro.imaginario)
        return suma

    def restar(self, otro):
        resta = Complejo(self.real - otro.real, self.imaginario - otro.imaginario)
        return resta

    def multiplicacion(self, otro):
        parte_real = self.real * otro.real - self.imaginario * otro.imaginario
        parte_imaginaria = self.real * otro.imaginario + self.imaginario * otro.real
        complejo = Complejo(parte_real, parte_imaginaria)
        return complejo 
    def division(self, otro):
        parte_real1 = self.real * otro.real + self.imaginario * otro.imaginario
        parte_imaginaria1 = self.imaginario * otro.real - self.real * otro.imaginario
        numerador = Complejo(parte_real1, parte_imaginaria1)
        
        parte_real2 = otro.real**2 - otro.imaginario**2        
        denominador = Complejo(parte_real2)
        
        division = Complejo((parte_real1 / parte_real2) , parte_imaginaria1 / parte_real2)
        return division
c1 = Complejo(2,1)
c2 = Complejo(2,3)
print(c1.division(c2))
        
        
