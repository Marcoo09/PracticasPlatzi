

KEYS = {
	'a': 'w',
	'b': 'z',
	'c': 't',
	'd': 'p',
	'e': '5',
	'f': 'tz',
	'g': '0',
	'h': '8',
	'i': '@',
	'j': 'e',
	'k': 'c',
	'l': 'b',
	'n': 'm',
	'm': '!',
	'o': '.',
	'p': ',',
	'q': '*',
	'r': '%',
	's': 'a',
	't': 'j',
	'u': ')',
	'v': '=',
	'w': '(',
	'x': '&',
	'y': '$',
	'z': 'º'
}

def cypher(message):
	
	words = message.split(' ')
	cypher_message = []

	for word in words:
		cypher_word = ''
		for letter in word:
			cypher_word += KEYS[letter]

		cypher_message.append(cypher_word)

	return ''.join(cypher_message)

def decypher(message):
	
	words = message.split(' ')
	decypher_message = []

	for word in words:
		decypher_word = ''

		for letter in word:

			for key, value in KEYS.items():
				if value == letter:
					decypher_word += key

		decypher_message.append(decypher_word)	

	return ''.join(decypher_message)			

def run():

	while True:

		command = str(input('''Bienvenido a criptografía que deseas hacer? 
				[c]ifrar mensaje
				[d]ecifrar mensaje
				[s]alir
			'''))

		if command == 'c':
			message = str(input('Escribe tu mensaje: ')).lower()
			cypher_message = cypher(message)
			print(cypher_message)

		elif command == 'd':
			message = str(input('Escribe tu mensaje cifrado: ')).lower()
			decypher_message = decypher(message)
			print(decypher_message)

		elif command == 's':
			print('salir')
		else:
			print('Comando no encontrado')

if __name__ == '__main__':
		run()