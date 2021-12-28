""" 
Script para unificar Censo 2018 
http://microdatos.dane.gov.co/index.php/catalog/643/get_microdata
"""

import wget
import ssl
import os
import re
import zipfile
from os import walk
import pandas as pd

mypath = "/Users/campopinillos/OneDrive - Instituto Colombiano de Bienestar Familiar/Actividades/03 Indice"
os.chdir(mypath)
print(os.getcwd())

ssl._create_default_https_context = ssl._create_unverified_context

url = "http://formularios.dane.gov.co/Anda_4_1/CNPV_2018/"

dptos = {'05Antioquia' :'05_Antioquia', '08Atlantico' : '08_Atlantico', 
'11Bogota' : '11_Bogota', '13Bolivar' : '13_Bolivar', '15Boyaca' : '15_Boyaca', 
'17Caldas' : '17_Caldas', '18Caqueta' : '18_Caqueta', '19Cauca' : '19_Cauca', 
'20Cesar' : '20_Cesar', '23Cordoba' : '23_Cordoba', '25Cundinamarca' : '25_Cundinamarca', 
'27Choco' : '27_Choco', '41Huila' : '41_Huila', '44LaGuajira' : '44_LaGuajira', 
'47Magdalena' : '47_Magdalena', '50Meta' : '50_Meta', '52Narino' : '52_Narino', 
'54NSantander' : '54_NorteDeSantander', '63Quindio' : '63_Quindio', '66Risaralda' : '66_Risaralda', 
'68Santander' : '68_Santander', '70Sucre' : '70_Sucre', '73Tolima' : '73_Tolima', 
'76Valle' : '76_ValleDelCauca', '81Arauca' : '81_Arauca', '85Casanare' : '85_Casanare', 
'86Putumayo' : '86_Putumayo', '88SanAndres' : '88_SanAndresProvidenciaYSantaCatalina', 
'91Amazonas' : '91_Amazonas', '94Guainia' : '94_Guainia', '95Guaviare' : '95_Guaviare', 
'97Vaupes' : '97_Vaupes', '99Vichada' : '99Vichada'}

for k in dptos.keys():
	wget.download(url + dptos[k], k + '.zip')

for k in dptos.keys():
	with zipfile.ZipFile(k + '.zip',"r") as zip_ref:
		zip_ref.extractall()

for f in os.listdir(mypath):
    if re.search(".zip", f):
        os.remove(os.path.join(mypath, f))

for dirpath, dirnames, filenames in os.walk(".", topdown=False):
	for name in filenames:
		if re.search("CSV.zip", name):
			with zipfile.ZipFile(os.path.join(dirpath, name),"r") as zip_ref:
				zip_ref.extractall(path= dirpath)
	for name in filenames:
		if re.search(".zip", name):
			os.remove(os.path.join(dirpath, name))


def DataFrame(pattern="PER"):
	li = []
	for dirpath, dirnames, filenames in os.walk(".", topdown=False):
		for name in filenames:
			if re.search(pattern, name):
				df = pd.read_csv(os.path.join(dirpath, name))
				li.append(df)
	return pd.concat(li, axis=0, ignore_index=True)

persona = DataFrame(pattern="PER")

hogar = DataFrame(pattern="HOG")

vivienda = DataFrame(pattern="VIV")

mgeonal = DataFrame(pattern="MGN")

persona.head()
len(persona)
hogar.head()
len(hogar)
vivienda.head()
len(vivienda)

persona.to_csv('personas_2018.csv', index=False)
hogar.to_csv('hogares_2018.csv', index=False)
vivienda.to_csv('vivienda_2018.csv', index=False)
mgeonal.to_csv('mgn_2018.csv', index=False)
