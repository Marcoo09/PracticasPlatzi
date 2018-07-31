# -*- coding: utf-8 -*- 

countries = {
	'uruguay': 3.5,
	'mexico': 122,
	'eeuu': 300,
	'china':1200,
	'india':1300,
	'peru':31,
	'argentina':43
}

while True:
	country = str(input('Escribe el nombre de un país: ')).lower()

	try:
		print('La población de {} es: {} millones'.format(country ,countries[country]))
	except KeyError:
		print('No tenemos el dato de la población del país {}'.format(country))
		print('---*---- ----*----')
		poblacion = int(input('Escribe la poblacion de {}: '.format(country)))
		countries[country] = poblacion
	
