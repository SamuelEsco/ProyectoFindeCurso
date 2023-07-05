from src.logica.trabajador import Trabajador
from src.logica.menu import mostrar_menu

trabajador = Trabajador("", 0)

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        trabajador.ingresar_datos()
    elif opcion == "2":
        try:
            sueldo_pagar = trabajador.calcular_sueldo_pagar()
            print("Sueldo a pagar:", sueldo_pagar)
        except Exception as e:
            print("Error al calcular el sueldo a pagar:", str(e))
    elif opcion == "3":
        try:
            bonificaciones = trabajador.calcular_bonificaciones()
            print("Bonificaciones:", bonificaciones)
        except Exception as e:
            print("Error al calcular las bonificaciones:", str(e))
    elif opcion == "4":
        try:
            descuentos = trabajador.calcular_descuentos()
            print("Descuentos:", descuentos)
        except Exception as e:
            print("Error al calcular los descuentos:", str(e))
    elif opcion == "5":
        trabajador.imprimir_boleta_pago()
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")