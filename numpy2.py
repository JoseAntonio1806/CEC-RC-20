import numpy as np
array = np.array([(1,2,3,4),(5,6,7,8)], dtype=np.int64)
print(array)
unos=np.ones((3,4))
print(unos)
ceros=np.zeros((3,4))
print(ceros)
aleatorios=np.random.random((2,2))
print(aleatorios)
#Crear matriz vacia
vacia=np.empty((3,2))
print(vacia)
#Matriz de un solo valor
full=np.full((2,2),8)
print(full)
#matrices con valores espaciados uniformememnte
espacio1=np.arange(0,30+1,5)
print(espacio1)
#linspace
espacio2=np.linspace(0,2,5)
print(espacio2)
#matriz de identidad
identidad1=np.eye(4,4)
print(identidad1)
identidad2=np.identity(4)
print(identidad2)
#conocer el tipo
a=np.array([(1,2,3)])
print(a.dtype)
#cmabio de forma
a=np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)
a=np.array([(1,2,3,4),(3,4,5,6)])
b=np.array([(1,2,3,4),(3,4,5,0)])
print(a)
print("\n"*1)
print(a[1,2])
print(a[0:,1])
print(a.max())
print(a.min())
print(a.sum())
print(np.std(a))
print(a/b)