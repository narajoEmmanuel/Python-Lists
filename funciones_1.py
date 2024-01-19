#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 3/4/2019 8:00am 
#Fecha de última Modificación: 3/4/2019 10:00pm
#Versión: 3.7.2

materia=[]
notas=[]
candidato=input('nombre del candidato: ')
def ingresarMaterias(i):
    """
    Funcionamiento: Permite el ingreso de las materias y las vuelve mayúsculas.
    Entradas: cantidad de materias (int)
    Salidas: NA
    """
    j=1
    while j<=i:
        materia.append(input("Ingrese el nombre de la materia "+str(j)+":"))
        materia[j-1]=materia[j-1].upper()
        j+=1
    return

def ingresarNotas(i,n):
    """
    Funcionamiento: Permite el ingreso de las notas de las materias.
    Entradas: cantidad de materias (int), contador n (int)
    Salidas: NA
    """
    while n<i:
        notas.append(float(input("Ingrese la nota de "+materia[n]+": ")))
        while notas[n]<0 or notas[n]>100:
            print("La nota debe estar entre 0 y 100")
            notas[n]=(float(input("Ingrese la nota de "+materia[n]+": ")))
        n+=1
    return 

def indicarPromedio(i,n):
    """
    Funcionamiento: calcula el promedio de la lista notas.
    Entradas: cantidad de materias (int), contador n (int)
    Salidas: el promedio de la lista notas.
    """
    promedio=0
    while n<i:
        promedio+=notas[n]
        n+=1
    promedio/=i
    return promedio

def saberResultado(i,n):
    """
    Funcionamiento:  Segun la informacion indica si puede ser asistente o no.
    Entradas: i(int), n(int)
    Salidas: indica si puede ser asistente o no.
    """
    promedio=indicarPromedio(i,n)
    if promedio>=70:
        if "INTRO" in materia:
            if "TALLER" in materia:
                if notas[materia.index("INTRO")]>=80:
                    if notas[materia.index("TALLER")]>=80:
                        return "El candidato: "+candidato+ " tiene un promedio de "+str(promedio)+", en Intro tiene" +str(notas[materia.index("INTRO")])+ " y en Taller tiene"+str(notas[materia.index("TALLER")])+" .Por ende, puede ser el asistente de la profe."
                    return candidato+", su nota de taller debe ser mayor o igual a 80, no puede ser asistente."
                return candidato+", su nota de intro debe ser mayor o igual a 80, no puede ser asistente."
            return candidato+", usted no cursó el curso de taller, no puede ser asistente."
        return candidato+", usted no cursó el curso de intro, no puede ser asistente."
    return candidato+", su promedio no es mayor de 70, no puede ser asistente."


