import pandas as pd 
from trayect.models import Ciudad, Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento  

antenas = Antena.objects.filter(ciudad = 1).values()
csv = "/Users/gabi/Documents/visualizador_opencensus/observatorio_BigData/workflowScripts/ResultadosPM150316.csv"

diaEstudio = "150316"
ciudadEstudio = "gran puerto montt"
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




