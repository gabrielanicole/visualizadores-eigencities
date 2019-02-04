#Script carga de datos 
import pandas as pd 
import numpy as np
import math
from escalamiento.models import Comuna_esc, Variable
# var = Variable.objects.values('nombre')
var = Variable.objects.all()
for variable in var:
    print(variable.nombre)
    logVar = 'log_' + variable.nombre
    data = list(Comuna_esc.objects.values_list("nombre", "log_pob_Comun_2002" , logVar, "pob_Comun_2002", variable.nombre, "lat", "lon", 'id' ))
    data_x = [float(x[1]) for x in data if  x[1] and x[2] and len(str(x[2])) > 3 ]
    data_y = [float(x[2]) for x in data if  x[1] and x[2] and len(str(x[2])) > 3 ]
    n = len(data)
    reg = np.polyfit(data_x, data_y , 1)
    print(reg)
    variable.n_calculob10 = n 
    variable.a0b10 = reg[1] 
    variable.mb10 = reg[0] 
    variable.save()




