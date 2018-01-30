import pandas as pd 
from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento, Persona   

antenas = Antena.objects.filter(ciudad = 1).values()
csv = "/Users/gabi/Documents/visualizador_opencensus/observatorio_BigData/workflowScripts/antofagasta150321.csv"

diaEstudio = "150321"
ciudadEstudio = "antofagasta"
df = pd.read_csv(csv)
#Este es solo de gran puerto montt

#suma	mediana	moda	average	desvstd	minim	maxim	varianza 

for i in range(len(df)):                                          
    print(df.iloc[i])
    ind = df.iloc[i].caract
    rT = df.iloc[i].TotalResidentes
    mT = df.iloc[i].TotalEnMov
    hora = df.iloc[i].hora
    NperHora = df.iloc[i].NperHora
    Nmov = df.iloc[i].Nmov
    suma = df.iloc[i].suma
    mediana = df.iloc[i].mediana
    moda = df.iloc[i].moda
    average = df.iloc[i].average
    desvstd = df.iloc[i].desvstd
    minim = df.iloc[i].minim
    maxim = df.iloc[i].maxim
    varianza = df.iloc[i].varianza
    p25 = df.iloc[i].p25
    p50 = df.iloc[i].p50
    p75 = df.iloc[i].p75

    ciudad = Ciudad.objects.get(nombre = ciudadEstudio)
    ind = Indicador.objects.get(nombre = ind)
    ciudadRevisar = CiudIndic.objects.filter(indicador= ind, ciudad=ciudad) 
    if not ciudadRevisar:
    	ciudadGuardar = CiudIndic(indicador = ind, ciudad = ciudad, residentesTotal = rT, movimientoTotal = mT)
    	ciudadGuardar.save()
    horaINDRevisar = Desplazamiento.objects.filter(dia=diaEstudio, ciudad=ciudad, indicador=ind, hora=hora)
    if not horaINDRevisar:
    	horaIND = Desplazamiento(dia=diaEstudio,ciudad=ciudad,indicador=ind,hora=hora,personasTotal = NperHora,movimientoTotal = Nmov,
suma = suma,mediana = mediana,moda = moda,promedio = average,desviacionSt = desvstd,minimo = minim,maximo = maxim,varianza = varianza,p25 = p25,p50 = p50,p75 = p75 )
    	horaIND.save()



csv = "/mysql_exp/ANTENAS_CHILE.csv"

df = pd.read_csv(csv)
#Este es solo de gran puerto montt

#suma   mediana moda    average desvstd minim   maxim   varianza 

for i in range(len(df)):                                          
    print(df.iloc[i])
    nombre = df.iloc[i].id
    ciudad_att = df.iloc[i].zona_u
    lat = df.iloc[i].lat
    lon = df.iloc[i].lon
   
    ciudad = Ciudad.objects.filter(nombre = ciudad_att)
    if ciudad:
        ciudad = Ciudad.objects.get(nombre = ciudad_att)
        antenaRevisar = Antena.objects.filter(nombre= nombre, ciudad = ciudad)
        if not antenaRevisar:
            antenaGuardar = Antena(nombre = nombre, ciudad = ciudad, lat = lat, lon = lon)
            antenaGuardar.save()

csv = "/mysql_exp/ANTCAR_CHILE.csv"

df = pd.read_csv(csv)


for i in range(len(df)):                                          
    print(df.iloc[i])
    ind = df.iloc[i][0]
    ant = df.iloc[i][1]
    cantidad = df.iloc[i][2]
   
    indicador = Indicador.objects.filter(nombre = ind)
    antena = Antena.objects.filter(nombre = ant)
    if indicador and antena:
        antcarRevisar = AntIndic.objects.filter(antena = antena[0], indicador = indicador[0]) 
        if not antcarRevisar:
            antcarGuardar = AntIndic(antena = antena[0], indicador = indicador[0], cantidad = cantidad)
            antcarGuardar.save()

#añadir total Residencia. 
csv = "/mysql_exp/consulta.csv"

df = pd.read_csv(csv)


for i in range(len(df)):                                          
    print(df.iloc[i])
    cantidad = df.iloc[i][0]
    ant = df.iloc[i][1]
    nom_ciudad = df.iloc[i][2]
   
    #indicador = Indicador.objects.filter(nombre = ind)
    antena = Antena.objects.filter(nombre = ant)
    if antena:
        antena = antena[0]
        if not (antena.residentesTotal) :
            antena.residentesTotal = cantidad
            antena.save()


