
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

from math import sqrt
from time import time

#Variables no consideradas  "id_registro",
VarNames = ("Nivel_padreUni", "porc_etnica_2018", "porc_indigena_2018", "Homicidios_2017", "Homicidios_2018", "Homicidios_2019", "Suicidios_2017", "Suicidios_2018", "Suicidios_2019", "llave_hogar", "Ind_nivel_sisben_4", "field1", "Unnamed: 0", "cod_dpto", "Cod_clase", "Tip_vivienda", "Tip_mat_paredes", "Tip_mat_pisos", "Ind_tiene_energia", "Tip_estrato_energia", "Ind_tiene_alcantarillado", "Ind_tiene_gas", "Ind_tiene_recoleccion", "Ind_tiene_acueducto", "Num_hogares_vivienda", "Tip_ocupa_vivienda", "Num_cuartos_exclusivos", "Num_cuartos_dormir", "Num_cuartos_unicos_dormir", "Tip_sanitario", "Tip_ubi_sanitario", "Tip_uso_sanitario", "Tip_uso_agua_beber", "Tip_elimina_basura", "Ind_tiene_cocina", "Tip_prepara_alimentos", "Tip_uso_cocina", "Tip_energia_cocina", "Ind_tiene_nevera", "Ind_tiene_lavadora", "Ind_tiene_pc", "Ind_tiene_internet", "Ind_tiene_moto", "Ind_tiene_tractor", "Ind_tiene_carro", "Ind_tiene_bien_raiz", "Vlr_gasto_alimento", "Vlr_total_gastos", "Num_habita_vivienda", "Num_personas_hogar", "Sexo_persona", "edad", "Tip_parentesco", "Ind_discap_ver", "Ind_discap_oir", "Ind_discap_hablar", "Ind_discap_moverse", "Ind_discap_salir", "Ind_discap_entender", "Ind_discap_ninguna", "Tip_seg_social", "Ind_enfermo_30", "Ind_acudio_salud", "Ind_fue_atendido_salud", "Ind_recibe_comida", "Ind_leer_escribir", "Ind_estudia", "Ind_grupo_sisben_4", "privado_logroeduca", "privado_analfabe", "privado_Inasistencia", "privado_Rezago", "privado_PI", "TI", "privado_desemplarga", "privado_trabajoinfo", "privado_asegura", "privado_accesosalud", "privado_agua", "privado_excreta", "privado_suelo", "privado_pared", "privado_hacina", "Noprivaciones", "IndicadorPobrezaMulti", "hecho_victimas_30062020", "Unidos_FA_20052020", "Marca_Unidos_16_18", "Marca_Unidos_19", "Marca_FA", "ANIO_PARD_10_2020", "CENSO_INDIGENA", "registro_discapacidad", "prev_servicio_Oct_2020", "ingresos_hogar", "ingresos_promP", "gasto_ppers", "gasto_alim_pers", "ingresos_promP_imp", "gasto_ppers_imp", "gasto_alim_pers_imp", "porc_gasto_alim", "union_temp", "n_ninos", "TIpo_Hijo", "EdadNNA_inter", "Jefat_fem", "TIPO_FAMI", "Acti_padreUni", "Acti_madreUni", "Gene_Ingr", "Nivel_padreUni", "Nivel_madreUni", "Edad_padreUni", "Edad_madreUni", "DIF_EDAD_PADRES", "Edad_padreUni_TIL4", "Edad_padreUni_TIL5", "Edad_madreUni_TIL4", "Edad_madreUni_TIL5", "DIF_EDAD_PADRES_TIL4", "DIF_EDAD_PADRES_TIL5", "Uni_dias_agua", "Uni_acceso_agua", "Ind_afec_eventonatural", "num_afec_eventonatural", "MotivoPARD_original", "Motivo_Denuncia2020_Original", "Motivo_Denuncia201719_Original", "Vulnera", "Motivo_unif", "PARD_Denuncia", "ExisteDesnutricion", "Tomas_NivelDesnutricionMax", "ExisteReincidencia")

ArchivoMuestra = "Muestra_Sisben_Base_AutomaticCluster.csv"

SaveBarplot = True

