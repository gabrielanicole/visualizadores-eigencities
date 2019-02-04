#Script carga de datos desde csv 
import pandas as pd 
import math
from escalamiento.models import Conurbacion_esc, Comuna_esc
csv= "escalamiento/centros_prueba2_sinBlancos_conurbaciones.csv"
df_centros = pd.read_csv(csv)
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
    print(comuna)
    try:  
        comuna.log_private_transport = math.log10(conb_private)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_private")    
    try:  
        comuna.log_public_transport = math.log10(conb_public)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_public")
    try:  
        comuna.log_CO2_transport = math.log10(conb_CO2)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_CO2")
    try:  
        comuna.log_vehicle = math.log10(conb_vehicle)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_vehicle")
    try:  
        comuna.log_motor = math.log10(conb_motor)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_motor")
    try:  
        comuna.log_Nonmotorized = math.log10(conb_Nonmotorized)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Nonmotorized")
    try:  
        comuna.log_Green = math.log10(conb_Green)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Green")
    try:  
        comuna.log_pob_Comun_2002 = math.log10(pob)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( log_pob")
    try:  
        comuna.log_Iliteracy = math.log10(conb_Iliteracy)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( log_Iliteracy")
    try:
        comuna.log_Municipal_spending = math.log10(conb_Municipal)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( log_Municipal_spending")
    try:
        comuna.log_Unemployment = math.log10(conb_Unemployment)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( log_Unemployment")
    try:
        comuna.log_Crime =  math.log10(conb_Crime)            
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Crime")
    try:
        comuna.log_Arrested = math.log10(conb_Arrested)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Arrested")
    try:
        comuna.log_Companies = math.log10(conb_Companies)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Companies")
    try:
        comuna.log_Sales = math.log10(conb_Sales)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Sales")
    try:
        comuna.log_workers = math.log10(conb_workers)   
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_workers")
    try:
        comuna.log_Income = math.log10(conb_Income)        
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Income") 
    try:
        comuna.log_technicians = math.log10(conb_technicians) 
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_technicians")
    try:
        comuna.log_University = math.log10(conb_University)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_University")
    try:
        comuna.log_Professionals = math.log10(conb_Professionals)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Professionals")
    try:
        comuna.log_Solid_waste = math.log10(conb_Solid)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Solid")
    try:
        comuna.log_Municipal_Power = math.log10(conb_MunicipalspendingPower)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_MunicipalspendingPower")
    try:
        comuna.log_Municipal_Water = math.log10(conb_MunicipalspendingWater)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_MunicipalspendingWater")
    try:
        comuna.log_Municipal_cleaning = math.log10(conb_MunicipalSpendingcleaning)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_MunicipalSpendingcleaning")
    try:
        comuna.log_Deaths = math.log10(conb_Deaths)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Deaths")
    try:
        comuna.log_Birthrate = math.log10(conb_Birthrate)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Birthrate")
    try:
        comuna.log_Year_scholarship = math.log10(conb_scholarship) 
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_scholarship")
    try:
        comuna.log_Offence_Property = math.log10(conb_Property)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Property")
    try:
        comuna.log_Offence_Person = math.log10(conb_Person)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Person")
    try:
        comuna.log_Burglary = math.log10(conb_Burglary)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Burglary")
    try:
        comuna.log_Robbery = math.log10(conb_Robbery)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Robbery")
    try:
        comuna.log_Injuries = math.log10(conb_Injuries)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Injuries")
    try:
        comuna.log_Indigenous = math.log10(conb_Indigenous)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Indigenous")
    try:
        comuna.log_Emergency = math.log10(conb_Emergency)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Emergency")
    try:
        comuna.log_Respiratory = math.log10(conb_Respiratory)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Respiratory")
    try:
        comuna.log_Cardiovascular = math.log10(conb_Cardiovascular)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Cardiovascular")
    try:
        comuna.log_Hospitalizations = math.log10(conb_Hospitalizations)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Hospitalizations")
    try:
        comuna.log_Street = math.log10(conb_Street)
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Street")
    try:  
        comuna.Iliteracy = conb_Iliteracy
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( Iliteracy")
    try:
        comuna.Municipal_spending = conb_Municipal
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( Municipal_spending")
    try:
        comuna.Unemployment = conb_Unemployment
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( Unemployment")
    try:
        comuna.Crime =  conb_Crime            
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Crime")
    try:
        comuna.Arrested = conb_Arrested
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Arrested")
    try:
        comuna.Companies = conb_Companies
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Companies")
    try:
        comuna.Sales = conb_Sales
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Sales")
    try:
        comuna.workers = conb_workers   
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_workers")
    try:
        comuna.Income = conb_Income        
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Income") 
    try:
        comuna.technicians = conb_technicians 
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_technicians")
    try:
        comuna.University = conb_University
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_University")
    try:
        comuna.Professionals = conb_Professionals
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Professionals")
    try:
        comuna.Solid_waste = conb_Solid
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Solid")
    try:
        comuna.Municipal_Power = conb_MunicipalspendingPower
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_MunicipalspendingPower")
    try:
        comuna.Municipal_Water = conb_MunicipalspendingWater
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_MunicipalspendingWater")
    try:
        comuna.Municipal_cleaning = conb_MunicipalSpendingcleaning
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_MunicipalSpendingcleaning")
    try:
        comuna.Deaths = conb_Deaths
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Deaths")
    try:
        comuna.Birthrate = conb_Birthrate
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Birthrate")
    try:
        comuna.Year_scholarship = conb_scholarship 
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_scholarship")
    try:
        comuna.Offence_Property = conb_Property
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Property")
    try:
        comuna.Offence_Person = conb_Person
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Person")
    try:
        comuna.Burglary = conb_Burglary
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Burglary")
    try:
        comuna.Robbery = conb_Robbery
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Robbery")
    try:
        comuna.Injuries = conb_Injuries
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Injuries")
    try:
        comuna.Indigenous = conb_Indigenous
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Indigenous")
    try:
        comuna.Emergency = conb_Emergency
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Emergency")
    try:
        comuna.Respiratory = conb_Respiratory
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Respiratory")
    try:
        comuna.Cardiovascular = conb_Cardiovascular
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Cardiovascular")
    try:
        comuna.Hospitalizations = conb_Hospitalizations
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Hospitalizations")
    try:
        comuna.Street = conb_Street
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( conb_Street")
    try:
        comuna.save()
    except:
        print(nombre,i, "no se cargo :( ")