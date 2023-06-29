"""Funciones del sistema"""

def validarOpc(tipo,texto,min=None,max = None):
    while True:
        try:
            opc = tipo(input(texto))
            if min and max:
                if min <= opc <= max:
                    break
                else:
                    print("Valor fuera de rango")
            else:
                break
        except:
            print("Ha ingresado un valor no valido")
    return opc

def validarRut(texto,min=None,max = None):
    while True:
        try:
            opc = int(input(texto))
            if min <= opc <= max:
                break
            else:
                print("Rut ingresado no es valido")
        except:
            print("Ha ingresado un valor no valido")
    return opc

def validarLen(tipo,texto,min=None):
    while True:
        try:
            nombre = tipo(input(texto))
            if len(nombre) >= min:
                break
            else:
                print(f"El nombre debe contener al menos {min} caracteres")
        except:
            print("Valor ingresado no valido")
    return nombre

def validarCorreo(texto,min=None):
    while True:
        try:
            correo = input(texto)
            if "@" in correo:
                if "." in correo:
                    break
                else:
                    print("El correo debe contener un (.)")
            else:
                print("El correo ingresado no contiene '@'")
        except:
            print("Valor ingresado no valido")
    return correo

def imprimirMenu():
    print("_____Bienvenidx_____")
    print("Elija una opción :")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir parejas")
    print("4. Salir")
    opc = validarOpc(int,"Opción > ",1,4)
    return opc

# Opción 1
# Grabar: Corresponde a guardar los datos de un jugador, entre ellos: 
# Nombre del jugador, rut, fecha de nacimiento, categoría (Oro – Plata - Bronce),
# celular, identificador de parejas (nombre que le fue asignado a la pareja que 
# compite). Además, debe validar que el nombre contenga al menos dos caracteres, 
# que no tenga más de 80 años, correo contenga @ y largo mínimo 6.
def grabarJugador(jugadores):
    jugador = []
    nombre = validarLen(str,"Ingrese nombre de jugador > ",2)
    rut = validarRut("Ingrese su rut sin digito verificador > ",5000000,90000000)
    nacimiento = validarOpc(int,"Ingrese año de nacimiento : ", 1943, 2015)
    categoria = validarOpc(int,"Ingrese categoría:\n1.Oro\n2.Plata\n3.Bronce\n > ",1,3)
    if categoria == 1:
        categoria = str("Oro")
    elif categoria == 2:
        categoria = str("Plata")
    elif categoria == 3:
        categoria = str("Bronce")
    celular = validarOpc(int,"Ingrese numero de celular > ",50000000,99999999)
    correo = validarCorreo("Ingrese correo > ",6)
    id_pareja = validarLen(str,"Ingrese nombre de grupo > ",2)
    jugador.append(rut)
    jugador.append(nombre)
    jugador.append(nacimiento)
    jugador.append(categoria)
    jugador.append(celular)
    jugador.append(correo)
    jugador.append(id_pareja)
    print(jugador)
    print(f"Jugador agregado correctamente")
    jugadores.append(jugador)
    return jugadores

# Opción 2
# ● Buscar: Corresponde buscar un participante por su por rut y mostrar su nombre,
# categoría, fono y correo.
def buscarParticipante(jugadores):
    if len(jugadores) != 0:
        rut = validarRut("Ingrese su rut de participante a busca > ",5000000,90000000)
        for i in range(len(jugadores)):
            for j in jugadores:
                if j[0] == rut:
                    print("Jugador encontrado!")
                    print(f"NOMBRE : {j[1]}")
                    print(f"CATEGORIA : {j[3]}")
                    print(f"FONO : {j[4]}")
                    print(f"CORREO : {j[5]}")
    else:
        print("La lista de jugadores está vacía")

# Opción 3
# ● Imprimir Parejas: Corresponde buscar por el identificador de parejas 
# y mostrar los nombres de los integrantes del equipo.
def imprimirPareja(jugadores):
    if len(jugadores) != 0:
        id_pareja = validarLen(str,"Ingrese nombre de grupo > ",2)
        for i in range(len(jugadores)):
            for j in jugadores:
                if j[6] == id_pareja:
                    print(f"NOMBRE : {j[1]}")
    else:
        print("La lista de jugadores está vacía")