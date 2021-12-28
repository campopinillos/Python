SELECT Cust_ID, SUM(Revenue) AS REV FROM Transactions
GROUP BY Cust_ID
ORDER BY REV DESC
LIMIT 5;


SELECT Cust_ID, SUM(Revenue) AS REV FROM Transactions AS Total
JOIN SELECT DISTINCT Cust_ID FROM Transactions AS Cloth
WHERE Cloth.Product_ID IN (
	SELECT * FROM Products
	WHERE Product_Type = "Clothing") 
ON Total.Cust_ID = Cloth.Cust_ID
GROUP BY Total.Cust_ID
ORDER BY Total.REV DESC
LIMIT 5;

create table phones (
      name varchar(20) not null unique,
      phone_number integer not null unique
);

create table calls (
      id integer not null,
      caller integer not null,
      callee integer not null,
      duration integer not null,
      unique(id)
  );

insert into phones values ('Jack', 1234);
insert into phones values ('Lena', 3333);
insert into phones values ('Mark', 9999);
insert into phones values ('Anna', 7582);
insert into calls values (25, 1234, 7582, 8);
insert into calls values (7, 9999, 7582, 1);
insert into calls values (18, 9999, 3333, 4);
insert into calls values (2, 7582, 3333, 3);
insert into calls values (3, 3333, 1234, 1);
insert into calls values (21, 3333, 1234, 1);



SELECT C.contest_id, C.hacker_id, C.name, SUM(total_submissions), SUM(total_accepted_submissions), SUM(total_views), SUM(total_unique_views)
FROM Contests AS C 
JOIN Colleges AS Col ON C.contest_id=Col.contest_id
JOIN Challenges AS Ch ON Ch.college_id=Col.college_id
JOIN View_Stats AS V ON V.challenge_id=Ch.challenge_id
JOIN Submission_Stats AS S ON S.challenge_id=Ch.challenge_id

