""" 
Script para verificar acceso escolar a menores de 5 años base del Censo 2018 
"""

import pandas as pd
import os

mypath = "/Users/campopinillos/OneDrive - Instituto Colombiano de Bienestar Familiar/Actividades/03 Indice"

persona = pd.read_csv(os.path.join(mypath, 'personas_2018.csv'))
mgeonal = pd.read_csv(os.path.join(mypath, 'mgn_2018.csv'))

menores = persona[persona['P_EDADR']==1]

# print(set(list(menores.columns)) & set(list(mgeonal.columns)))
menores = menores.merge(mgeonal, how = 'left',
			  on = ['U_DPTO', 'U_MPIO', 'UA_CLASE',
			  		'COD_ENCUESTAS','U_VIVIENDA'])

menores = menores[['U_DPTO','U_MPIO','UA_CLASE','PA_ASISTENCIA','P_SEXO','COD_DANE_ANM']]å

menores.to_csv('menores_2018.csv', index=False)