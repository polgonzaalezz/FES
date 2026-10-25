###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Pol Gonzalez")
print("Cerdanyola")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print("Tipus de a:", type(a))
print("Tipus de b:", type(b))
print("Tipus de c:", type(c))
print("Tipus de d:", type(d))
print("Tipus de e:", type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

cadena = 12345
cadena_enter = int(cadena)
cadena_decimal = float(cadena_enter)

print("Nombre enter:", cadena_enter)
print("Nombre decimal:", cadena_decimal)

nombre = 3.99
nombre_convertit = int(nombre)

print("Nombre decimal original:", nombre)
print("Nombre decimal convertit a enter (se n'elimina la part decimal):", nombre_convertit)


print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí
nom = "Marc"
edad = 40
alcada = 1.75

print(f"Hola! Em dic {nom}, tinc {edad} i faig {alcada}")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

resultat = int(round(3.1416) / 2)
print("Valor aproximat de PI:", 3.1416)
print("PI arrodonit:", round(3.1416))
print("Divisió de PI arrodonit entre 2:", resultat)


print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

celsius = float(input("Introdueix la temperatura en °C: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

total_compte = float(input("Introdueix l'import total del compte: "))
percentatge_propina = float(input("Introdueix el percentatge de propina: "))

propina = total_compte * (percentatge_propina / 100)
total_final = total_compte + propina

print(f"Propina: {propina:.2f} €")
print(f"Total a pagar: {total_final:.2f} €")


print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
contrasenya = input("Introdueix una contrasenya: ")

if len(contrasenya) >= 8:
	print("Contrasenya vàlida")
else:
	print("Contrasenya no vàlida")