def main():  
    df_Total   = pd.read_csv('Muestra_Sisben_Base_TotalSinMuestreo.csv', encoding = "ISO-8859-1", low_memory=False)
    df_Muestra = pd.read_csv(ArchivoMuestra,                             encoding = "ISO-8859-1", low_memory=False)
    
    # Generate two normal distributions around different means
    FailedVars = []
    Percent_Simil  = []
    for varName in VarNames:
        try :
            BaseTotal = df_Total[varName].values
            Muestra   = df_Muestra[varName].values
            
            # Create two overlayed histograms
            FreqBase, binsB, _ = plt.hist(BaseTotal,   alpha=0.6 , weights=np.ones(len(BaseTotal)) / len(BaseTotal))           
            FreqMuestra, _, _  = plt.hist(Muestra, bins = binsB, alpha=0.6, weights=np.ones(len(Muestra)) / len(Muestra))
            
            Similitud=SimilitudDistribuciones(FreqBase,FreqMuestra)
            Percent_Simil.append(Similitud)
            
            print("%.2f %%" % (100*Similitud) + " Similitud de "+varName)
            
            if SaveBarplot :
                plt.legend(["BaseTotal", "Muestra"])
                plt.ylabel("Distribución Percentual")
                plt.xlabel("Valor")
                plt.title(varName+ " similitud = %.2f %%" % (100*Similitud))
                plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
                plt.savefig("Distribucion_"+varName+ ".png") 
                plt.clf()
        except :
            FailedVars.append(varName)
    
    bins_new = [x/100.0 for x in range(0,101,5)]    
    plt.hist(Percent_Simil, bins = bins_new, alpha=0.6)           
    
    PromSimil = sum(Percent_Simil)/len(Percent_Simil)
    plt.ylabel("Similitud")
    plt.xlabel("Porcentajes")
    plt.title("Similitud Prom = %.2f %%" % (100*PromSimil))        
    plt.xticks(bins_new, bins_new, rotation ='vertical') 
    plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
    plt.savefig("Total_Distribucion.png") 
    plt.clf() 
            
    print()
    print("Error en Similitud de ")
    for varName in FailedVars:
        print(varName)
    
#Dotpoint to compute diferences between distributions    
def dotpoint(V1,V2):
    VectProd = [x[0]*x[1] for x in zip(V1,V2)]    
    Sumprod = sum(VectProd)    
    return Sumprod    
    
def vectorMagnuitude(V1):
    return (sqrt(dotpoint(V1,V1)))

def NormalizeVect(V1):    
    Magnitud = vectorMagnuitude(V1)
    VReturn =  [x/Magnitud for x in V1]
    return VReturn

def SimilitudDistribuciones(Distrib1,Distrib2):
    #Cambiamos los porcentajes en los vectores por comparacion 
    #entre los porcentajes de la distribucion 1 y 2 Asi porcentajes 
    #bajos en las distribuciones tendran igual peso que los grandes
    NormDist1 = []
    for x in Distrib1:
        if x != 0 :
            NormDist1.append(1.0)
        else :
            NormDist1.append(0.0)
    
    NormDist2 = []
    for x in zip(Distrib2,Distrib1):
        if x[1] != 0 :
            NormDist2.append(x[0]/x[1])
        else :
            NormDist2.append(0.0)
    
    NormDist1 = NormalizeVect(NormDist1)    
    NormDist2 = NormalizeVect(NormDist2)
    
    Similitud = dotpoint(NormDist1,NormDist2)
    
    return (Similitud)
        
if __name__ == '__main__':
    startTime = time()
    main()    
    print("Time spent ", (time()-startTime))
    

