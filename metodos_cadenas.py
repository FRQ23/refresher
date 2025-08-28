
cadena1 = "Hola soy Fernando"
cadena2 = "Comprate la 5070 ti pa"
cadena3 = "5555555555555555555"
cadena4 = "hola"

#todas las cosas que podemos hacer con esto
#print(dir(cadena1))

#las cosas que podemos hacer con una cadena

#resultado = dir(cadena1)

#print(resultado)

#upper (poner la cadena en mayúsculas)


#resultado = DATO.METODO(PARÁMETROS)

# mayusculas = cadena1.upper()
#
# print(mayusculas)



# convertir en minuscula
# minusculas = cadena1.lower()
#
# print(minusculas)


# convertir la primera letra en mayuscula
#
# primera_letra_mayuscula = cadena1.capitalize()
#
# print(primera_letra_mayuscula)


#buscar una cadena dentro de otra cadena si no encuentra es -1, si no te dice la posicíón donde está

# busqueda_find = cadena2.find("C")
#
# if (busqueda_find == -1):
#     print("No se encontró la letra")
# else:
#     print("Se encontró la letra en la posicioón: ", busqueda_find)
#
# #print(busqueda_find)


#buscamos una cadena dentro de otra cadena, el mismo comportamiento que find, pero si es que no encuentra en lugar de retornar -1, retorna una excepeción (para manejarse)

# busqueda_index = cadena1.index("z")
# print(busqueda_index)

#Si es un numéricos, devuelve true, sino, devuelve false

# es_numerico = cadena3.isnumeric()
# print(es_numerico)


#si es alfanumérico (A-Z y a-z, caracteres especiales no entran ni siquiera el espacio) si está dentro de ese conjunto retornará true si no, será false.

# es_alfa = cadena4.isalpha()
# print(es_alfa)

# COUNT devuelve el número de ocurrencias de una subcadena dada, devuelve la cantidad de veces que coinicide, si no encuentra, es 0

# get_coincidencias = cadena4.count("a")
# print(get_coincidencias)

# LEN es una función pero no un método cuenta la cantidad de caracteres que tiene una cadena

# contar_caracteres = len(cadena1)
# print(contar_caracteres)

# verificamos si una cadena empiece con otra cadena dada, si es así devuleve true

# empieza_con = cadena1.startswith("h")
# print(empieza_con)

# verificamos si una cadena termine con otra cadena dada, si es así devuleve true

# termina_con = cadena1.endswith("do")
# print(termina_con)

# Remplaza un pedazo de la cadena dada por otra

# cadena_nueva = cadena1.replace("la", "lu")
# print(cadena_nueva)

# El único metodo que devuelve una matriz (lista) separa cadenas con las que le pasemos

cadena_separada = cadena1.split(" ")
print(cadena_separada[0])


pasar_a_mayus=("2:12:20 - Métodos de listas")
pasar_a_mayus = pasar_a_mayus.upper()
print(pasar_a_mayus)


#NOS QUEDAMOS EN 2:12:20 - MÉTODOS DE LISTAS