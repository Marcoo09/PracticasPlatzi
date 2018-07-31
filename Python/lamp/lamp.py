# -*- coding: utf-8 -*-

import os as os

LAMPS = ['''
              .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''',
        '''
             ,-.
            (   )
             \ /
            _|=|_
           |_____|

    ''']


class Lamp:


	def __init__(self, _is_turned_on):
		self._is_turned_on = _is_turned_on

	def turn_on(self):
		self._is_turned_on = True
		os.system('cls')
		self.display_image()

	def turn_off(self):
		self._is_turned_on = False
		os.system('cls')
		self.display_image()

	def display_image(self):
		if self._is_turned_on:
			print(LAMPS[0])
		else:
			print(LAMPS[1])

