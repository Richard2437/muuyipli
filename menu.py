# _*_ coding: utf-8 -*-

"""====================================================================== 
                       Calculadora simple -MENU

                       


    Este programa es una calculadora con un menu interactivo que permite 
    realizar operaciones basicas suma, resta, multiplicacion, division

    autor: yo
    fecha: hoy
    """

#crear un bucle


 
# Crear un bucle infinito para mostrar el menu hasta que el usuario desea salir
 
while True:
    print("\n=== MENU DE CALCULADORA ===")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. salir")
 
    #solicitar al usuario que seleccione una opcion del menu
    opcion=input("Selecione una opcion del (1-5)")
 
    #============OPERACIONES=============
 
    # Opcion 1: sumar
    if opcion == '1':
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        resultado= num1+num2
        print(f"la suma de {num1} y {num2} es: {resultado}")
 
    # Opcion 2: restar
    if opcion == '2':
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        resultado= num1-num2
        print(f"la suma de {num1} y {num2} es: {resultado}")
 
    # Opcion 3: multiplicar
    if opcion == '3':
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        resultado= num1*num2
        print(f"la suma de {num1} y {num2} es: {resultado}")
 
    # Opcion 4: division
    if opcion == '4':
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        resultado= num1/num2
        print(f"la suma de {num1} y {num2} es: {resultado}")
 
    #Opcion 5: salir
    elif opcion == '5':
        print("saliendo del programa. ¡hasta luego!")
        break
 
    #Opcion no valida
    else:
        print("Opcion no valida, elija una opcion del 1-5")
 
    #Se agrega una pausa para que el usuario pueda ver el resultado antes de continuar
    input("Presione enter para continuar.")
 

    input("presione enter para continuar...")