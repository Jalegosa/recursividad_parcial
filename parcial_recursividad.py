#ninguno está bueno no tienes que usar ciclos y bucles solo funciones
#quitar el match case y dejarlo con otro para que sea un menu y que el usuario esoja las opciones


def mcd_numeros():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    while b != 0:
        a, b = b, a % b
    print(f"El MCD es: {a}")



def repetir_palabra():
    palabra = input("Ingrese una palabra: ")
    n = int(input("¿Cuántas veces desea repetirla?: "))
    print((palabra + '\n') * n)



def contar_letra():
    palabra = input("Ingrese la cadena: ")
    letra = input("Ingrese la letra a contar: ")
    if len(letra) != 1:
        print("Debe ingresar solo una letra.")
    else:
        cantidad = palabra.count(letra)
        print(f"La letra '{letra}' aparece {cantidad} veces.")



def decimal_a_binario():
    numero = int(input("Ingrese un número decimal: "))
    binario = bin(numero)[2:]
    print(f"El número binario es: {binario}")


def contador_digitos():
    numero = int(input("Ingrese un número: "))
    total = len(str(abs(numero)))
    print(f"El número tiene {total} dígitos.")



def salir():
    print("Programa finalizado.")


def menu():
    print("\n--- MENÚ ---")
    print("1. Máximo Común Divisor (MCD)")
    print("2. Repetir palabra N veces")
    print("3. Contar una letra en una palabra")
    print("4. Convertir decimal a binario")
    print("5. Contar los dígitos de un número")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mcd_numeros()
    elif opcion == "2":
        repetir_palabra()
    elif opcion == "3":
        contar_letra()
    elif opcion == "4":
        decimal_a_binario()
    elif opcion == "5":
        contador_digitos()
    elif opcion == "6":
        salir()
    else:
        print("Opción inválida.")
        menu()


# Iniciar el programa
menu()
