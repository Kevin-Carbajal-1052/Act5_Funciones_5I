print("Manejo de funciones V1")
def hola_mundo():
    print("Momo de tuais\n")
def Mensa(msg):
    print(msg+"Maste\n")
def EscribeNC(Nombre,Apellido):
    print(f"Tu nombre completo es {Nombre} {Apellido}\n")
def suma(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y {n2} es de:",s


# Llamando a la funcion
hola_mundo()
Mensa("Llama ") # Llama a mensa con un parametro
EscribeNC("Momo", "de Tuais")
print("Funciones que regresan valores")
print(suma(5,5))