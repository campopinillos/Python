""" 
Script para modificar base del Censo 2018 
"""

import pandas as pd
import os

mypath = "/Users/campopinillos/OneDrive - Instituto Colombiano de Bienestar Familiar/Actividades/03 Indice"

persona = pd.read_csv(os.path.join(mypath, 'personas_2018.csv'))
persona.head()

pop_tot = persona.groupby(['U_DPTO','U_MPIO'])['U_MPIO'].count()

pop_edad = pd.crosstab(index=[persona['U_DPTO'],persona['U_MPIO']], columns=persona['P_EDADR'],
					   rownames=[persona['U_DPTO'], persona['U_MPIO']])

asisten = persona[persona['PA_ASISTENCIA']==1.0].groupby(['U_DPTO','U_MPIO','PA_ASISTENCIA'])['PA_ASISTENCIA'].count()

alfabet = pd.crosstab(index=[persona['U_DPTO'],persona['U_MPIO']], columns=persona['P_ALFABETA'],
					  rownames=[persona['U_DPTO'],persona['U_MPIO']], colnames=persona['P_ALFABETA'])

alfabet = pd.pivot_table(persona, index=['U_DPTO','U_MPIO'], columns='P_ALFABETA', aggfunc='count', fill_value=0)

nv_educ = pd.crosstab(index=[persona['U_DPTO'],persona['U_MPIO']], columns=persona['P_NIVEL_ANOSR'],
					  rownames=[persona['U_DPTO'],persona['U_MPIO']], colnames=persona['P_NIVEL_ANOSR'])

actual_educ = pd.crosstab(index=[persona['U_DPTO'],persona['U_MPIO']], columns=persona['P_TRABAJO'],
					  rownames=[persona['U_DPTO'],persona['U_MPIO']], colnames=persona['P_TRABAJO'])


censo = pd.read_csv(os.path.join(mypath, 'censo_2018.csv'))
censo.head()


personas = persona[['TIPO_REG', 'U_DPTO', 'U_MPIO', 
'UA_CLASE', 'COD_ENCUESTAS', 
'U_VIVIENDA', 'P_NROHOG', 
'P_NRO_PER', 'P_SEXO', 
'P_EDADR','P_PARENTESCOR',
'PA1_GRP_ETNIC','P_ALFABETA',
'PA_ASISTENCIA','P_NIVEL_ANOSR','P_TRABAJO']]