cod_dpto|cod_mpio|porc_etnica_2018|porc_indigena_2018|llave_hogar|Ind_nivel_sisben_4|Coord_x_auto_rec|Coord_y_auto_rec|Coord_x_auto_enc|Coord_y_auto_enc|Ind_tiene_energia|Ind_tiene_alcantarillado|Ind_tiene_gas|Ind_tiene_recoleccion|Ind_tiene_acueducto|Num_hogares_vivienda|Ind_tiene_cocina|Ind_tiene_nevera|Ind_tiene_lavadora|Ind_tiene_pc|Ind_tiene_internet|Vlr_gasto_transporte|Vlr_gasto_educacion|Vlr_gasto_salud|Vlr_gasto_serv_publicos|Vlr_gasto_celular|Vlr_gasto_arriendo|Vlr_gasto_otros|Num_personas_hogar|Sexo_persona|Num_documento|fec_nacimiento|edad|Ind_discap_bañarse|Ind_discap_ninguna|Ind_fue_atendido_salud|Ind_estudia|ind_ingr_salario|Vlr_ingr_cosecha|Vlr_ingr_arriendos|Vlr_ingr_col_mayor|ide_Unigasto|IndicadorPobrezaMulti|privado_logroeduca|privado_analfabe|privado_Inasistencia|privado_Rezago|privado_PI|TI|privado_desemplarga|privado_trabajoinfo|privado_asegura|privado_accesosalud|privado_agua|privado_excreta|privado_suelo|privado_pared|privado_hacina|ide_Ug|persug|Capital|prediction|marca|estado|Linea_p|replicacion|Noprivaciones|Clasificacion|id_registro|apellido1_conyuge_Padre|apellido2_conyuge_Padre|apellido1_conyuge_Madre|apellido2_conyuge_Madre|apellido1_conyuge_Jefe|apellido2_conyuge_Jefe|CODIGO CASO|hecho_victimas_30062020|ingresos|ingresos_hogar|ingresos_ppers_Median|ingresos_promP_imp|gasto_ppers_imp|gasto_alim_ppers_imp|porc_gasto_alim|union_temp|n_ninos|Jefat_fem|Edad_padreUni|Edad_madreUni|DIF_EDAD_PADRES|pers_por_cuarto|pers_por_cuarto_exclusivo|anno_encuesta|EXTRAEDAD_2021|ESTUDIA_2021|Uni_dias_agua|Ind_afec_eventonatural|num_afec_eventonatural|atendido_prevencion|Ha_coca|Estudia|Extraedad|TasaHomicidios_0a17|TasaHomicidios_total|TasaSuicidios_0a17|TasaSuicidios_total|TasaVIF_0a17|TasaVIF_total|TasaVIP_0a17|TasaVIP_total|TasaVS_0a17|TasaVS_total|vict_delsexual_0a17|vict_delsexual_total|Fecundi_10a14|Fecundi_15a19|PobRural|Edad_padres_mayor|Edad_padres_menor|ComparteCocina_Sanitario|Estrato|motivo_pard_agrupado|v_sexual|maltrato|anno_vulnera|anno_vsexual|anno_maltrato|dif_annos_vsexual|dif_annos_maltrato|dif_annos_vulnera|edad_vulnera_vsexual|edad_vulnera_maltrato|Error|id|Cod_clase_2|Cod_clase_3|Ind_grupo_sisben_4_B|Ind_grupo_sisben_4_C|Ind_grupo_sisben_4_D|ruralidad_2|ruralidad_3|ruralidad_4|Tip_vivienda_2|Tip_vivienda_3|Tip_vivienda_4|Tip_vivienda_5|Tip_ocupa_vivienda_2|Tip_ocupa_vivienda_3|Tip_ocupa_vivienda_4|Tip_ocupa_vivienda_5|Tip_seg_social_1|Tip_seg_social_2|Tip_seg_social_3|Tip_seg_social_9|Ind_acudio_salud_1|Ind_fue_atendido_salud_1|Tip_cuidado_niños_2|Tip_cuidado_niños_3|Tip_cuidado_niños_4|Tip_cuidado_niños_5|Tip_cuidado_niños_6|Tip_cuidado_niños_7|Tip_cuidado_niños_8|Tip_cuidado_niños_9|Ind_recibe_comida_1|Ind_leer_escribir_1|TIpo_Hijo_2|TIpo_Hijo_3|TIPO_FAMI_2|TIPO_FAMI_3|TIPO_FAMI_4|TIPO_FAMI_5|TIPO_FAMI_6|Gene_Ingr_2|Gene_Ingr_3|Gene_Ingr_4|Nivel_padreUni_1|Nivel_padreUni_2|Nivel_padreUni_3|Nivel_padreUni_4|Nivel_padreUni_5|Nivel_padreUni_6|Nivel_padreUni_7|Nivel_padreUni_8|Nivel_madreUni_1|Nivel_madreUni_2|Nivel_madreUni_3|Nivel_madreUni_4|Nivel_madreUni_5|Nivel_madreUni_6|Nivel_madreUni_7|Nivel_madreUni_8|Edad_padreUni_TIL5_1|Edad_padreUni_TIL5_2|Edad_padreUni_TIL5_3|Edad_padreUni_TIL5_4|Edad_padreUni_TIL5_5|Edad_madreUni_TIL5_1|Edad_madreUni_TIL5_2|Edad_madreUni_TIL5_3|Edad_madreUni_TIL5_4|Edad_madreUni_TIL5_5|DIF_EDAD_PADRES_TIL5_1|DIF_EDAD_PADRES_TIL5_2|DIF_EDAD_PADRES_TIL5_3|DIF_EDAD_PADRES_TIL5_4|DIF_EDAD_PADRES_TIL5_5|Tipo_jorna_2|Tipo_jorna_3|Tipo_jorna_4|Tipo_jorna_5|Tipo_jorna_6|Tipo_jorna_7