'''
cod_mpio
ruralidad
porc_etnica_2018
porc_indigena_2018
Homicidios_2017
Homicidios_2018
Homicidios_2019
Suicidios_2017
Suicidios_2018
Suicidios_2019
llave_hogar
Ind_nivel_sisben_4
field1
Unnamed: 0
id_registro
cod_dpto
Cod_clase
Tip_vivienda
Tip_mat_paredes
Tip_mat_pisos
Ind_tiene_energia
Tip_estrato_energia
Ind_tiene_alcantarillado
Ind_tiene_gas
Ind_tiene_recoleccion
Ind_tiene_acueducto
Num_hogares_vivienda
Tip_ocupa_vivienda
Num_cuartos_exclusivos
Num_cuartos_dormir
Num_cuartos_unicos_dormir
Tip_sanitario
Tip_ubi_sanitario
Tip_uso_sanitario
Tip_uso_agua_beber
Tip_elimina_basura
Ind_tiene_cocina
Tip_prepara_alimentos
Tip_uso_cocina
Tip_energia_cocina
Ind_tiene_nevera
Ind_tiene_lavadora
Ind_tiene_pc
Ind_tiene_internet
Ind_tiene_moto
Ind_tiene_tractor
Ind_tiene_carro
Ind_tiene_bien_raiz
Vlr_gasto_alimento
Vlr_total_gastos
Num_habita_vivienda
Num_personas_hogar
Sexo_persona
edad
Tip_parentesco
Ind_discap_ver
Ind_discap_oir
Ind_discap_hablar
Ind_discap_moverse
Ind_discap_salir
Ind_discap_entender
Ind_discap_ninguna
Tip_seg_social
Ind_enfermo_30
Ind_acudio_salud
Ind_fue_atendido_salud
Ind_recibe_comida
Ind_leer_escribir
Ind_estudia
Ind_grupo_sisben_4
privado_logroeduca
privado_analfabe
privado_Inasistencia
privado_Rezago
privado_PI
TI
privado_desemplarga
privado_trabajoinfo
privado_asegura
privado_accesosalud
privado_agua
privado_excreta
privado_suelo
privado_pared
privado_hacina
Noprivaciones
IndicadorPobrezaMulti
hecho_victimas_30062020
Unidos_FA_20052020
Marca_Unidos_16_18
Marca_Unidos_19
Marca_FA
ANIO_PARD_10_2020
CENSO_INDIGENA
registro_discapacidad
prev_servicio_Oct_2020
ingresos_hogar
ingresos_promP
gasto_ppers
gasto_alim_pers
ingresos_promP_imp
gasto_ppers_imp
gasto_alim_pers_imp
porc_gasto_alim
union_temp
n_ninos
TIpo_Hijo
EdadNNA_inter
Jefat_fem
TIPO_FAMI
Acti_padreUni
Acti_madreUni
Gene_Ingr
Nivel_padreUni
Nivel_madreUni
Edad_padreUni
Edad_madreUni
DIF_EDAD_PADRES
Edad_padreUni_TIL4
Edad_padreUni_TIL5
Edad_madreUni_TIL4
Edad_madreUni_TIL5
DIF_EDAD_PADRES_TIL4
DIF_EDAD_PADRES_TIL5
Uni_dias_agua
Uni_acceso_agua
Ind_afec_eventonatural
num_afec_eventonatural
MotivoPARD_original
Motivo_Denuncia2020_Original
Motivo_Denuncia201719_Original
Vulnera
Motivo_unif
PARD_Denuncia
ExisteDesnutricion
Tomas_NivelDesnutricionMax
ExisteReincidencia








field1, Tot_viviendas, Unnamed: 0, Cod_clase, Tot_hogares,  Num_cuartos_vivienda,
Num_hogares_vivienda,  Num_cuartos_dormir, Num_cuartos_unicos_dormir, Num_horas_llega, 
Num_dias_llega, Vlr_gasto_educacion, Vlr_gasto_transporte, Vlr_gasto_salud, 
Vlr_gasto_serv_publicos, Vlr_gasto_celular, Vlr_gasto_otros, Vlr_total_gastos, 
Vlr_gasto_arriendo, Vlr_gasto_alimento, Vlr_ingr_salario, Vlr_ingr_honorarios, 
Vlr_ingr_cosecha, Vlr_ingr_pension, Vlr_ingr_remesa_pais, Vlr_ingr_remesa_exterior, 
Vlr_ingr_arriendos, Vlr_otros_ingresos, Vlr_ingr_fam_accion, Vlr_ingr_col_mayor, 
Vlr_ingr_otro_subsidio, Num_cuartos_exclusivos, Num_habita_vivienda, Num_evento_inundacion, 
Num_evento_terremoto, Num_evento_vendaval, Num_evento_avalancha, Num_evento_incendio, 
Num_evento_hundimiento, Num_personas_posibles, Num_personas_hogar, Num_sem_buscando, 
Num_mes_ingr_cosecha, edad, edad_padre, edad_madre, edad_jefe, edad_conyuge_Padre, 
edad_conyuge_Madre, edad_conyuge_Jefe, edad_grupo, edad_Max, grado_mat_2017, 
grado_mat_2018, grado_mat_2019, grado_mat_2020, 


llave_hogar, Menor,   id_registro, cod_dpto, cod_mpio, 
Ord_vivienda, Tip_vivienda, Tip_mat_paredes, Tip_mat_pisos, 
Ind_tiene_energia, Tip_estrato_energia, Ind_tiene_alcantarillado, Ind_tiene_gas, 
Ind_tiene_recoleccion, Ind_tiene_acueducto, Tip_estrato_acueducto,  
Tip_ocupa_vivienda, 
Tip_sanitario, Tip_ubi_sanitario, Tip_uso_sanitario, 
Tip_origen_agua, Ind_agua_llega_7dias, Ind_agua_llega_24horas, 
Tip_uso_agua_beber, Tip_elimina_basura, Ind_tiene_cocina, 
Tip_prepara_alimentos, Tip_uso_cocina, Tip_energia_cocina, Ind_tiene_nevera, 
Ind_tiene_lavadora, Ind_tiene_pc, Ind_tiene_internet, Ind_tiene_moto, Ind_tiene_tractor, 
Ind_tiene_carro, Ind_tiene_bien_raiz, Ind_gasto_alimento, 
Ind_gasto_transporte, Ind_gasto_educacion, 
Ind_gasto_salud, Ind_gasto_serv_publicos, 
Ind_gasto_celular, Ind_gasto_arriendo, 
Ind_gasto_otros, 
Ind_evento_inundacion, Ind_evento_avalancha, 
Ind_evento_terremoto, Ind_evento_incendio, 
Ind_evento_vendaval, Ind_evento_hundimiento, 
Ind_declaracion, Ind_escaner, Sexo_persona, 
Tip_documento, Tip_parentesco, Tip_estado_civil, Ind_conyuge_vive_hogar, 
Ide_conyuge, Ind_padre_vive_hogar, Ind_pariente_domestico, Ide_serv_domestico, 
Ind_discap_ver, Ind_discap_oir, Ind_discap_hablar, Ind_discap_moverse, Ind_discap_salir, 
Ind_discap_entender, Ind_discap_ninguna, Tip_seg_social, Ind_enfermo_30, Ind_acudio_salud, 
Ind_fue_atendido_salud, Ind_esta_embarazada, Ind_tuvo_hijos, Ind_recibe_comida, 
Ind_leer_escribir, Ind_estudia, Niv_educativo, Grado_alcanzado, Ind_fondo_pensiones, 
Tip_actividad_mes, Tip_empleado, 
Ind_grupo_sisben_4, Ind_nivel_sisben_4, 
privado_logroeduca, privado_analfabe, privado_Inasistencia, privado_Rezago, privado_PI, 
TI, privado_desemplarga, privado_trabajoinfo, privado_asegura, privado_accesosalud, 
privado_agua, privado_excreta, privado_suelo, privado_pared, privado_hacina, 
Noprivaciones, IndicadorPobrezaMulti, PUNTAJE_SISBEN_III, CruzoRUV_30062020, 
hecho_victimas_30062020, Unidos_FA_20052020, Marca_Unidos_16-18, Marca_Unidos_19, 
Marca_FA, INGRESO_PARD_10_2020, CODIGO_CASO_PARD_10_2020, ANIO_PARD_10_2020, 
MOTIVO_INGRESO_PARD_10_2020, CENSO_INDIGENA, EDAD_DIC31_2020, EDAD_MAR31_2021, 
Padre_asociado_por, Padre_id_registro, Padre_Ide_ficha_origen, Padre_Sexo_persona, 
Padre_Ind_grupo_sisben_4, Padre_Ind_nivel_sisben_4, Padre_Ide_conyuge, 
Padre_Ide_hogar, Padre_Ide_persona, Padre_Tip_parentesco, nivel_padre, 
Padre_Grado_alcanzado, actividad_padre, Padre_Tip_empleado, Padre_Vlr_ingr_salario, 
Padre_Vlr_ingr_honorarios, Padre_Vlr_ingr_cosecha, Padre_Vlr_ingr_pension, 
Padre_Vlr_ingr_remesa_pais, Padre_Vlr_ingr_remesa_exterior, Padre_Vlr_ingr_arriendos, 
Padre_Vlr_otros_ingresos, Padre_Vlr_ingr_fam_accion, Padre_Vlr_ingr_col_mayor, 
Padre_Vlr_ingr_otro_subsidio, Madre_asociado_por, Madre_id_registro, 
Madre_Ide_ficha_origen, Madre_Sexo_persona, Madre_Ind_grupo_sisben_4, 
Madre_Ind_nivel_sisben_4, Madre_Ide_conyuge, Madre_Ide_hogar, Madre_Ide_persona, 
Madre_Tip_parentesco, nivel_madre, Madre_Grado_alcanzado, actividad_madre, 
Madre_Tip_empleado, Madre_Vlr_ingr_salario, Madre_Vlr_ingr_honorarios, 
Madre_Vlr_ingr_cosecha, Madre_Vlr_ingr_pension, Madre_Vlr_ingr_remesa_pais, 
Madre_Vlr_ingr_remesa_exterior, Madre_Vlr_ingr_arriendos, Madre_Vlr_otros_ingresos, 
Madre_Vlr_ingr_fam_accion, Madre_Vlr_ingr_col_mayor, Madre_Vlr_ingr_otro_subsidio, 
Jefe_de_hogar, Jefe_id_registro, Jefe_Ide_ficha_origen, Jefe_Sexo_persona, 
Jefe_Ind_grupo_sisben_4, Jefe_Ind_nivel_sisben_4, Jefe_Ide_conyuge, Jefe_Ide_hogar, 
Jefe_Ide_persona, Jefe_Tip_parentesco, nivel_jefe, Jefe_Grado_alcanzado, actividad_jefe, 
Jefe_Tip_empleado, Jefe_Vlr_ingr_salario, Jefe_Vlr_ingr_honorarios, Jefe_Vlr_ingr_cosecha, 
Jefe_Vlr_ingr_pension, Jefe_Vlr_ingr_remesa_pais, Jefe_Vlr_ingr_remesa_exterior, 
Jefe_Vlr_ingr_arriendos, Jefe_Vlr_otros_ingresos, Jefe_Vlr_ingr_fam_accion, 
Jefe_Vlr_ingr_col_mayor, Jefe_Vlr_ingr_otro_subsidio, prev_servicio_2017, 
prev_servicio_2018, prev_servicio_2019, tipo_jornada_mat_2017, 
estado_definitivo_mat_2017, tipo_jornada_mat_2018, 
estado_definitivo_mat_2018, tipo_jornada_mat_2019, 
estado_definitivo_mat_2019, registro_discapacidad, al_sistemanervioso, 
MotivoDenunciaRPT_PetsRAVDsSRDs01072017_31082020s, MotivoDenunciaRPT_PetsSIM_SRDsRAVDs0101_31102020, 
niv_educativo_conyuge_Padre, sexo_conyuge_Padre, actividad_conyuge_Padre, 
niv_educativo_conyuge_Madre, sexo_conyuge_Madre, actividad_conyuge_Madre, 
niv_educativo_conyuge_Jefe, sexo_conyuge_Jefe, actividad_conyuge_Jefe, 
prev_servicio_Oct_2020, tipo_jornada_mat_2020, estado_definitivo_mat_2020, 
union_temp, n_ninos, Mayor, TIpo_Hijo, EdadNNA_inter, Jefat_fem, 
Con padre, Con madre, Con conyugue madre, Con conyugue padre, TIPO_FAMI, Acti_padreUni, 
Acti_madreUni, Gene_Ingr, Nivel_padreUni, Nivel_madreUni, Edad_padreUni, Edad_madreUni, 
DIF_EDAD_PADRES, Edad_padreUni_TIL4, Edad_padreUni_TIL5, Edad_madreUni_TIL4, 
Edad_madreUni_TIL5, DIF_EDAD_PADRES_TIL4, DIF_EDAD_PADRES_TIL5, ESTUDIA_2017, 
ESTUDIA_2018, ESTUDIA_2019, ESTUDIA_2020, duplicados2, Vulnera, Motivo_unif, ingresos, 
ingresos_Sum, ingresos_promP, Jefe_Tip_empleado_Uni, Madre_Tip_empleado_Uni, 
Padre_Tip_empleado_Uni, Tip_empleado_Uni, 

ExisteDesnutricion, Tomas_NivelDesnutricionMax, ExisteReincidencia
'''





