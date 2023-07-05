# SUELDO HORIZONTE
## Objetivos del proyecto

Implementar en Python un algoritmo para calcular el sueldo a pagar a un trabajador de la empresa "Horizonte" siguiendo las especificaciones dadas.

Aplicar el desarrollo guiado por pruebas, lo que significa que se deben crear casos de prueba para verificar que el algoritmo funciona correctamente.

Aplicar el control de versiones, lo que implica que se debe utilizar una herramienta de control de versiones (por ejemplo, Git) para mantener un registro de los cambios realizados en el código.

Dividir el proceso de implementación en refinamientos para facilitar el desarrollo y asegurar que cada parte del algoritmo funcione correctamente antes de pasar a la siguiente.

Calcular el sueldo neto a pagar al trabajador considerando las bonificaciones y descuentos especificados en la consigna.

Imprimir la boleta de pago del trabajador con los detalles del sueldo neto, bonificaciones y descuentos.

## Integrantes del equipo de desarrollo
| Apellidos y nombres | Rol | 
|---------------------| ---- |
|Escobar Ccanto Samuel| Desarrollador|
|Leiva Leiva Juan| Desarrollador|
|Nolasco Meza Nilton Anthony|Desarrollador|
|Ramirez Crispin William|Desarrollador|
|Ramos Canchomonia Malher|Desarrollador|
|Taype Huarocc Jeanpier|Desarrollador|
## Listado de historias de usuario (product backlog priorizada)
| Prioridad | Identificador |  Nombre (alias) | Descripción | Punto de historia (días ideales) | Responsable |
|-----------|---------------|-----------------|-------------|----------------------------------|-------------|
|1|HU001|Ingresar datos del trabajador|Como gerente, quiero ingresar el nombre del trabajador, su sueldo básico, días de faltas, minutos de tardanzas y horas extras con la finalidad de elaborar un catálogo de datos del trabajador.|1|Jeanpier Taype|
|2|HU002|Calcular las bonificaciones|Como gerente, quiero calcular las bonificaciones a pagar al trabajador, que incluyen las horas extras, la bonificación por movilidad y la bonificación suplementaria con la finalidad de actualizar las bonificaciones|3|Jeanpier Taype|
|3|HU003|Calcular los descuentos|Como gerente, quiero calcular los descuentos a aplicar al trabajador, que incluyen las faltas y las tardanzas, con la finalidad de|2|Jeanpier Taype|
|4|HU004|Cálculo del sueldo neto|Como gerente, quiero realizar el cálculo final del sueldo a pagar al trabajador, sumando las bonificaciones y restando los descuentos con la finalidad de tener un registro preciso y detallado de los pagos realizados y garantizar la transparencia y precisión en el manejo de la nómina de la empresa.|1|Jeanpier Taype|
|5|HU005|Impresión de boleta de pagos|Como gerente quiero generar  una boleta de pago con el nombre del trabajador, su sueldo básico, las bonificaciones, los descuentos y el sueldo neto con la finalidad de mejorar la eficiencia, precisión y transparencia en el proceso de pago de salarios de la empresa.|1|William Ramire|
|6|HU006|Pago por horas extras|Como gerente quiero calcular el pago correspondiente a las horas extras trabajadas por el empleado con la finalidad de compensar justamente su tiempo y esfuerzo adicional, cumplir con las leyes laborales vigentes y mantener una relación justa y equitativa con nuestros trabajadores.|1|William Ramirez|
|7|HU007|Bonificación por movilidad|Como gerente quiero calcular la bonificación fija por movilidad a pagar al trabajador con la finalidad de incentivar su desempeño, reconocer su compromiso y dedicación, y mejorar su calidad de vida laboral.|1|William Ramire|
|8|HU008|Bonificación suplementaria|Como gerente, quiero calcular la bonificación suplementaria a pagar al trabajador, equivalente al 3% de su sueldo básico con la finalidad de recompensar su productividad, estimular su motivación y fidelizar su compromiso con la empresa.|1|William Ramire|
|9|HU009|Descuento por faltas|Como gerente, quiero calcular el descuento correspondiente a las faltas del trabajador, basado en su remuneración computable.|1|Juan Leiva|
|10|HU010|Descuento por tardanzas|Como gerente, quiero calcular el descuento correspondiente a las tardanzas del trabajador, basado en su remuneración computable.|1|Juan Leiva|
|11|HU011|Validación de datos|Como gerente, quiero verificar que los datos ingresados por el usuario sean válidos y no contengan errores.|2|Juan Leiva|
|12|HU012|Pruebas unitarias de ingreso de datos|Como gerente, quiero realizar pruebas unitarias para verificar que el ingreso de datos del trabajador funciona correctamente.|2|Juan Leiva|
|13|HU013|Pruebas unitarias de cálculo de bonificaciones|Como gerente, quiero realizar pruebas unitarias para verificar que el cálculo de las bonificaciones funciona correctamente.|2|Nilton Nolasco|
|14|HU014|Pruebas unitarias de cálculo de descuentos|Como gerente, quiero realizar pruebas unitarias para verificar que el cálculo de los descuentos funciona correctamente.|2|Nilton Nolasco|
|15|HU015|Pruebas unitarias de cálculo del sueldo neto|Como gerente, quiero realizar unitarias para verificar que el cálculo del sueldo neto funciona correctamente.|2|Nilton Nolasco|
|16|HU016|Documentación del código|Como gerente, quiero que el código esté debidamente documentado para poder entenderlo y modificarlo en caso de ser necesario.|5|Nilton Nolasco|
|17|HU017|Pruebas unitarias|Como gerente, quiero escribir pruebas unitarias para verificar que el cálculo del sueldo a pagar sea correcto.|5|Escobar. S|
|18|HU018|Pruebas de integración|Como gerente, quiero realizar pruebas de integración con la finalidad de verificar que la aplicación funcione correctamente en su conjunto.|5|Escobar. S|
|19|HU019|Despliegue de la aplicación|Como gerente, quiero desplegar la aplicación en un servidor con la finalidad de que pueda ser utilizada por los usuarios.|3|Escobar. S|
|20|HU020|Configuración de control dem versiones|Como gerente, quiero configurar un sistema de control de versiones con la finalidad de gestionar los cambios en el código fuente.|2|Escobar. S|
|21|Hu021|Configuración de control de versiones|Como Gerente, quiero que el sistema valide que se ingrese el sueldo básico para evitar errores en el cálculo del sueldo neto.|1|Ramos.M|
|22|Hu022|Crear función para validar los días de falta|Como Gerente,  quiero que el sistema valide que se ingrese el número de días de falta para evitar errores en el cálculo del sueldo neto.|1|Ramos.M|
|23|Hu023|Crear función para validar los minutos de tardanza|Como Gerente, quiero que el sistema valide que se ingrese el número de minutos de tardanza para evitar errores en el cálculo del sueldo neto.|1|Ramos.M|
|24|Hu024|Crear función para validar las horas extras|Como Gerente, quiero que el sistema valide que se ingrese el número de horas extras para evitar errores en el cálculo del sueldo neto.|1|Ramos.M|
# ProyectoFindeCurso
