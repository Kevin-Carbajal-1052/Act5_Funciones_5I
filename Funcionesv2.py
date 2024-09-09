print("Funciones creadas por el usuario")
# Las funciones
def milista():
    print("LISTAS")
    amigos=["Homero", "Paty", "Lety\n"]
    for momodetuias in amigos:
        print(momodetuias)

#tupla
def mitupla():
    print("TUPLAS")
    frutas=("manzana","pera","sandia\n")
    for frutas2 in frutas:
        print(frutas2)

#diccionario
def diccionario():
    print("DICCIONARIO")
    carros={
        "marca":"Ford",
        "modelo":"Cobra",
        "color":"Azul"
    }
    for runrun in carros:
        print(runrun)

#Conjuntos
def conjunto():
    print("CONJUNTOS")
    conj={"momo","nayon","chayote","dayun"}
    for a in conj:
        print(a)

# Llamadas a funciones
milista()
mitupla()
diccionario()
conjunto()
