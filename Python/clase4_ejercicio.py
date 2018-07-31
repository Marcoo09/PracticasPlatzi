# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
	uy_to_arg_rate = 0.5

	return uy_to_arg_rate * ammount
def run():
	print('Calculadora de divisas')
	print('Convierte pesos urugayo a peso argentino')
	print(' ')

	ammount = float(raw_input('Ingresa la cantidad de pesos uruguayo que quieres convertir'))

	result = foreign_exchange_calculator(ammount)

	print('${} pesos uruguayos son ${} argentinos'.format(ammount,result))

	print(' ')
if __name__== 'main':
	run()