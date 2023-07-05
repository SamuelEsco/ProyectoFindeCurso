import unittest
from src.logica.trabajador import Trabajador

class TestTrabajador(unittest.TestCase):

    # PASA
    def test_calcular_sueldo_pagar(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("Juan", 3000)
        trabajador.horas_extras =30
        trabajador.dias_falta = 20
        trabajador.minutos_tardanza = 30

        # Calcular el sueldo a pagar
        sueldo_pagar = trabajador.calcular_sueldo_pagar()

        # Comprobar el resultado
        self.assertEqual(sueldo_pagar, 1917.3124999999995)

    # NO PASA
    def test_nopuedo_calcular_sueldo_pagar_con_espacios_en_blanco(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("Carlos", 2300)

        # Intentar calcular el sueldo a pagar con espacios en blanco
        with self.assertRaises(ValueError):
            trabajador.horas_extras = " "
            trabajador.calcular_sueldo_pagar()

        with self.assertRaises(ValueError):
            trabajador.dias_falta = "   "
            trabajador.calcular_sueldo_pagar()

    # NO PASA
    def test_nopuedo_calcular_sueldo_pagar_con_numeros_negativos(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("Laura", 2100)

        # Intentar calcular el sueldo a pagar con números negativos
        with self.assertRaises(ValueError):
            trabajador.horas_extras = -5
            trabajador.calcular_sueldo_pagar()

        with self.assertRaises(ValueError):
            trabajador.dias_falta = -2
            trabajador.calcular_sueldo_pagar()


        # PASA
    def test_calcular_bonificaciones(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("Pedro", 2500)
        trabajador.horas_extras = 8

        # Calcular las bonificaciones
        bonificaciones = trabajador.calcular_bonificaciones()

        # Comprobar el resultado/1200.0/1208.3333333333333
        self.assertEqual(bonificaciones, 1200.0)

        # NO PASA: 291.34583333333336
    def test_calcular_descuentos(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("María", 1800)
        trabajador.dias_falta = 3
        trabajador.minutos_tardanza = 30

        # Calcular los descuentos
        descuentos = trabajador.calcular_descuentos()

        # Comprobar el resultado
        self.assertEqual(descuentos, 326.666)

    # NO PASA:
    def test_nopuedo_calcular_descuentos_int_y_str(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("Juana", 2200)

        with self.assertRaises(ValueError):
            # Intento con un valor de cadena
            trabajador.dias_falta = "abc"
            trabajador.calcular_descuentos()

    # NO PASA:
    def test_nopuedo_calcular_descuentos_int_mas_de_30_faltas(self):
        # Crear un objeto Trabajador con valores de ejemplo
        trabajador = Trabajador("Ana", 3000)

        # Intentar calcular los descuentos con valores inválidos

        with self.assertRaises(ValueError):
            # Intento con un valor de cadena
            trabajador.dias_falta = 31
            trabajador.calcular_descuentos()





if __name__ == '__main__':
    unittest.main()