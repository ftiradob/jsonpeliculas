import json

def listar(doc):
    for i in doc:
        print("Título: ",i["title"])
        print("Año: ",i["year"])
        print("Duración: ",i["duration"])
        print("")

def cuentaactores(doc):
    for i in doc:
        print("Título: ",i["title"])
        print("Número de actores/actrices: ",len(i["actors"]))
        print("")

with open("movies.json") as pelis:
    doc=json.load(pelis)

print("")
while True:
    print("1. Listar el título, año y duración de todas las películas.")
    print("2. Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.")
    print("3. Mostrar las películas que contengan en la sinopsis dos palabras dadas.")
    print("4. Mostrar las películas en las que ha trabajado un actor dado.")
    print("5. Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.")
    print("0. Salir")
    opcion=int(input("Elija opción: "))

    if opcion==1:
        print("")
        listar(doc)
    elif opcion==2:
        print("")
        cuentaactores(doc)
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")