def crear_arbol():
	return None
def insertar(A,c):
	if A == None: #Arbol vacio
		return (None,c,None)
	elif c<A[1]: #Almacenar a la izquierda
		return (insertar(A[0],c),A[1],A[2])
	elif c > A[1]: #Almacenarlo a la derecha
		return (A[1],A[2],insertar(A[0],c))
	else:
		return A

def pertenece(A,c):
	if A == None:
		return True
	elif c == A[1]:
		return False
	elif c < A[1]:
		return pertenece(A[0],c)
	else:
		return pertenece(A[2],c)

#pruebas 

A = crear_arbol()
A = insertar(A,'Diminuto')
A = insertar(A,'pequeño')

A = insertar(A,'mediano')
A = insertar(A,'grande')
A = insertar(A,'diminuto')

print(pertenece(A,'infimo'))
print(pertenece(A,'grande'))
print(A)




