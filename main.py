from itertools import count


def contador_digitos(self, numero):
    self.numero = numero
    if numero == 0:
        return
    else:
        contar_numero = count(numero)
        print(f"el total de digitos es: {contar_numero}")

numero = int(input("Ingrese un numero: "))
contador_digitos(numero)

