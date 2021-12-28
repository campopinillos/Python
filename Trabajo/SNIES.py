import pandas as pd
import numpy as np
import os

os.chdir('/Users/campopinillos/Downloads/')
_2019 = pd.read_excel('2019.xlsx', header=0, skiprows=7)

new_header = _2019.iloc[0] #grab the first row for the header
_2019 = _2019[1:] #take the data less the header row
_2019.columns = new_header #set the header row as the df header

np.sum()

_2019['MATRICULADOS '].sum(level='NIVEL DE FORMACIÓN')



files_name = ["/Users/campopinillos/OneDrive - Instituto Colombiano de Bienestar Familiar/Actividades/02 Modelos/Tablero/anexo-proyecciones-poblacion-Municipal_2018-2026.xlsx",
"/Users/campopinillos/Downloads/anexo-area-sexo-edad-proyecciones-poblacion-Municipal_2005-2017.xlsx"]

df = pd.read_excel(files_name[1], header=0, skiprows=10)

new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header

df = df[df['AÑO'].isin([2016,2017,2018,2019])]
df = df[df['ÁREA GEOGRÁFICA']=='Total']
df['POB17_21'] = df.loc[:, "Total_17":"Total_21"].sum(axis=1).astype(int)

df[df['MPIO']=='Cali']

dpto = pd.pivot_table(df, values=['POB17_21'], index=['DPNOM','AÑO'], aggfunc=np.sum).reset_index()
dpto[dpto['DPNOM']=='Valle del Cauca']

nacional = pd.pivot_table(df, values=['POB17_21'], index=['AÑO'], aggfunc=np.sum).reset_index()
nacional



