"""
Calculadora en Python con menú interactivo

Fecha: 13/08/2025
Creador: César Iván Sis Estrada

El programa utiliza un bucle infinito para mostrar el menú hasta que el usuario
decida salir. Se implementa el control de flujo 'match-case' (Python 3.10+)
para seleccionar la operación deseada.

"""

while True: #Se comienza un bucle
    print ("\nCALCULADORA") #Titulo
    print ("1.SUMA") #Opcion numero 1 para sumar
    print ("2.RESTA") #Opcion numero2 para restar
    print ("3.MULTIPLICACION") #Opcion numero 3 para multiplicar
    print ("4.DIVISION") #Opcion numero 4 para dividir
    print ("5.SALIR") #Opcion numero 5 para salir de la calculadora
 
    opcion = int(input("\nSeleccione una opcion: ")) #Se pide que se elija una opcion
 
    match opcion: #Verifica la opcion elegida
        case 5: #Si eligio la quinta opcion, se saldra del programa
            print ("\n¡Gracias por usar el programa!") #Muestra un mensaje de agradeciemiento
            break #Termina el programa
   
    numero1 = float(input("\nIngrese un numero: ")) #Se pide que se ingrese un numero
    numero2 = float(input("Ingrese otro numero: ")) #Se pide que se ingrese otro numero
 
    match opcion: #Verifica la opcion elegida
        case 1: #Si se eligio la primera opcion, se sumara
            suma = numero1 + numero2 #Se realiza la suma
            print ("El resultado de la suma es: ", suma) #Se muestra el resultado de la suma en pantalla
 
        case 2: #Si se eligio la segunda opcion, se restara
            resta = numero1 - numero2 #Se realiza la resta
            print ("El resultado de la resta es: ", resta) #Se muestra el resultado de la resta en pantalla
 
        case 3: #Si se eligio la tercera opcion, se realizara una multiplicacion
            multi = numero1 * numero2 #Se realiza la multiplicacion
            print ("El resultado de la multiplicacion es: ", multi) #Se muestra el resultado de la multiplicacion en pantalla
 
        case 4: #Si se eligio la cuarta opcion, se realizara una division
            match numero2: #Se verifica el numero 2
                case 0: #Si se divide entre 0, no se dividira
                    print ("No se puede dividir entre 0.") #Se muestra un mensaje en pantalla
                case _: #Si se divide por cualquier otro numero, se dividira
                    division = numero1 / numero2 #Se realiza la division
                    print ("El resultado de la division es: ", division) #Se muestra el resultado de la division en pantalla
 
        case _: #Si no se eligio ninguna opcion, se repetira el bucle
            print ("No se eligio ninguna opcion.") #Se muestra un mensaje en pantalla
