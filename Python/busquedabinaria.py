# -*- coding: utf-8 -*-

def binary_search(numbers_sort,number_to_find,low, high):

	if low > high:
		return False

	mid = int((low + high) / 2)

	if numbers_sort[mid] == number_to_find:
		return True

	elif numbers_sort[mid] > number_to_find:
		return binary_search(numbers_sort, number_to_find,0,mid - 1)

	else:
		return binary_search(numbers_sort,number_to_find,mid + 1, high)

if __name__ == '__main__':

	numbers = [2,3,4,8,9,11,301,15,16,28,35,49,51,65,98,99,101,109,251,110,152,108,55,36,37,33,250,199,500,300,450,400,100,399,1] 

	numbers.sort()

	number_to_find = int(input('Ingrese un número: '))

	result = binary_search(numbers ,number_to_find, 0 , len(numbers) - 1)

	if result == True:
		print('El número si está en la lista')
	else:
		print('El número no está en la lista')