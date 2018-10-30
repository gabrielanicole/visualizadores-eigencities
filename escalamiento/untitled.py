#Script carga de datos desde csv 

import pandas as pd 
#from trayect.models import Ciudad , Indicador, CiudIndic, Antena, AntIndic, Estadia, Desplazamiento, Persona   
from escalamiento.models import Conurbacion_esc, Comuna_esc

#antenas = Antena.objects.filter(ciudad = 1).values()
csv = "/Users/gabi/Documents/visualizador_opencensus/manzanas_django/esclamiento/datos_com_conb.csv"

df = pd.read_csv(csv)

print(df)

for i in df:
	print(i)

for i in range(len(df)):                                          
    print(df.iloc[i])




	# comuna = Comuna_esc( nombre = , pob_Conurb_2002 = , conurbacion = , pob_Comun_2002 = , 
	# 	vehicle = , motor = , Non_motorized = , private_transport = , public_transport = , 
	# 	CO2_transport = , Green = , Iliteracy = , Municipal_spending = , Unemployment = , Crime = ,
	# 	Arrested = , Companies = , Sales = , workers = , Income = , technicians = , University = , 
	# 	Professionals = , Solid_waste = , Municipal_Power = , Municipal_Water = , Municipal_cleaning = , 
	# 	Deaths =,  Birthrate = , Year_scholarship = , Offence_Property = , Offence_Person = , 
	# 	Burglary = , Robbery = , Injuries = , Indigenous = , Emergency = , Respiratory = , 
	# 	Cardiovascular = , Hospitalizations = , Street = ]

	# comuna.save()