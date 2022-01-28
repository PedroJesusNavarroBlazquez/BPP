import unittest
import operaciones

class PruebasUnitarias(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones.suma(18,2), 20)
    def test_rest(self):
        self.assertEqual(operaciones.resta(7, 3), 4)
    def test_es_par(self):
        self.assertTrue(operaciones.es_par(2))
        self.assertFalse(operaciones.es_par(3))

if __name__ == '__main__':
    unittest.main()

