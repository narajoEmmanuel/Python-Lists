#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 3/4/2019 8:00am 
#Fecha de última Modificación: 3/4/2019 10 :00pm
#Versión: 3.7.2

from funciones_1 import*
""""funciones" es el archivo que contiene las funciones principales
a ser llamadas desde este archivo"""

#definicion de funcion
def serAsistente():
    """
    Funcionamiento: Muestra las preguntas para determinar si puede ser asistente. 
    Entradas: cantidad de materias
    Salidas: muestra al usuario si puede ser asistente o no. 
    """
    i=int(input("Ingresa la cantidad de materias: "))
    n=0
    ingresarMaterias(i)
    ingresarNotas(i,n)
    indicarPromedio(i,n)
    print(saberResultado(i,n))
'''
Contadores:
i= indica la cantidad de materias cursadas (int)
n= indica la posicion de la materia en la lista (int)
j= indica los numeros de las materias a ingresar (ej: Ingrese el nombre de la materia 1: ) (int)
'''
#programa
serAsistente()
