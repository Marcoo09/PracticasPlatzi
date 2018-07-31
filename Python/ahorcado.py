import random
import os
os.system('cls')

IMAGES = ['''
|  
|   
|  
|  
| 
'''
,'''
|  
|  0 
|  
|  
| 
'''
,'''
|  
|  0 
| / 
|  
| 
'''
,'''
|  
|  0 
| /| 
|  
| 
'''
,'''
|  
|  0 
| /|\ 
|  
| 
'''
,'''
|  
|  0 
| /|\ 
| / 
| 
'''
,'''
|  
|  0 
| /|\ 
| / \ 
| 
''']

WORDS = ['computadora', 
		 'lavadora',
 		 'queso', 
		 'rico'
		]
def random_word():
	index = random.randint(0, len(WORDS) - 1)
	return WORDS[index]

def display_board(hidden_word, tries):
	os.system('cls')
	print(IMAGES[tries])
	print('')
	print(hidden_word)
	print('--- * ---- * ---- * --- * --- * ---')

def run():
	word= random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word, tries)
		current_letter = str(input('Elige una letra: '))

		letter_indexes = list()

		for i in range(len(word)):
			if word[i] == current_letter:

				if hidden_word[i] == current_letter:
					break
				else:	
					letter_indexes.append(i)

		if len(letter_indexes) == 0:
			tries += 1
			if tries == 6:
				display_board(hidden_word, tries)
				print('')
				print('Perdiste! La palabra correcta era: {}'.format(word))
				break

		else:
			for i in letter_indexes:	
				hidden_word[i] = current_letter	

			letter_indexes = list()
		
		try:
			hidden_word.index('-')
		except ValueError:
			print('')
			print('Ganaste!La palabra correcta era: {}'.format(word))	
			break

if __name__ == '__main__':
	print('B I E N V E N I D O S al AHORCADOS')
	run()