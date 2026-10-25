###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
print("\nExercici 1:")
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

if num1 > num2:
    print(f"{num1} és més gran que {num2}")
elif num1 < num2:
    print(f"{num2} és més gran que {num1}")
else:
    print(f"{num1} i {num2} son iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
num1 = float(input("Primer nombre: "))
num2 = float(input("Segon nombre: "))
operacio = input("Introdueix l'operació (+, -, *, /): ").strip()

if operacio == "/" and num2 == 0:
    print("Error: no es pot dividir per zero.")
elif operacio == "+":
    resultat = num1 + num2
    print(f"El resultat és: {resultat}")
elif operacio == "-":
    resultat = num1 - num2
    print(f"El resultat és: {resultat}")
elif operacio == "*":
    resultat = num1 * num2
    print(f"El resultat és: {resultat}")
elif operacio == "/":
    resultat = num1 / num2
    print(f"El resultat és: {resultat}")
else:
    print("Operació no vàlida.")


# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
any = int(input("Introdueix un any: "))

if (any % 4 == 0 and any % 100 != 0) or any % 400 == 0:
    print(f"L'any {any} és de traspàs.")
else:
    print(f"L'any {any} no és de traspàs")


# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Introdueix la teva edat: "))

if 0 <= edat <= 2:
    print("Nadó")
elif 3 <= edat <= 12:
    print("Infant")
elif 13 <= edat <= 17:
    print("Adolescent")
elif 18 <= edat <= 64:
    print("Adult")
elif edat >= 65:
    print("Persona gran")
else:
    print("Edat no vàlida.")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = float(input("Introdueix el nivell de senyal RSSI en dBm: "))

if rssi >= -50:
    print("Cobertura excel·lent.")
elif rssi >= -67:
    print("Cobertura bona.")
elif rssi >= -75:
    print("Cobertura feble.")
else:
    print("Cobertura molt feble.")


# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Introdueix la potència òptica rebuda en dBm: "))

if potencia < -27:
    print("El nivell és massa baix.")
elif potencia <= -8:
    print("El nivell és acceptable.")
else:
    print("El nivell és massa alt.")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum_gb = float(input("Introdueix el consum mensual de dades en GB: "))

if consum_gb <= 20:
    print("El consum està dins del límit de 20 GB.")
else:
    extra_gb = consum_gb - 20
    print(f"S'ha superat el límit en {extra_gb:.2f} GB.")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los_encès = input("L'indicador LOS està encès? (s/n): ").strip().lower()
internet_encès = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()

if los_encès == "s":
    print("Cal revisar el cable de fibra.")
elif internet_encès != "s":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = float(input("Introdueix el percentatge de bateria del SAI: "))

if bateria < 0 or bateria > 100:
    print("El percentatge ha d'estar entre el 0 % i el 100 %.")
elif bateria < 20:
    print("Nivell de bateria crític.")
elif bateria < 50:
    print("Nivell de bateria baix.")
else:
    print("Nivell de bateria suficient.")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.



# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.



# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.



# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.



# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.


