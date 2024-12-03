import unittest
from backtracking import leer_archivo, resolver_batalla_naval

class TestBacktracking(unittest.TestCase):
    
    def test_3_3_2(self):
        datos = "3_3_2.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)    
        resultado_esperado = 4 
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas) 
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_5_5_6(self):
        datos = "5_5_6.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 12
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_8_7_10(self):
        datos = "8_7_10.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 26
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_10_3_3(self):
        datos = "10_3_3.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 6
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_10_10_10(self):
        datos = "10_10_10.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 40
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_12_12_21(self):
        datos = "12_12_21.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 46
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_15_10_15(self):
        datos = "15_10_15.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 40
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
    
    def test_20_20_20(self):
        datos = "20_20_20.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 104
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_20_25_30(self):
        datos = "20_25_30.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 172
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)
        
    def test_30_25_25(self):
        datos = "30_25_25.txt"
        demandas_filas, demandas_columnas, barcos = leer_archivo(datos)
        resultado_esperado = 202
        mejor_demanda_cumplida = resolver_batalla_naval(len(demandas_filas), len(demandas_columnas), barcos, demandas_filas, demandas_columnas)
        self.assertEqual(mejor_demanda_cumplida, resultado_esperado)