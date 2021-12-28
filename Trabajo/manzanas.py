import numpy as np
import pandas as pd
import xlsxwriter
# import subprocess

persona = pd.read_csv("censo_2018.csv")
vivienda = pd.read_csv("vivienda_2018.csv")
hogar = pd.read_csv("hogares_2018.csv")
mgeonal = pd.read_csv("mgn_2018.csv")

# print(set(list(persona.columns)) & set(list(mgeonal.columns)))
persona = persona.merge(mgeonal, how = 'left',
						on = ['COD_ENCUESTAS',
							  'U_VIVIENDA', 'U_DPTO',
							  'U_MPIO', 'UA_CLASE'])

# print(set(list(vivienda.columns)) & set(list(mgeonal.columns)))
vivienda = vivienda.merge(mgeonal, how = 'left', 
						  on = ['COD_ENCUESTAS',
								'U_VIVIENDA', 'U_DPTO',
								'U_MPIO', 'UA_CLASE'])


# print(set(list(hogar.columns)) & set(list(mgeonal.columns)))
hogar = hogar.merge(mgeonal, how = 'left', 
					on = ['COD_ENCUESTAS',
						  'U_VIVIENDA', 'U_DPTO',
						  'U_MPIO', 'UA_CLASE'])

# persona.info()
# vivienda.info()
# hogar.info()
# mgeonal.info()

# Edad en Grupos Quinquenales
persona["EDAD"] = np.where(persona["P_EDADR"] == 0 , "Edad_De_00A04",
np.where(persona["P_EDADR"] == 1 ,"Edad_De_05A09",
np.where(persona["P_EDADR"] == 2 ,"Edad_De_10A14",
np.where(persona["P_EDADR"] == 3 ,"Edad_De_10A14",
np.where(persona["P_EDADR"] == 4 , "Edad_De_15A19",
np.where(persona["P_EDADR"] == 5 , "Edad_De_20A24",
np.where(persona["P_EDADR"] == 6 , "Edad_De_25A29",
np.where(persona["P_EDADR"] == 7 , "Edad_De_30A34",
np.where(persona["P_EDADR"] == 8 , "Edad_De_35A39",
np.where(persona["P_EDADR"] == 9 , "Edad_De_40A44",
np.where(persona["P_EDADR"] == 10 , "Edad_De_45A49",
np.where(persona["P_EDADR"] == 11 , "Edad_De_50A54",
np.where(persona["P_EDADR"] == 12 , "Edad_De_55A59",
np.where(persona["P_EDADR"] == 13 , "Edad_De_60A64",
np.where(persona["P_EDADR"] == 14 , "Edad_De_65A69",
np.where(persona["P_EDADR"] == 15 , "Edad_De_70A74",
np.where(persona["P_EDADR"] == 16 , "Edad_De_75A79",
np.where(persona["P_EDADR"] == 17 , "Edad_De_80A84",
np.where(persona["P_EDADR"] == 18 , "Edad_De_85A89",
np.where(persona["P_EDADR"] == 19 , "Edad_De_90A94",
np.where(persona["P_EDADR"] == 20 , "Edad_De_95A99",
np.where(persona["P_EDADR"] == 21 , "Edad_De_100_más", ""
))))))))))))))))))))))
# persona["EDAD"].value_counts()
# df = persona.groupby('P_EDADR')['COD_ENCUESTAS'].nunique()
# print(df)

# Alfabetismo
persona['ALFABETA'] = np.where(persona["P_ALFABETA"] == 1 , "Si_Alfabeta",
np.where(persona["P_ALFABETA"] == 2 ,"No_Alfabeta",
np.where(persona["P_ALFABETA"] == 9 ,"No_Informa_Alfabeta", "No_Aplica_Alfabeta")))
# persona["ALFABETA"].value_counts()

# Asistencia Escolar
persona['ESCOLAR'] = np.where(persona["PA_ASISTENCIA"] == 1 , "Si_Asiste",
np.where(persona["PA_ASISTENCIA"] == 2 ,"No_Asiste",
np.where(persona["PA_ASISTENCIA"] == 9 ,"No_Informa_Asiste", "No_Aplica_Asiste")))
# persona["ESCOLAR"].value_counts()

