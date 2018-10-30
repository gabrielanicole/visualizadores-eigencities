#Script carga de datos desde csv 

import pandas as pd 
import math
#from trayect.models import Ciudad , Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento, Persona   
from escalamiento.models import Conurbacion_esc, Comuna_esc

#antenas = Antena.objects.filter(ciudad = 1).values()
#csv = "/Users/gabi/Documents/visualizador_opencensus/manzanas_django/esclamiento/centros_prueba2_sinBlancos_conurbaciones.csv"
csv= "escalamiento/centros_prueba2_sinBlancos_conurbaciones.csv"
df_centros = pd.read_csv(csv)

#print(df)

#for i in df:
#    print(i)

for i in range(len(df_centros)):
    nombre = df_centros.iloc[i].NOMBRE if df_centros.iloc[i].NOMBRE else None  
    pob = df_centros.iloc[i]["conb_Pob_Conurb_2002"] if df_centros.iloc[i]["conb_Pob_Conurb_2002"] else None  
    conb_Crime  = df_centros.iloc[i]["conb_Crime reports"]  if df_centros.iloc[i]["conb_Crime reports"] else None 
    conb_Income= df_centros.iloc[i]["conb_Income(workers)"] if df_centros.iloc[i]["conb_Income(workers)"] else None 
    conb_Municipal = df_centros.iloc[i]["conb_Municipal spending(M$/hab)"]  if df_centros.iloc[i]["conb_Municipal spending(M$/hab)"] else None  
    conb_workers = df_centros.iloc[i]["conb_workers"] if df_centros.iloc[i]["conb_workers"] else None 
    conb_vehicle = df_centros.iloc[i]["conb_vehicle"]  if df_centros.iloc[i]["conb_vehicle"] else None  
    conb_motor  = df_centros.iloc[i]["conb_motor vehicle"] if df_centros.iloc[i]["conb_motor vehicle"]else None 
    conb_Nonmotorized = df_centros.iloc[i]["conb_Non-motorized vehicle"] if df_centros.iloc[i]["conb_Non-motorized vehicle"]else None  
    conb_private = df_centros.iloc[i]["conb_private transport"] if df_centros.iloc[i]["conb_private transport"] else None  
    conb_public = df_centros.iloc[i]["conb_public transport"] if df_centros.iloc[i]["conb_public transport"] else None 
    conb_CO2 = df_centros.iloc[i]["conb_CO2(movil transport sources)"]  if df_centros.iloc[i]["conb_CO2(movil transport sources)"] else None 
    conb_Green = df_centros.iloc[i]["conb_Green spaces"] if  df_centros.iloc[i]["conb_Green spaces"] else None 
    conb_Iliteracy = df_centros.iloc[i]["conb_Iliteracy"]  if df_centros.iloc[i]["conb_Iliteracy"] else None 
    conb_Unemployment = df_centros.iloc[i]["conb_Unemployment"] if df_centros.iloc[i]["conb_Unemployment"] else None 
    conb_Arrested  = df_centros.iloc[i]["conb_Arrested person"]  if df_centros.iloc[i]["conb_Arrested person"] else None  
    conb_Companies = df_centros.iloc[i]["conb_Companies"]  if df_centros.iloc[i]["conb_Companies"] else None 
    conb_Sales = df_centros.iloc[i]["conb_Sales"] if df_centros.iloc[i]["conb_Sales"] else None 
    conb_technicians = df_centros.iloc[i]["conb_Professional technicians"] if df_centros.iloc[i]["conb_Professional technicians"] else None 
    conb_University = df_centros.iloc[i]["conb_University Professional"] if df_centros.iloc[i]["conb_University Professional"] else None 
    conb_Professionals = df_centros.iloc[i]["conb_Professionals"] if df_centros.iloc[i]["conb_Professionals"] else None 
    conb_Solid  = df_centros.iloc[i]["conb_Solid Waste"] if df_centros.iloc[i]["conb_Solid Waste"] else None 
    conb_MunicipalspendingPower  = df_centros.iloc[i]["conb_Municipal spending for Power Consumption"] if df_centros.iloc[i]["conb_Municipal spending for Power Consumption"] else None 
    conb_MunicipalspendingWater  = df_centros.iloc[i]["conb_Municipal spending for Water Consumption"] if df_centros.iloc[i]["conb_Municipal spending for Water Consumption"] else None 
    conb_MunicipalSpendingcleaning = df_centros.iloc[i]["conb_Municipal Spending cleaning services garbage collection landfill"] if df_centros.iloc[i]["conb_Municipal Spending cleaning services garbage collection landfill"] else None 
    conb_Deaths = df_centros.iloc[i]["conb_Deaths"]  if df_centros.iloc[i]["conb_Deaths"] else None 
    conb_Birthrate = df_centros.iloc[i]["conb_Birthrate"]  if df_centros.iloc[i]["conb_Birthrate"] else None  
    conb_scholarship = df_centros.iloc[i]["conb_Year of scholarship"] if df_centros.iloc[i]["conb_Year of scholarship"] else None 
    conb_Property = df_centros.iloc[i]["conb_Offence Against Property"] if df_centros.iloc[i]["conb_Offence Against Property"] else None 
    conb_Person = df_centros.iloc[i]["conb_Offence Against the Person"] if df_centros.iloc[i]["conb_Offence Against the Person"] else None 
    conb_Burglary = df_centros.iloc[i]["conb_Burglary"] if df_centros.iloc[i]["conb_Burglary"] else None 
    conb_Robbery = df_centros.iloc[i]["conb_Robbery"] if df_centros.iloc[i]["conb_Robbery"] else None 
    conb_Injuries = df_centros.iloc[i]["conb_Injuries"] if  df_centros.iloc[i]["conb_Injuries"] else None  
    conb_Indigenous = df_centros.iloc[i]["conb_Indigenous"] if df_centros.iloc[i]["conb_Indigenous"] else None 
    conb_Emergency = df_centros.iloc[i]["conb_Emergency attendence"] if df_centros.iloc[i]["conb_Emergency attendence"] else None 
    conb_Respiratory = df_centros.iloc[i]["conb_Respiratory Diseases"] if df_centros.iloc[i]["conb_Respiratory Diseases"] else None 
    conb_Cardiovascular = df_centros.iloc[i]["conb_Cardiovascular Diseases"] if df_centros.iloc[i]["conb_Cardiovascular Diseases"] else None 
    conb_Hospitalizations = df_centros.iloc[i]["conb_Hospitalizations"] if df_centros.iloc[i]["conb_Hospitalizations"] else None 
    conb_Street = df_centros.iloc[i]["conb_Street length"] if df_centros.iloc[i]["conb_Street length"] else None 
    comuna = Comuna_esc.objects.filter(nombre = nombre)[0]
    # try:
        # comuna = Comuna_esc.objects.filter(nombre = nombre)[0]
        #comuna.log_pob_Comun_2002 = math.log(pob) 
        #comuna.log_vehicle = math.log(conb_vehicle) 
        #comuna.log_motor = math.log(conb_motor) 
        #comuna.log_Non_motorized = math.log(conb_Nonmotorized)
        #comuna.log_private_transport =  math.log(conb_private) 
        #comuna.log_public_transport = math.log(conb_public) 
        #comuna.log_CO2_transport =  math.log(conb_CO) --> NO SE CARGO 
        #comuna.log_Green = math.log(conb_Green)


    try:  
        comuna.log_Iliteracy = math.log(conb_Iliteracy)
    except:
        None 
    try:
        comuna.log_Municipal_spending = math.log(conb_Municipal)
    except:
        None
    try:
        comuna.log_Unemployment = math.log(conb_Unemployment)
    except:
        None
    try:
        comuna.log_Crime =  math.log(conb_Crime)            
    except:
        None
    try:
        comuna.log_Arrested = math.log(conb_Arrested)
    except:
        None
    try:
        comuna.log_Companies = math.log(conb_Companies)
    except:
        None
    try:
        comuna.log_Sales = math.log(conb_Sales)
    except:
        None
    try:
        comuna.log_workers = math.log(conb_workers)   
    except:
        None
    try:
        comuna.log_Income = math.log(conb_Income)        
    except:
        None 
    try:
        comuna.log_technicians = math.log(conb_technicians) 
    except:
        None
    try:
        comuna.log_University = math.log(conb_University)
    except:
        None
    try:
        comuna.log_Professionals = math.log(conb_Professionals)
    except:
        None
    try:
        comuna.log_Solid_waste = math.log(conb_Solid)
    except:
        None
    try:
        comuna.log_Municipal_Power = math.log(conb_Municipalspending)
    except:
        None
    try:
        comuna.log_Municipal_Water = math.log(conb_Municipalspending)
    except:
        None
    try:
        comuna.log_Municipal_cleaning = math.log(conb_Municipal)
    except:
        None
    try:
        comuna.log_Deaths = math.log(conb_Deaths)
    except:
        None
    try:
        comuna.log_Birthrate = math.log(conb_Birthrate)
    except:
        None
    try:
        comuna.log_Year_scholarship = math.log(conb_scholarship) 
    except:
        None
    try:
        comuna.log_Offence_Property = math.log(conb_Property)
    except:
        None
    try:
        comuna.log_Offence_Person = math.log(conb_Person)
    except:
        None
    try:
        comuna.log_Burglary = math.log(conb_Burglary)
    except:
        None
    try:
        comuna.log_Robbery = math.log(conb_Robbery)
    except:
        None
    try:
        comuna.log_Injuries = math.log(conb_Injuries)
    except:
        None
    try:
        comuna.log_Indigenous = math.log(conb_Indigenous)
    except:
        None
    try:
        comuna.log_Emergency = math.log(conb_Emergency)
    except:
        None
    try:
        comuna.log_Respiratory = math.log(conb_Respiratory)
    except:
        None
    try:
        comuna.log_Cardiovascular = math.log(conb_Cardiovascular)
    except:
        None
    try:
        comuna.log_Hospitalizations = math.log(conb_Hospitalizations)
    except:
        None
    try:
        comuna.log_Street = math.log(conb_Street)
    except:
        None
    try:
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( ")