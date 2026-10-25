###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Router 1"
ubicacio = "Menjador"
nombre_ports = 8
encaminador_engegat = True
print(f"El {nom_encaminador} està a {ubicacio} i té {nombre_ports} ports. Està encès: {encaminador_engegat}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
dades_incloses_gb = 20
dades_consumides_gb = 10
dades_restants_gb = dades_incloses_gb - dades_consumides_gb
print(f"Els GB restants son: {dades_restants_gb} GB")

dades_consumides_gb = 16
dades_restants_gb = dades_incloses_gb - dades_consumides_gb
print(f"Els GB restants despres de l'actualutzació: {dades_restants_gb} GB")
