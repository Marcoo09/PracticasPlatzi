

def first_not_repeting_char(char_sequence):
	
	seen_letters = {}

	''' This for get the letters for the sequence and save in a dictionary the index and the repetitions of each letter of the sequence '''
	for idx,letter in enumerate(char_sequence):
		if letter not in seen_letters:
			seen_letters[letter] = (idx, 1)
		else:
			seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)
	
	final_letters = []

	''' This for  go through the key and value of each item of the dictionary evaluate if the letter is repetead and if it's true save it in a list'''
	for key, value in seen_letters.items():
		if value[1] == 1:
			final_letters.append((key, value[0]))

	''' This line use the sorted function to sort the list for the index (in the initial sequence) of the letter '''
	not_repeted_letters = sorted(final_letters, key = lambda value: value[1])

	''' This conditional evaluate if the variable not_repetead_letters have items or not and if true return the character of this item '''
	if not_repeted_letters:
		return not_repeted_letters[0][0]
	else:
		return '_'

if __name__ == '__main__':
	char_sequence= str(input('Escribe una secuencia de caracteres: '))

	result = first_not_repeting_char(char_sequence)

	''' This if evaluate the response of the function first_not_repeting_char saved in the variable which is called result'''
	if result == '_':
		print('Todos los caracteres se repiten.')
	else:
		print('El primer caracter que no se repite es: {}'.format(result))