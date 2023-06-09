from colorama import Fore, Back, Style
import datetime
import speech_recognition as sr

def reconocimientoVoz():
    """
    Esta función se encarga de realizar la trascripción de voz a texto

    return:
    l: lista en la cual se guarda todo lo que dice la persona que tiene la palabra 
    """
    r = sr.Recognizer()
    cont=0
    l=[]
    with sr.Microphone() as source:
        while cont<10:
            print()
            print (Fore.YELLOW + "Intervención:\n")
            print(Fore.YELLOW + "Di algo...")
            audio = r.listen(source)
            cont=cont+1
            try:
                print("\033c",end="") #Borra la consola
                print(Fore.YELLOW + "inicia el reconocimiento...\n")
                horaActual = datetime.datetime.now().time() #Acceder a la hora
                horaActualStr = horaActual.strftime("%H:%M:%S")
                text = r.recognize_google(audio, language='es-ES')
                print(Fore.YELLOW + "Hora: ", Fore.WHITE + horaActualStr)
                print(Fore.YELLOW + "Has dicho: " + Fore.WHITE +text)
                l.append(text)
                print()
                print(Fore.YELLOW + "[1] Sí")
                print(Fore.YELLOW + "[2] No")
                palabra = int(input(Fore.YELLOW + "¿Sigue el miembro actual haciendo uso de la palabra?: " + Fore.WHITE))
                if palabra == 1:
                    print("\033c",end="") #Borra la consola
                    pass
                else:
                    print("\033c",end="") #Borra la consola
                    break

            except sr.UnknownValueError:
                print("No se pudo reconocer el audio.")
            except sr.RequestError as e:
                print("No se pudo obtener respuesta desde el servicio de Google Speech Recognition: {0}".format(e))
    return(l)
    
