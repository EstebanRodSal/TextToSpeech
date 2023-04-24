from colorama import Fore, Back, Style

def agendaSesion():
    """Agenda que permite al usuario incluir apartados y puntos para cada apartado"""
    agenda = {}
    cont = 1

    print("\033c",end="") #Borra la consola

    while True:

        print("".center(50)) #Imprime un espacio en blanco
        print(Fore.YELLOW + f"Ingrese el apartado de la agenda o digite la tecla {Style.BRIGHT + Fore.WHITE}Enter{Style.NORMAL + Fore.YELLOW} para terminar")
        print("".center(50)) #Imprime un espacio en blanco
        
        # Solicitar el apartado
        apartado = input("Apartado: " + Fore.WHITE)
        apartadoLen = len(apartado)
        print("\033c",end="") #Borra la consola

        # Si el usuario ingresa "terminar", se finaliza el proceso de ingreso de la agenda
        if apartadoLen == 0:
            print("\033[F\033[K", end="") # Mover el cursor a la línea anterior y borrar la línea anterior
            print("".center(50)) #Imprime un espacio en blanco
            break
            

        # Si el apartado no existe en la agenda, se crea un nuevo subdiccionario para ese apartado
        if apartado not in agenda:
            agenda[apartado] = []


        print("\033[F\033[K", end="") # Mover el cursor a la línea anterior y borrar la línea anterior
        print("".center(50)) #Imprime un espacio en blanco
        print(Fore.YELLOW + f"Ingrese los puntos para el apartado {Fore.WHITE + Style.BRIGHT + apartado + Style.NORMAL + Fore.YELLOW} o digite la tecla {Style.BRIGHT + Fore.WHITE}Enter{Style.NORMAL + Fore.YELLOW} para terminar")
        print("".center(50)) #Imprime un espacio en blanco
        # Solicitar los puntos dentro del apartado
        while True:
            
            
            punto = input(Fore.YELLOW + f"Punto: " + Fore.WHITE)
            puntoLen = len(punto)

            # Si el usuario ingresa "terminar", se finaliza el ingreso de puntos para ese apartado
            if puntoLen == 0:
                print("\033[F\033[K", end="") # Mover el cursor a la línea anterior y borrar la línea anterior
                print("\033c",end="") #Borra la consola
                
                break
                
                

            # Agregar el punto al subdiccionario correspondiente
            agenda[apartado].append(punto)


    return agenda
