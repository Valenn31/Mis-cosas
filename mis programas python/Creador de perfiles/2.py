import os
import keyboard


def borrar_pantalla():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para sistemas tipo Unix (Linux, macOS)
    else:
        os.system('clear')

#Creacion de la clase
class Doc:
    def __init__(self,name,surname,dni,address):
        self.name    = name.capitalize()
        self.surname = surname.capitalize()
        self.dni     = dni
        self.address = address.capitalize()

    def __str__(self):
            return f"""
  ______________________________

    Nombre:     {self.name}
    Apellido:   {self.surname}
    DNI:        {self.dni}
    Dirección:  {self.address} """

def guardar_perfil(doc):
    with open("Creador de perfiles\perfiles.txt", mode="a") as file:
        file.write(f"""
        Nombre:   {doc.name}
        Apellido: {doc.surname}
        DNI:      {doc.dni}
        Direccion {doc.address}\n""")

documentacion = []
resp = "S"
dni = ""

# Funcion para pedir los datos hasta que el usuario diga basta (0 --> 1)

def agregar_perfil():
    borrar_pantalla()
    print("")

    name = input("""  Nombre: """)
    print("______________________")
    print("")

    surname = input("""  Apellido: """)
    print("______________________")
    print("")
    
    dni = (input("""  DNI: """))
    print("______________________")
    print("")

    while len(dni) != 8:
        borrar_pantalla()
        print("")
        print(f"  Nombre: {name}")
        print("______________________")
        print("")
        print(f"  Apellido: {surname}")
        print("______________________")
        print("")
        dni = (input("""  DNI: """))
        print("______________________")
        print("")

    address = input("""  Direccion: """)
    print("______________________")
    borrar_pantalla()

    Docs = Doc(name,surname,dni,address)
    documentacion.append(Docs)
    guardar_perfil(Docs)

#Bucle para la funcion de pedir un usuario + validacion de agregar otro perfil

while resp.lower() == "s":
    agregar_perfil()
    resp = input("Desea realizar otra carga de datos? S/N: ")

    while resp.lower() != "s" and resp.lower() != "n":
        borrar_pantalla()
        print("Opción inválida. Por favor, ingrese 'S' para sí o 'N' para no.")
        resp = input("Desea realizar otra carga de datos? S/N: ")

# Mostrar los perfiles creados
borrar_pantalla()
for Doc in documentacion:
     print(Doc)

# Salir del programa (libreria keyboard)
print("""  ______________________________""")
print("")
print("  Presiona Enter para salir...")
keyboard.wait('enter')  # Espera a que el usuario presione Enter
