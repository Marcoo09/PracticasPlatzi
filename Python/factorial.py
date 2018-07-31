# -*- coding: utf-8 -*-

def factorial(number):
	if number == 0:
		return 1

	return number * factorial(number - 1)


numero = int(input('Escribe un numero: '))

result = factorial(numero)

print(result)