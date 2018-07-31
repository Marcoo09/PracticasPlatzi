# -*- coding: utf-8 -*-

import io

def run():
	with open('numeros.txt','w') as f:
		for i in range(1000):
			f.write(str(i))

if __name__ == '__main__':
	run()