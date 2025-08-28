#primer hola mundo

print("Hola mundo",  3 + 20)


#datos simples

"""
hola = "hola"

print(hola)


#si es una sola linea
hola = 'adiós'


#para escribir en multiple lineas
adiós = ('''hoal
como estás''')



print (adiós)



#tipo de dato int

int

a = 5

#tipo de dato flotante

float

b=40.2

#tipo de dato booleano


verdadero = True
falso = False


print(verdadero)
print(falso)


#variables

d = 2
e = 3

f = a+e

print(f)

nombre = "Fernando"
apellido = "Rosales"

print(nombre + " " + apellido + ".")


nombre1 = "Fernando "
nombre1 += "Rosales. "

print(nombre1)


numero=5
numero+=5


print(numero)

numero_1=45
numero_1-=2

print(numero_1)


#f strings
bienvenida = f"Hola {nombre} ¿Cómo estás?"
print(bienvenida)

del nombre

print(bienvenida)


#operadores de pertenencia

print("Hola" not in bienvenida)


print("Hola" in bienvenida)


#para hacer anotaciones

"""
"""
Para
 hacer
  comentarios
   en
    varias
     lineas
      e
       imprimir
        en
         varias
          lineas
"""

#definir variable con camelCase

#nombreCompleto


#RECOMENDADO

"""

#definir variable con snake_case

#nombre_completo

#definir constantes con snake_case

#ESTO_ES_ UNA_ CONSTANTE

"""


#RECOMENDADO



#Datos complejos


#lista

"""
lista= ["Fernando Rosales", "keloke",True, 1.75]
print(lista[0]) #indice 0
print(lista[1]) #indice 1
print(lista[2]) #indice 2
print(lista[3]) #indice 3

lista[0] = "Fernando"

print(lista[0])
"""

#tuplas

tupla = ("Fernando Rosales", "keloke",True, 1.75)
print(tupla[0])

#conjunto (set) (no se puede acceder a elementos por indicie, no almacanea datos duplicados)

conjunto = {"Fernando Rosales", "keloke",True, 1.75}

#print(conjunto[3]) -> no puede acceder al elemento

#diccionario {key : value}
diccionario = {"saludo":"hola",
               "altura": 1.75

}


#print(diccionario[key])
print(diccionario["saludo"])
print(diccionario["altura"] + 3)



#operadores aritméticos/matemáticos


"""
+ suma a + b = 15
- resta b - a = 5
* multiplicación a * b = 50
/ División b/a = 2
% Modulo-devuleve el resto de la devisión b%a = 0
** exponente - realiza exponencial b ** a = 10000
// Devisión baja - devuleve el entero de la división b // a = 2

"""

#suma y resta (+ y -)


suma = 12 + 5
resta = 12 - 5

#multiplicación y división (* y /)

multiplicacion = 12*5
division = 12/5 #siempre da un dato flotante

# resto o modulo

resto = 12 % 5

#potenciación exponente (**)

exponente = 12**5

#división baja

divsion_baja = 12 // 5


print(suma)
print(resta)
print(multiplicacion)
print(division)
print(divsion_baja)
print(resto)
print(exponente)
print(divsion_baja)

# devuelve que tipo de datos es

tipo_de_dato = type(division)
print(tipo_de_dato)



# Operadores de comparación


"""
== es igual que

!= es distinto de

< es menor que

<= es menor o igual que

> es mayor que

>= es mayor o igual que

"""

es_igual_que = 5 == 5
es_distinto_de = 5 != 6

mayor_que = 5 > 6
menor_que = 5 < 6

mayor_o_igual = 5 >= 6
menor_o_igual = 5 <= 6

print(es_igual_que)
print(es_distinto_de)
print(mayor_que)
print(menor_que)
print(mayor_o_igual)
print(menor_o_igual)

#calculos combinados

a = 5
b = 10
c = 20
comparacion = a + b < c
print(comparacion)

#condicionaless

"""
if true
    se ejecuta


if false
    esto no se ejecuta

"""


#if_else

edad = 1


if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")



#else_if


ingreso_mensual = 10000

if ingreso_mensual >= 10000:
    print("Estás bien en todo el mundo")

elif ingreso_mensual >= 1000:
    print("Estas bien solo en paises tercermundias")

else:
    print("Eres pobre")


#operadores lógicos


#AND en el único caso que dará verdader es si los dos son verdaderos, de lo contrario, cualquier otro caso será falso.
result = True & True

#OR en el único caso que puede dar falso es si los dos son falsos, de lo contrario, cualquier otro caso será verdadero.

result_1= False | False


#NOT lo que hace es cambiar la naturaleza, es decir, si es verdadero, lo hace falso y de caso contrario, si es falso lo hace verdadero.

result_3 = not True
result_4 = not False

#print

print(result_4)


