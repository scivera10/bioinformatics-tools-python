
import unittest

from calculate_gc import calcular_gc, calcular_gc_ventanas

class TestCalculateGC(unittest.TestCase):

    def test_gc_ventanas(self):
        resultado = calcular_gc_ventanas("ATGCGCATAT", window=4)
        self.assertEqual(resultado, [50.0, 50.0, 0.0])

    def test_ventana_decimal(self):
        # Comprobar que una ventana decimal genera un TypeError
        with self.assertRaises(TypeError):
          calcular_gc_ventanas("ATGCGC", window=4.5)

    def test_ventana_negativa(self):
        with self.assertRaises(ValueError):
            calcular_gc_ventanas("ATGCGC", window=-5)
    
    def test_ventana_cero(self):
        with self.assertRaises(ValueError):
            calcular_gc_ventanas("ATGCGC", window=0)
    
    def test_ventana_mayor_secuencia(self):
        resultado = calcular_gc_ventanas("ATGCGC", window=1000)
        self.assertEqual(len(resultado), 1)
        self.assertAlmostEqual(resultado[0], 66.6666667, places=6)
    
    def test_gc_global(self):
       secuencia = "ATGCGC"
       resultado = calcular_gc(secuencia)
       self.assertAlmostEqual(resultado, 66.6666667, places=6)

    def test_gc_extremos(self):
       self.assertEqual(calcular_gc("ATAT"), 0.0)
       self.assertEqual(calcular_gc("GCGC"), 100.0)

    def test_secuencia_vacia(self):
       with self.assertRaises(ValueError):
        calcular_gc("")
       with self.assertRaises(ValueError):
        calcular_gc_ventanas("", window=1000)

if __name__ == "__main__":
    unittest.main()
