from colorama import Fore, Back, Style
import datetime
import speech_recognition as sr

contCiclo = 0
asignacionesAnteriores = None

def asignaciones():
    """
    En esta función se asigna la persona que va a hacer uso de la palabra, el punto y apartado de la agenda, hora de inicio
    para que luego se llame a la función encargada de transcribir la voz a texto.
    Luego de Solicitar los miembros, los partados y puntos de la agenda genera un indice mediante el cual el usuario sea capaz de seleccionar
    dichos datos facilmente.

    Retorna una tupla con los siguientes valores:
        participantes: una lista de los nombres de los participantes
        apartadoAgenda: una cadena que contiene el apartado de la agenda que se va a tratar
        punto: una cadena que contiene el punto específico que se va a tratar
        indiceParticipantes: un entero que representa el índice de la persona que va a hablar.
    """
    from participantes import registroParticipantes as miembros
    from agenda import agendaSesion as ag
    
    global contCiclo, asignacionesAnteriores
    if contCiclo == 0:
        participanteSesion = miembros()
        agenda = ag()
        asignacionesAnteriores = (participanteSesion, agenda)
        contCiclo = 1
    else:
        participanteSesion, agenda = asignacionesAnteriores

    participantes = participanteSesion
    print(Fore.YELLOW + "\nÍndice de participantes:")
    for i, participante in enumerate(participantes):
        print(f"[{i+1}] {participante}") #Muestra el índice

    print()
    indiceParticipantes = int(input(Fore.YELLOW + "Ingrese el índice del participante que va a hablar: " + Fore.WHITE))
    if indiceParticipantes < 1 or indiceParticipantes > len(participantes):
        print(Fore.RED + "Índice de participante fuera de rango")
        return

    print("\033c",end="") #Borra la consola

    # Imprimir la agenda completa
    print(Fore.YELLOW + "Índice de la agenda: ")
    print("".center(50)) #Imprime un espacio en blanco
    seccion = 1
    for apartado, puntos in agenda.items():
        print(f"[{seccion}] [{apartado}]:")
        puntoNum = 1
        for punto in puntos:
            print(Fore.YELLOW + f"\t[{seccion}.{puntoNum}] {punto}")
            puntoNum += 1
        seccion += 1

    indice = input(Fore.YELLOW + "Ingrese el punto de la agenda a tratar (por ejemplo, 1.2): " + Fore.WHITE)
    seccion, punto = indice.split(".")
    seccion = int(seccion) - 1
    punto = int(punto) - 1

    if seccion >= len(agenda):
        print(Fore.RED + "Índice de sección fuera de rango")
        return
    if punto >= len(agenda[list(agenda.keys())[seccion]]):
        print(Fore.RED + "Índice de punto fuera de rango")
        return

    punto = agenda[list(agenda.keys())[seccion]][punto]
    apartadoAgenda = list(agenda.keys())[seccion]

    return participantes, apartadoAgenda, punto, indiceParticipantes
    print("\033c",end="") #Borra la consola




def main():
    """
    es el punto de entrada del programa y es donde se ejecuta la lógica principal del mismo. En primer lugar, 
    se inicializan dos variables: registros es una lista que almacenará todas las intervenciones realizadas 
    durante la sesión y totalPalabras es un diccionario que almacenará la cantidad total de palabras que ha dicho cada participante.

    A continuación, se inicia un bucle while True que se ejecutará hasta que el usuario decida terminar la sesión.
    En cada iteración del bucle se solicita al usuario que introduzca la información correspondiente a la intervención realizada 
    por el participante (mediante la función asignaciones()), se reconoce el audio de la intervención (mediante la función reconocimientoVoz()), 
    se calcula la cantidad de palabras dichas y se almacena toda esta información en la lista registros. También se actualiza el diccionario totalPalabras 
    con la cantidad de palabras dichas por el participante en la intervención actual.

    Después de cada intervención, se le pregunta al usuario si desea continuar con la sesión o terminarla.
    Si el usuario decide terminar la sesión, se ordena el diccionario totalPalabras por la cantidad de palabras dichas por cada participante
    en orden descendente y se muestran en pantalla tanto los registros de la sesión como el total de palabras dichas por cada participante.

    """

    registros = []
    totalPalabras = {}

    while True:
        participantes, apartadoAgenda, punto, indiceParticipantes = asignaciones()

        print("\033c",end="") #Borra la consola
        #Impresiones en pantalla
        hablante = participantes[indiceParticipantes-1]
        print(Fore.YELLOW + f"\nParticipante: {Fore.WHITE + hablante}")
        print(Fore.YELLOW + f"Apartado: {Fore.WHITE + apartadoAgenda}")
        print(Fore.YELLOW + f"Punto: {Fore.WHITE + punto}")


        from vozATexto import reconocimientoVoz
        transcripcion = reconocimientoVoz()
        transcripcion = ' '.join(transcripcion)
        cantidadPalabras = len(transcripcion.split())

        hora = datetime.datetime.now().strftime("%H:%M:%S")
        registros.append((hablante, apartadoAgenda, punto, hora, transcripcion, cantidadPalabras))

        # Suma las palabras dichas por participante
        if hablante in totalPalabras:
            totalPalabras[hablante] += cantidadPalabras
        else:
            totalPalabras[hablante] = cantidadPalabras

        print(Fore.YELLOW + "[1] Sí")
        print(Fore.YELLOW + "[2] No")
        estado = int(input(Fore.YELLOW + "¿Continua la sesión?: " + Fore.WHITE))
        if estado == 1:
            print("\033c",end="") #Borra la consola
            pass

        else:
            print("\033c",end="") #Borra la consola
            break

    # Ordenar por cantidad de palabras dichas en orden descendente
    totalPalabras = dict(sorted(totalPalabras.items(), key=lambda x: x[1], reverse=True))

    # Registro de la sesión
    print(Fore.GREEN + "\n\n--- Reporte de la sesión ---\n")
    for registro in registros:
        print(Fore.YELLOW + f"Participante: {Fore.WHITE + registro[0]}")
        print(Fore.YELLOW + f"Apartado: {Fore.WHITE + registro[1]}")
        print(Fore.YELLOW + f"Punto: {Fore.WHITE + registro[2]}")
        print(Fore.YELLOW + f"Hora: {Fore.WHITE + registro[3]}")
        print(Fore.WHITE + f"Transcripción:\n{registro[4]}\n")
        print(Fore.YELLOW + f"Cantidad de palabras: {len(registro[4].split())}\n")

    # Mostrar total de palabras dichas por participante en orden descendente
    print(Fore.GREEN + "\n\n--- Total de palabras dichas por participante ---\n")
    for participante, total in totalPalabras.items():
        print(Fore.YELLOW + f"{participante}: {total}")






main()

