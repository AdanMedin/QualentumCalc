import unittest
from operaciones import suma, resta, multiplicacion, division, raizCuadrada

class TestOperaciones(unittest.TestCase):
    def test_s(self):
        self.assertEqual(suma(4, 1), 5)
        self.assertEqual(suma(-3, 1), -2)
        self.assertEqual(suma(-2, 2), 0)
        
    def test_r(self):
        self.assertEqual(resta(4, 1), 3)
        self.assertEqual(resta(-3, 1), -4)
        self.assertEqual(resta(2, -2), 4)
        
    def test_m(self):
        self.assertEqual(multiplicacion(4, 1), 4)
        self.assertEqual(multiplicacion(-3, 0), 0)
        self.assertEqual(multiplicacion(-2, 2), -4)
        
    def test_d(self):
        self.assertEqual(division(4, 2), 2)
        self.assertEqual(division(-3, 2), -1.5)
        self.assertEqual(division(1, 2), 0.5)
        with self.assertRaises(ZeroDivisionError): # Comprovamos que falla si se intenta dividir un numero entre cero
            division(4, 0)
        
    def test_sqrt(self):
        self.assertEqual(raizCuadrada(0), 0)
        self.assertEqual(raizCuadrada(3), 1.7320508075688772)
        with self.assertRaises(ValueError): # Comprovamos que falla si se intenta obtener la raiz cuadrada de un numero negativo
            raizCuadrada(-2)
        
if __name__ == "_main_":
    unittest.main()