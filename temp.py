'''
def soma(a, b):
    resultado = a + b
    return resultado

s = soma (1, 2)
print (s)

###

def dobrar_numero():
    numero = float(input("Digite um número: "))
    resultado = numero * 2
    return resultado

print('O dobro do número é: ', dobrar_numero())

###

def somar_numeros():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    return resultado

print('A soma dos números é: ', somar_numeros())

def valor_absoluto():
    numero = float(input("Digite um número: "))
    resultado = abs(numero)
    return resultado

print('O módulo do número é: ', valor_absoluto())

###

def antecessor_numero():
    numero = float(input("Digite um número: "))
    resultado = numero - 1
    return resultado

print('O antecessor do número é: ', antecessor_numero())

###

def buscar_menor():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero1 < numero2
        return numero1
    else:
        return numero2

print('O número menor é: ', buscar_menor())

###


def verificar_par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        return print('O número é par!')
    else:
        return print('O número é ímpar!')

print(verificar_par())

'''

def raizquadrada_numero():
    numero = float(input("Digite um número: "))
    resultado = numero ** 0.5
    return resultado

print('A raiz quadrada do número é: ', raizquadrada_numero())