##Cargar Residencia 
csv = "/mysql_exp/PERSONAS_SINSTGO.csv"

df = pd.read_csv(csv)

from random import randint
print(randint(0, 9))

## Cargar solo 20 personas por cada antena. 
torres =  pd.unique(df.iloc[:,0])
for i in torres:
    personas = df[df.iloc[:,0]== i]
    a = []
    while len(a) < 20 and len(a) < len(personas): 
        nuevo_indice = randint(0,len(personas) -1 )
        if not (nuevo_indice in a):
            a.append(nuevo_indice)
            nom_antena = personas.iloc[nuevo_indice,0]
            numa_persona = personas.iloc[nuevo_indice,2]
            antenaResidencia =  Antena.objects.filter(nombre = nom_antena) 
            if antenaResidencia :
                antena = antenaResidencia[0]
                persona = Persona(numa = numa_persona, residencia = antena)
                persona.save()
            else:
                print(antena, "no esta :(")

##Cargar Estadías 

#1.- Descargar los numas que se agregaron

##Coneccion con la base de datos en local

import mysql
import mysql.connector

cnx = mysql.connector.connect(user='gabi', password='mysql_gabi',
                              host='127.0.0.1', database="pings")

cnx_uso = mysql.connector.connect(user='gabi', password='mysql_gabi',
                              host='127.0.0.1', database="pings_usos")

cursor_lugar = cnx_uso.cursor(buffered=True)

numas = Persona.objects.all().values('numa')
cursorNuma =cnx.cursor(buffered = True )

for persona in numas:
    print()
    numa = persona["numa"]
    #Buscar Trayectoria
    queryNuma = (
        "SELECT dia, hora, antena from ping where numa = %s order by dia, hora ")
    cursorNuma.execute(queryNuma, (numa,))
    pings = cursorNuma.fetchall()
    ping0 = 0 
    tray = []
    guardar = False 
    for ping in pings:
        dia = ping[0]
        hora = ping[1]
        antena = ping[2]
        if ( ping0 != 0  and dia != ping0[0]): 
            #cambia el día, caso: terminamos y comenzamos en la misma antena. 
            #en este caso no revisamos la antena anterior y partimos de cero. 
            #solo guardo el primer ping. y reviso donde termina la antena para continuar con el siguiente ping. 
            
            if guardar : 
                guardarEstadia(ping0[2], numa, ping0[0], ping0[1])
                tray.append(ping0)
            ping0 = ping
            guardarEstadia(antena, numa, dia, hora)
            tray.append(ping)
            guardar = False


        elif (ping0 != 0 and antena != ping0[2]): #debo guardar los ping anteriores y este como el primero
            
            if guardar : 
                tray.append(ping0)
                guardarEstadia(ping0[2], numa, ping0[0], ping0[1])
            ping0 = ping
            tray.append(ping)
            guardarEstadia(antena, numa, dia, hora)
            guardar = False


        #buscar antena en sqlite. 
        elif (ping0 == 0): #debo guardar este ping, para revisar si se repite en el siguiente y guardar el primer ping.
           
            ping0 = ping
            tray.append(ping)
            guardarEstadia(antena, numa, dia, hora)

        else : #es el mismo día y misma antena, solo hay que guardar la hora. 
           
            ping0 = ping
            guardar = True

def guardarEstadia(antena, numa, dia, hora):
    antenaRevisar =  Antena.objects.filter(nombre = antena) 
    numaRevisar =  Persona.objects.filter(numa = numa) 
    if antenaRevisar and numaRevisar:
        antenaPing = antenaRevisar[0]
        numaPing = numaRevisar[0]
        pingRevisar = Estadia.objects.filter(numa = numaPing, horaP = hora, dia= dia, antena = antenaPing)
        if not pingRevisar:
            estadia = Estadia(numa = numaPing , horaP = hora, dia = dia , antena = antenaPing)
            try:
                estadia.save()
            except ValueError:
                print(ValueError)
                print(" no se guardo", antena, numa, dia, hora)
        else:
            print(" ya existe ", antena, numa, dia, hora)

    else:
        print("antena o numa no esta: ", antena, numa)








     

