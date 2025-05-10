from colorama import init, Fore
import textwrap 
init() 

def ajustes(texto, ancho=118):
    return textwrap.fill(texto, width=ancho)

print("Hola, bienvenido a la versión 1.1 de Mathex, la IA experta en mates creada por Hammett23.")
print("En esta versión aparte de poder sumar y restar, también es capaz de multiplicar y dividir pero tú me tienes que decir los datos necesarios para calcularla.")

while True:
    a = input(ajustes("¿Qué quieres hacer? Calcular " + Fore.CYAN + "a) sumas " + Fore.RESET + ", " + Fore.CYAN + "b) restas" + Fore.RESET +", " + Fore.CYAN + "c) multiplicaciones " + Fore.RESET + "o " + Fore.CYAN + "d) divisiones" + Fore.RESET + ":  ", ancho=127)).lower()
    
    if a == "sumas" or a == "a":
        print(ajustes("Perfecto, ahora tienes que ingresar un número en donde pone 'Ingresa 1er número' y después darle al enter. Luego te pondrá 'Ingresa 2do número' y haz lo mismo. Tras esto, yo sumaré los números ingresados y te saldrá 'La respuesta es: respuesta123' y ya lo tienes calculado. ", ancho=150))
        print(ajustes(Fore.RED + "ADVERTENCIA: Los números decimales se ponen con punto, no con coma. " + Fore.GREEN + "✔ " + Fore.RESET + "2.5 " + Fore.RED + "✘ " + Fore.RESET + "2,5", ancho=150))
        primero = input("Ingresa 1er número: ")
        segundo = input("Ingresa 2do número: ")
        if "." in primero or "." in segundo:
                suma = float(primero) + float(segundo)
                print("La respuesta es:", suma)
        else:
                suma = int(primero) + int(segundo)
                print("La respuesta es:", suma)        
            
        
    
    elif a == "restas" or a == "b":
        print(ajustes("Perfecto, ahora tienes que ingresar un número en donde pone 'Ingresa 1er número' y después darle al enter. Luego te pondrá 'Ingresa 2do número' y haz lo mismo. Tras esto, yo sumaré los números ingresados y te saldrá 'La respuesta es: respuesta123' y ya lo tienes calculado. ", ancho=150))
        print(ajustes(Fore.RED + "ADVERTENCIA: Los numeros decimales se ponen con punto, no con coma. " + Fore.GREEN + "✔ " + Fore.RESET + "2.5 " + Fore.RED + "✘ " + Fore.RESET + "2,5", ancho=150))
        primero = input("Ingresa 1er número: ")
        segundo = input("Ingresa 2do número: ")
        if "." in primero or "." in segundo:
                resta = float(primero) - float(segundo)
                print("La respuesta es:", resta)
        else:
                resta = int(primero) - int(segundo)
                print("La respuesta es:", resta)        
            
    
    elif a == "multiplicaciones" or a == "c":
        print(ajustes("Perfecto, ahora tienes que ingresar un número en donde pone 'Ingresa 1er número' y después darle al enter. Luego te pondrá 'Ingresa 2do número' y haz lo mismo. Tras esto, yo sumaré los números ingresados y te saldrá 'La respuesta es: respuesta123' y ya lo tienes calculado.", ancho=150))
        print(ajustes(Fore.RED + "ADVERTENCIA: Los números decimales se ponen con punto, no con coma. " + Fore.GREEN + "✔ " + Fore.RESET + "2.5 " + Fore.RED + "✘ " + Fore.RESET + "2,5", ancho=150))
        primero = input("Ingresa 1er número: ")
        segundo = input("Ingresa 2do número: ")
        if "." in primero or "." in segundo:
            multiplicación = float(primero) * float(segundo)
            print ("La respuesta es:", multiplicación)
        else:
            multiplicación = int(primero) * int(segundo)
            print ("La respuesta es:", multiplicación) 
    
    elif a == "divisiones" or a == "d":
        print(ajustes("Perfecto, ahora tienes que ingresar un número en donde pone 'Ingresa 1er número' y después darle al enter. Luego te pondrá 'Ingresa 2do número' y haz lo mismo. Tras esto, yo sumaré los números ingresados y te saldrá 'La respuesta es: respuesta123' y ya lo tienes calculado.", ancho=150))
        print(ajustes(Fore.RED + "ADVERTENCIA: Los números decimales se ponen con punto, no con coma. " + Fore.GREEN + "✔ " + Fore.RESET + "2.5 " + Fore.RED + "✘ " + Fore.RESET + "2,5", ancho=150))
        primero = input("Ingresa 1er número: ")
        segundo = input("Ingresa 2do número: ")
        if "." in primero or "." in segundo:
            división = float(primero) / float(segundo)
            print ("La respuesta es:", división)
        else:
            división = int(primero) / int(segundo)
            print ("La respuesta es:", división)    
        
    else:
        print(ajustes("Lo siento, no identifico '" + a + "' como una respuesta válida. Para sumar tienes que poner 'sumas' o 'a', 'restas' o 'b' para restar, 'multiplicaciones' o 'c' para multiplicar y 'divisiones' o 'd' para dividir", ancho=150))
        continue 

    while True:
        b = input(ajustes("¿Qué quieres hacer ahora?: " + Fore.CYAN + "a) otra operación " + Fore.RESET + "o " + Fore.CYAN + "b) finalizar conversación" + Fore.RESET + ": ", ancho=118)).lower()

        if b == "otra operación" or b == "a":
            break
        
        elif b == "finalizar conversación" or b == "b":
            print("Gracias por usar Mathex, ojalá que podamos volver a hablar. ")
            print (Fore.GREEN + "Hammett23 © 2025. Este programa está protegido por derechos de autor.")
            print(Fore.GREEN +"Prohibida su modificación, reproducción o distribución sin autorización del autor.")
            exit_main = True
            break
        
        else:
            print(ajustes("Lo siento, no identifico '" + b + "' como una respuesta válida. Si quieres hacer otra operación tienes que poner 'otra operación' o 'a'. Si quieres finalizar la conversación tienes que poner 'finalizar conversación' o 'b'.", ancho=118))

    if 'exit_main' in locals() and exit_main:
        break
