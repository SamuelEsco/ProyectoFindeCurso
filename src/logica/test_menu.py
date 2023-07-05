import unittest
from src.logica.menu import mostrar_menu


class TestMenu(unittest.TestCase):
    def test_mostrar_menu(self):
        # Redirigir la salida estándar a un StringIO para capturar la salida
        from io import StringIO
        import sys
        stdout_saved = sys.stdout
        sys.stdout = output = StringIO()

        # Llamar a la función mostrar_menu()
        mostrar_menu()

        # Restaurar la salida estándar
        sys.stdout = stdout_saved

        # Comprobar si la salida es correcta
        expected_output = "----- Menú Principal -----\n1. Ingresar datos del trabajador\n2. Calcular sueldo a pagar\n3. Calcular bonificaciones\n4. Calcular descuentos\n5. Imprimir boleta de pago\n6. Salir\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_mostrar_menu_digitar_mal(self):
         # Redirigir la salida estándar a un StringIO para capturar la salida
        from io import StringIO
        import sys
        stdout_saved = sys.stdout
        sys.stdout = output = StringIO()

        # Llamar a la función mostrar_menu()
        mostrar_menu()

        # Restaurar la salida estándar
        sys.stdout = stdout_saved

        # Comprobar si la salida es correcta
        expected_output = "----- Menú Principales -----\n1. Ingreso datos del trabajador\n2. Calcular sueldo a pagar\n3. Calcular bonificaciones\n4. Calcular descuentos\n5. Imprimir boleta de pago\n6. Salir\n"
        self.assertEqual(output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
