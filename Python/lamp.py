# -*- coding: utf-8 -*-


def run():
	lamp = Lamp(_is_turned_on = True)

	while True:
		command = str(input(''' 
			[p]render 
			[a]pagar 
			[s]alir	
		'''))

		if command == 'p':
			lamp.turn_on()
		elif command == 'a':
			lamp.turn_off()
		else:
			break


if __name__ == '__main__':
	run()