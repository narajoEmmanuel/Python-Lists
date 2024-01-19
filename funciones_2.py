#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 11/4/2019  12:00pm 
#Fecha de última Modificación: 13/4/2019  10:00am
#Versión: 3.7.2

amigos=[]
meses=[["Enero",0],["Febrero",0],["Marzo",0],["Abril",0],["Mayo",0],["Junio",0],["Julio",0],["Agosto",0],["Setiembre",0],["Octubre",0],["Noviembre",0],["Diciembre",0]]
aux=["1","2"]
hombres=[]
mujeres=[]

#definicion de funcion
def ingresarAmigos():
    """
    Funcionamiento: Permite el ingreso de los amigos, sus fechas de cumpleaños y su sexo.
    Entradas: N/A
    Salidas: matriz "amigos" llena.
    """
    continuar=1
    while continuar==1:
        datos=[]
        datos.append(input("1. Ingrese el nombre de su amig@: "))#posicion 0
        datos[0]=datos[0].title()
        datos.append(input("2. Ingrese el sexo de su amig@ (hombre(1) o mujer (2)): "))#posicion 1
        SaberSexoAux(datos)
        datos.append(input("3. ¿En qué mes cumple "+datos[0]+"?(ej: enero)"))#posicion 2
        datos[2]=datos[2].capitalize()
        contarMeses(datos)
        datos.append(int(input("4. ¿Qué día cumple "+datos[0]+"?")))#posicion 3
        diaAux(datos)
        amigos.append(datos)
        print('\n----------------------------------\n')
        continuar=int(input("Si desea ingresar otro amigo presione 1, sino presione 2: "))
        print('\n----------------------------------\n')
    return

def diaAux(datos):
    """
    Funcionamiento: valida que el número de día ingresado sea correcto.
    Entradas: lista "datos"
    Salidas: lista "datos"
    """
    while datos[3]<1 or datos[3]>31:
        print("Número inválido.")
        datos[3]=int(input("4. Qué día cumple "+datos[0]+"?"))
    return


def SaberSexoAux(datos):
    """
    Funcionamiento: valida que el número del sexo ingresado sea correcto.
    Entradas: lista "datos"
    Salidas: lista "datos"
    """
    while datos[1] not in aux:
        print("Dato inválido.")
        datos[1]=input("2. Ingrese el sexo de su amig@ (hombre(1) o mujer (2)): ")
    return

def contarMeses(datos):
    """
    Funcionamiento: cuenta cuantos amigos hay en cada mes y valida el ingreso de los meses
    Entradas: lista datos
    Salidas: datos[2]
    """
    if datos[2]==meses[0][0]:
        meses[0][1]+=1
    elif datos[2]==meses[1][0]:
        meses[1][1]+=1
    elif datos[2]==meses[2][0]:
        meses[2][1]+=1
    elif datos[2]==meses[3][0]:
        meses[3][1]+=1
    elif datos[2]==meses[4][0]:
        meses[4][1]+=1
    elif datos[2]==meses[5][0]:
        meses[5][1]+=1
    elif datos[2]==meses[6][0]:
        meses[6][1]+=1
    elif datos[2]==meses[7][0]:
        meses[7][1]+=1
    elif datos[2]==meses[8][0]:
        meses[8][1]+=1
    elif datos[2]==meses[9][0]:
        meses[9][1]+=1
    elif datos[2]==meses[10][0]:
        meses[10][1]+=1
    elif datos[2]==meses[11][0]:
        meses[11][1]+=1
    else:
        x=False
        while x==False:
            print("Nombre del mes inválido.")
            datos[2]=input("3. ¿En qué mes cumple "+datos[0]+"?")
            datos[2]=datos[2].capitalize()
            n=0
            while n<12:
                if datos[2]==meses[n][0]:
                    x=True
                n+=1
        contarMeses(datos)
    return
   

def imprimirResultado():
    """
    Funcionamiento: imprime la lista de amigos
    Entradas: N/A
    Salidas: lista de amigos
    """
    n=0
    while n<12:
        a=0
        if meses[n][1]>0:
            print("~ En "+meses[n][0]+" cumplen "+str(meses[n][1])+" amigos, ellos son:")
            while a<len(amigos):
                if amigos[a][2]==meses[n][0]:
                    print(amigos[a][0]+" el día "+str(amigos[a][3]))
                a+=1
        else:
            print("~ En "+meses[n][0]+" cumplen "+str(meses[n][1])+" amigos.")
            while a<len(amigos):
                if amigos[a][2]==meses[n][0]:
                    print(amigos[a][0]+" el día "+str(amigos[a][3]))
                a+=1
        n+=1
    return

def saberSexo(amigos):
    """
    Funcionamiento: Calcular la cantidad de amigos y amigas..
    Entradas: matriz "amigos"
    Salidas: Cantidad de amigos y amigas
    """
    hombres=0
    mujeres=0
    j=0
    while j<len(amigos):
        if amigos[j][1]==1:
            hombres+=1
        else:
            mujeres+=1
        j+=1
        
    print('\n----------------------------------\n')
    print('Usted tiene ',hombres,' amigo(s) y ',mujeres,' amiga(s).')
    if hombres>mujeres:
        print('Por lo tanto, se deduce que usted tiene mas amigos que amigas.')
    elif hombres<mujeres:
        print('Por lo tanto, se deduce que usted tiene mas amigas que amigos.')
    elif hombres==mujeres:
        print('Se deduce que usted tiene la misma cantidad de amigos y amigas.')
    
    return ''

    
