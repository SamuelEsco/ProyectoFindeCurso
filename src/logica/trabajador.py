import re

class Trabajador:
    def __init__(self, nombre, sueldo_basico):
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.dias_falta = 0
        self.minutos_tardanza = 0
        self.horas_extras = 0

    def ingresar_datos(self):
        while True:
            try:
                nombre = input("Ingrese el nombre del trabajador : ")
                if not re.match("^[a-zA-Z]+$", nombre):
                    raise ValueError("Nombre inválido. Ingrese un valor válido .")
                self.nombre = nombre
                break
            except ValueError as e:
                print(str(e))

        while True:
            try:
                sueldo_basico = input("Ingrese el sueldo básico: ")
                sueldo_basico = float(sueldo_basico)
                if sueldo_basico < 1025 :
                    raise ValueError("Sueldo básico inválido. Ingrese un valor válido.")
                self.sueldo_basico = sueldo_basico
                break
            except ValueError as e:
                print(str(e))

        while True:
            try:
                dias_falta = input("Ingrese los días de falta (máximo 30): ")
                dias_falta = int(dias_falta)
                if dias_falta < 0 or dias_falta > 30:
                    raise ValueError("Días de falta inválidos. Ingrese un valor válido.")
                self.dias_falta = dias_falta
                break
            except ValueError as e:
                print(str(e))

        while True:
            try:
                minutos_tardanza = input("Ingrese los minutos de tardanza: ")
                minutos_tardanza = int(minutos_tardanza)
                if minutos_tardanza < 0 or minutos_tardanza > 43200:
                    raise ValueError("Minutos de tardanza inválidos. Ingrese un valor válido.")
                self.minutos_tardanza = minutos_tardanza
                break
            except ValueError as e:
                print(str(e))

        while True:
            try:
                horas_extras = input("Ingrese las horas extras: ")
                horas_extras = int(horas_extras)
                if horas_extras < 0:
                    raise ValueError("Horas extras inválidas. Ingrese un valor válido.")
                self.horas_extras = horas_extras
                break
            except ValueError as e:
                print(str(e))

    def calcular_sueldo_pagar(self):
        bonificaciones = self.calcular_bonificaciones()
        descuentos = self.calcular_descuentos()
        sueldo_neto = self.sueldo_basico + bonificaciones - descuentos
        return sueldo_neto

    def calcular_bonificaciones(self):
        pago_horas_extras = 1.50 * self.horas_extras * self.sueldo_basico / 30 / 8
        movilidad = 1000
        bonificacion_suplementaria = 0.03 * self.sueldo_basico
        bonificaciones = movilidad + bonificacion_suplementaria + pago_horas_extras
        return bonificaciones

    def calcular_descuentos(self):
        remuneracion_computable = self.sueldo_basico + 1000 + 0.03 * self.sueldo_basico
        descuento_faltas = remuneracion_computable / 30 * self.dias_falta
        descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * self.minutos_tardanza
        descuentos = descuento_faltas + descuento_tardanzas
        return descuentos

    def imprimir_boleta_pago(self):
        sueldo_neto = self.calcular_sueldo_pagar()
        print("----- Boleta de Pago -----")
        print("Trabajador:", self.nombre)
        print("Sueldo Básico:", self.sueldo_basico)
        print("Bonificación:", self.calcular_bonificaciones())
        print("Descuento:", self.calcular_descuentos())
        print("Sueldo Neto:", sueldo_neto)