from colorama import Fore, Back, Style

def registroParticipantes ():                                                           
    """
    Esta función se encarga de solicitar los miembros de la sesion y almacenarlos dentro de la lista participantes, una vez el ciclo detecta que 
    la longitud de el nuevo nombre ingresado corresponde a 0, automaticamente detiene la solicitud de nombres 
    """

    participantes = []
    nombreLen = 1
    cont = 1

    print("\033c",end="") #Borra la consola
    print("".center(50)) #Imprime un espacio en blanco
    print( Fore.YELLOW + "Ingrese el nombre completo de los participantes, en caso de completar la lista con los participantes solamente digite la tecla Enter")
    print(Style.RESET_ALL)
    print("".center(50))#Imprime un espacio en blanco

    indice = 1
    while nombreLen != 0:
        nombre = str(input(Fore.YELLOW + "Participante {}: ".format(indice) + Fore.WHITE))
        nombreLen = len(nombre)
        if nombreLen > 0:
            participantes.append(nombre)
            indice += 1
    

    print("\033[F\033[K", end="") # Mover el cursor a la línea anterior y borrar la línea anterior
    print("\033c",end="") #Borra la consola

    return participantes