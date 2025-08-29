"""

Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

"""

# print("¡Hola Mundo!")


"""

Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

"""

# variable = "¡Hola Mundo!"
# print(variable)


"""

Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

"""

# nombre = input("Ingresa tu nombre por favor: \n")
# print("¡Hola " + nombre + "!")

"""

Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
 
"""

# resultado = ((3+2)/(2*5))**2
# print(resultado)

"""

Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

"""

# horas_trabajadas = float(input("¿Cuántas horas trabajó? "))
# coste_por_hora = float(input("¿Cuánto cuesta su hora de trabajo? "))
#
# paga_correspondiente = horas_trabajadas * coste_por_hora
# print("Usted tiene que recibir: ", paga_correspondiente)

"""

Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma:

"""

# n = int(input("Ingrese un número entero positivo: "))
#
# suma = n*(n+1)/2
#
# print("La suma de los primeros números desde 1 hasta " + str(n) + " es " + str(suma))


"""

Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

"""

# peso = float(input("Ingrese su peso en Kilogramos: "))
# estatura = float(input("Ingrese su estatura en metros: "))
#
# imc = (peso/estatura**2)
#
# print("Tu índice de masa corporal es: " + str(imc) + " donde " + str(round(imc, 2)) + " es el índice de masa corporal calculado redondeado con dos decimales.")

"""

Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

"""

# numero_1=int(input("Ingresa un número positivo: "))
# numero_2=int(input("Ingresa otro número positivo: "))
#
# print("La " + str(numero_1) + " entre " + str(numero_2) + " da un cociente " + str(numero_1 // numero_2) + " y un resto " + str(numero_1 % numero_2))

"""

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

"""

# inversion = float(input("Ingrese lo que quiere invertir: "))
# interes_anual = float(input("Ingrese el interes anual: "))
# numero_anios = float(input("Ingrese el número de anios: "))
#
# capital_obtenido = inversion * (interes_anual / 100 + 1) ** numero_anios
#
#
# print("Capital final: " + str(round(capital_obtenido,2)))
# print(f"Capital final: {round(capital_obtenido,2)}")


"""

Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

"""

# cantidad_payasos = int(input("Ingrese la cantidad de payasos: "))
# cantidad_munecas = int(input("Ingrese la cantidad de munecas: "))
#
# peso_payasos = 112
# peso_munecas = 75
#
# calculo_peso_total = ((cantidad_payasos*peso_payasos) + (cantidad_munecas * peso_munecas))/1000
#
# print("fEl pesos total de " + str(cantidad_payasos) + " payasos y de " + str(cantidad_munecas) + " munecas es de " + str(calculo_peso_total) + " kg o bien " + str(round(calculo_peso_total*1000,2)) + " gramos.")
# print(f"El peso total de {cantidad_payasos} payasos y {cantidad_munecas} munecas es de {calculo_peso_total} kg o bien {int(calculo_peso_total*1000)} gramos.")

"""

Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

"""

# ahorro = float(input("Ingrese la cantidad que meterá a su cuenta de ahorro: "))
# anios = int(input("ingrese la cantidad de anios: "))
# interes = 0.04
# ahorro1 = ahorro
#
# primer = ahorro + ahorro*interes
#
# segundo = primer + primer*interes
#
# tercer = segundo + segundo*interes
#
# print(f"Sus ganancias en el primer anio son: {round(primer,2)}  en  el segundo anio son {round(segundo,2)} y en el tercero son {round(tercer,2)} ")
#
#
# for i in range(1, anios + 1):
#     ahorro1 += ahorro1*interes
#     ahorro1 = round(ahorro1,2)
#     print(f"Al final del anio {i}, el ahorro es: {ahorro1}")

"""

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

"""

pan = 3.49
pan_pasado = pan - pan * 0.60

cantidad_pan = int(input("Ingrese el numero de panes que se vendió: "))

print(f"El costo habitual de un pan es de 3.49 euros el descuento que se le da es de un 60%, como se vendieron {cantidad_pan} pan/es el precio habitual hubieran sido {round(pan*cantidad_pan,2)} pero como son pasados, el precio es {round(pan_pasado*cantidad_pan,2)}")