# Genero
persona['SEXO'] = np.where(persona["P_SEXO"] == 1 , "Hombre",
np.where(persona["P_SEXO"] == 2 ,"Mujer",""))
# persona["SEXO"].value_counts()

# Etnias
persona['ETNIA'] = np.where(persona["PA1_GRP_ETNIC"] == 1 , "Indigena",
np.where(persona["PA1_GRP_ETNIC"] == 2 ,"Gitano",
np.where(persona["PA1_GRP_ETNIC"] == 3 ,"Raizal",
np.where(persona["PA1_GRP_ETNIC"] == 4 ,"Palenquero",
np.where(persona["PA1_GRP_ETNIC"] == 5 ,"Negro_Afro",
np.where(persona["PA1_GRP_ETNIC"] == 6 ,"Ninguno",
np.where(persona["PA1_GRP_ETNIC"] == 9 ,"No_Informa", "")))))))
# persona["ETNIA"].value_counts()

# Generando tablas por Manzana
# pop_tot = (persona.groupby(['COD_DANE_ANM','P_EDADR'])['P_EDADR'].agg('count').reset_index(name='Count'))
pop_tot = (persona.groupby(['COD_DANE_ANM'])['COD_DANE_ANM'].agg('count').reset_index(name='Count'))
pop_tot.rename(columns={"Count": "Población"}, inplace=True)

pop_eda = pd.crosstab(index=persona['COD_DANE_ANM'], columns=persona['EDAD'])
pop_etn = pd.crosstab(index=persona['COD_DANE_ANM'], columns=persona['ETNIA'])
pop_alf = pd.crosstab(index=persona['COD_DANE_ANM'], columns=persona['ALFABETA'])
pop_gen = pd.crosstab(index=persona['COD_DANE_ANM'], columns=persona['SEXO'])
pop_asi = pd.crosstab(index=persona['COD_DANE_ANM'], columns=[persona['EDAD'], persona['ESCOLAR']])

# Generando tabla de poblacion por Manzana
pop_man = pop_tot.merge(pop_eda, how = 'outer', on = ['COD_DANE_ANM'])
pop_man = pop_man.merge(pop_etn, how = 'outer', on = ['COD_DANE_ANM'])
pop_man = pop_man.merge(pop_alf, how = 'outer', on = ['COD_DANE_ANM'])
pop_man = pop_man.merge(pop_gen, how = 'outer', on = ['COD_DANE_ANM'])
pop_man = pop_man.merge(pop_asi, how = 'outer', on = ['COD_DANE_ANM'])

# Generando tabla de hogares por Manzana
hog_tot = (hogar.groupby(['COD_DANE_ANM'])['COD_DANE_ANM'].agg('count').reset_index(name='Count'))
hog_tot.rename(columns={"Count": "Hogares"}, inplace=True)

# Generando tabla de hogares por Manzana
viv_tot = (vivienda.groupby(['COD_DANE_ANM'])['COD_DANE_ANM'].agg('count').reset_index(name='Count'))
viv_tot.rename(columns={"Count": "Viviendas"}, inplace=True)

# Informacion del IPM
ipm = pd.read_csv("imp_manzanas.csv")
# ipm.info()
ipm.drop(columns="Unnamed: 0", inplace=True)
ipm.rename(columns={"cod_dane": "COD_DANE_ANM"}, inplace=True)

# Base por manzanas
manzanas = pop_man.merge(hog_tot, how = 'outer', on = ['COD_DANE_ANM'])
manzanas = manzanas.merge(viv_tot, how = 'outer', on = ['COD_DANE_ANM'])
manzanas = manzanas.merge(ipm, how = 'left', on = ['COD_DANE_ANM'])


manzanas.to_csv('Censo_manzanas.csv', index=False)

manzanas = pd.read_csv("Censo_manzanas.csv")

dup = manzanas.pivot_table(index=['COD_DANE_ANM'], aggfunc='size')
len(dup)
len(manzanas)

codmz = pd.read_excel("codmz.xlsx", engine="openpyxl")
# codmz.set_index('OBJECTID',inplace=True)

mz = codmz.merge(manzanas, how='left', left_on='MANZ_CCNCT', right_on='COD_DANE_ANM')

mz.to_excel('manzanas.xlsx', index=False, engine='xlsxwriter')
