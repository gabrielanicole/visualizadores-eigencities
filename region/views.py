import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from region.models import Hogar, CHogar, CPersona, Persona, Vivienda
from django.db.models import Min, Max
from django.core.serializers import serialize


# Create your views here.

def index(request):
	#
	if request.method == 'POST':
		print("ENPOST")
		resp = ""

		if 'valor_seleccion' in request.POST:
			redcode_manz= request.POST['redcode_valor'] 
			valor_criterio= request.POST['valor_seleccion']
			print("valor_criterio")
			print(valor_criterio)

			print (valor_criterio.find(","))
			if (valor_criterio.find(",")>0 ):
				valor_criterio = valor_criterio.split(',')
				print(valor_criterio)
				valores = valor_criterio
				data = ""
				for valor in valores:
					print(valor)
					resp = contenido_indicadores(redcode_manz, valor)
					print("respuesta_1")
					print(resp["respuesta"])
					data += '<br/><br/>' + resp["respuesta"] if data != "" else resp["respuesta"]

				resp['respuesta'] = data 


			else:
				resp = contenido_indicadores(redcode_manz, valor_criterio)
			
			return JsonResponse(resp, safe=False)
			 

		elif 'nuevoMapa_disc' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'resdiscap_0','resdiscap_1','resdiscap_2', 'resdiscap_3','resdiscap_4','resdiscap_5',
			'resdiscap_6', 'resdiscap_7', 'resdiscap_8', 'resdiscap_9', 'discapac_0', 'discapac_1').order_by('-discapac_0')
			values_list = list(persona_vald.values('redcode', 
			'resdiscap_0','resdiscap_1','resdiscap_2', 'resdiscap_3','resdiscap_4','resdiscap_5',
			'resdiscap_6', 'resdiscap_7', 'resdiscap_8', 'resdiscap_9', 'discapac_0', 'discapac_1'))

			discapacidades_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'resdiscap_1','resdiscap_2', 'resdiscap_3','resdiscap_4','resdiscap_5',
			'resdiscap_6').order_by('id')

			json_disc = []
			for i in discapacidades_vald:
				maximo = max(i[1],i[2],i[3],i[4],i[5])
				#jsobj["a"]["b"]["e"].append({"f":var3, "g":var4, "h":var5})
				if maximo == '0' :
					json_disc.append({'redcode': i[0], 'discapacidad': 'ninguna', 'cantidad':maximo,
					'd1':i[1],'d2':i[2],'d3':i[3],'d4':i[4],'d5':i[5]})

				else:
					if i[1] == maximo:
						json_disc.append({'redcode': i[0], 'discapacidad': 'ceguera', 'cantidad':maximo,
						 'd1':i[1],'d2':i[2],'d3':i[3],'d4':i[4],'d5':i[5] })
					else:
						if i[2] == maximo:
							json_disc.append({'redcode': i[0], 'discapacidad': 'sordera', 'cantidad':maximo,
							 'd1':i[1],'d2':i[2],'d3':i[3],'d4':i[4],'d5':i[5]})
						else:
							if i[3] == maximo:
								json_disc.append({'redcode': i[0], 'discapacidad': 'mudez', 'cantidad':maximo,
								'd1':i[1],'d2':i[2],'d3':i[3],'d4':i[4],'d5':i[5]  })
							else:
								if i[4] == maximo:
									json_disc.append({'redcode': i[0], 'discapacidad': 'lisiado_paralisado', 'cantidad':maximo,
									 'd1':i[1],'d2':i[2],'d3':i[3],'d4':i[4],'d5':i[5]})
								else:
									if i[5] == maximo:
										json_disc.append({'redcode': i[0], 'discapacidad': 'mental', 'cantidad':maximo,
										 'd1':i[1],'d2':i[2],'d3':i[3],'d4':i[4],'d5':i[5] })

			maximo_disc = persona_vald[0][11]
			minimo_disc = persona_vald[len(persona_vald)-1][11]

			values_list = { 'tipos_disc': values_list, 'min_disc': minimo_disc, 'max_disc': maximo_disc, 'por_disc': json_disc}
			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_cultura' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'cultura_1','cultura_2', 'cultura_3', 'cultura_4','cultura_5','cultura_6', 'cultura_7',
			 'cultura_8','cultura_9' ).order_by('id')
			values_list = list(persona_vald.values('redcode', 
			'cultura_1','cultura_2', 'cultura_3', 'cultura_4','cultura_5','cultura_6', 'cultura_7',
			 'cultura_8','cultura_9' )) 
			json_gen = []
			for i in persona_vald:
				maximo = max(i[1],i[2], i[3],i[4], i[5],i[6], i[7],i[8])
				if maximo == 0 or maximo == '0' :
					json_gen.append({'redcode': i[0], 'cultura': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_gen.append({'redcode': i[0], 'cultura': 'Alacalufe (Kawashkar)', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_gen.append({'redcode': i[0], 'cultura': 'Atacameno', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_gen.append({'redcode': i[0], 'cultura': 'Aimara', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_gen.append({'redcode': i[0], 'cultura': 'Colla', 'cantidad':maximo})
								else:
									if maximo == i[5]:
										json_gen.append({'redcode': i[0], 'cultura': 'Mapuche', 'cantidad':maximo})
									else:
										if maximo == i[6]:
											json_gen.append({'redcode': i[0], 'cultura': 'Quechua', 'cantidad':maximo})
										else:
											if maximo == i[7]:
												json_gen.append({'redcode': i[0], 'cultura': 'Rapa Nui', 'cantidad':maximo})
											else:
												if maximo == i[8]:
													json_gen.append({'redcode': i[0], 'cultura': 'Yamana (Yagan)', 'cantidad':maximo})

			return JsonResponse(json_gen, safe=False)
		elif 'nuevoMapa_tipoEduc' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'tipoer_1','tipoer_2', 'tipoer_3', 'tipoer_4','tipoer_5','tipoer_6', 'tipoer_7',
			'tipoer_8','tipoer_9', 'tipoer_10', 'tipoer_11','tipoer_12','tipoer_13', 'tipoer_14',
			'tipoer_15').order_by('id')
			values_list = list(persona_vald.values('redcode', 
			'tipoer_1','tipoer_2', 'tipoer_3', 'tipoer_4','tipoer_5','tipoer_6', 'tipoer_7',
			'tipoer_8','tipoer_9', 'tipoer_10', 'tipoer_11','tipoer_12','tipoer_13', 'tipoer_14',
			'tipoer_15' )) 
			json_educ = []

			for i in persona_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5] + i[6] + i[7] + i[8] + i[9] + i[10] + i[11],
					i[12] + i[13], i[14], i[15])
				if maximo == 0 or maximo == '0' :
					json_educ.append({'redcode': i[0], 'educ': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_educ.append({'redcode': i[0], 'educ': 'No Asistio', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_educ.append({'redcode': i[0], 'educ': 'Pre-Basica', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_educ.append({'redcode': i[0], 'educ': 'Especial/Diferencial', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_educ.append({'redcode': i[0], 'educ': 'Basica/Primaria', 'cantidad':maximo})
								else:
									if maximo == i[5] + i[6] + i[7] + i[8] + i[9] + i[10] + i[11]:
										json_educ.append({'redcode': i[0], 'educ': 'Media', 'cantidad':maximo})
									else:
										if maximo == i[12] + i[13]:
											json_educ.append({'redcode': i[0], 'educ': 'Tecnica', 'cantidad':maximo})
										else:
											if maximo == i[14]:
												json_educ.append({'redcode': i[0], 'educ': 'Instituto Profesional', 'cantidad':maximo})
											else:
												if maximo == i[15]:
													json_educ.append({'redcode': i[0], 'educ': 'Universitaria', 'cantidad':maximo})

			return JsonResponse(json_educ, safe=False)

		elif 'nuevoMapa_religion' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'religion_1','religion_2', 'religion_3', 'religion_4','religion_5','religion_6', 'religion_7',
			'religion_8','religion_9').order_by('id')
			values_list = list(persona_vald.values('redcode', 
			'religion_1','religion_2', 'religion_3', 'religion_4','religion_5','religion_6', 'religion_7',
			'religion_8','religion_9')) 
			json_religion = []

			for i in persona_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
				if maximo == 0 or maximo == '0' :
					json_religion.append({'redcode': i[0], 'religion': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_religion.append({'redcode': i[0], 'religion': 'Catolica', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_religion.append({'redcode': i[0], 'religion': 'Evangelica', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_religion.append({'redcode': i[0], 'religion': 'Testigo de Jehova', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_religion.append({'redcode': i[0], 'religion': 'Judaica', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_religion.append({'redcode': i[0], 'religion': 'Mormon', 'cantidad':maximo})
									else:
										if maximo == i[6]:
											json_religion.append({'redcode': i[0], 'religion': 'Musulmana', 'cantidad':maximo})
										else:
											if maximo == i[7]:
												json_religion.append({'redcode': i[0], 'religion': 'Ortodoxa Profesional', 'cantidad':maximo})
											else:
												if maximo == i[8]:
													json_religion.append({'redcode': i[0], 'religion': 'Otra', 'cantidad':maximo})
												else:
													if maximo == i[9]:
														json_religion.append({'redcode': i[0], 'religion': 'Ninguna, ateo, agnostico', 'cantidad':maximo})

			return JsonResponse(json_religion, safe=False)

		elif 'nuevoMapa_trabajo' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'trabaja_1','trabaja_2', 'trabaja_3', 'trabaja_4','trabaja_5').order_by('id')
			values_list = list(persona_vald.values('redcode', 
			'trabaja_1','trabaja_2', 'trabaja_3', 'trabaja_4','trabaja_5')) 
			json_trabajo = []

			for i in persona_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5])
				if maximo == 0 or maximo == '0' :
					json_trabajo.append({'redcode': i[0], 'trabajo': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_trabajo.append({'redcode': i[0], 'trabajo': 'asalariado', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_trabajo.append({'redcode': i[0], 'trabajo': 'domestico', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_trabajo.append({'redcode': i[0], 'trabajo': 'cuenta propia', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_trabajo.append({'redcode': i[0], 'trabajo': 'empleador', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_trabajo.append({'redcode': i[0], 'trabajo': 'no remunerado', 'cantidad':maximo})
									
			return JsonResponse(json_trabajo, safe=False)

		elif 'nuevoMapa_hijos' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode',
				'hijos_0', 'hijos_1','hijos_2', 'hijos_3','hijos_4', 'hijos_5','hijos_6', 'hijos_7','hijos_8', 'hijos_9',
				'hijos_10', 'hijos_11','hijos_12', 'hijos_13','hijos_14', 'hijos_15','hijos_16', 'hijos_17','hijos_18', 'hijos_19',
				'hijos_20', 'hijos_21','hijos_22', 'hijos_23','hijos_24', 'hijos_25','hijos_26', 'hijos_27','hijos_28', 'hijos_29',
				'hijos_30', 'hijos_31','hijos_32', 'hijos_33','hijos_34', 'hijos_35','hijos_36', 'hijos_37','hijos_38', 'hijos_39',
				'hijos_40', 'hijos_41','hijos_42', 'hijos_43','hijos_44', 'hijos_45','hijos_46', 'hijos_47','hijos_48', 'hijos_49',
				'hijos_50', 'hijos_51','hijos_52', 'hijos_53','hijos_54', 'hijos_55','hijos_56', 'hijos_57','hijos_58', 'hijos_59',
				'hijos_60', 'hijos_61','hijos_62', 'hijos_63','hijos_64', 'hijos_65','hijos_66', 'hijos_67','hijos_68', 'hijos_69',
				'hijos_70', 'hijos_71','hijos_72', 'hijos_73','hijos_74', 'hijos_75','hijos_76', 'hijos_77','hijos_78', 'hijos_79',
				'hijos_80', 'hijos_81','hijos_82', 'hijos_83','hijos_84', 'hijos_85','hijos_86', 'hijos_87','hijos_88', 'hijos_89',
				'hijos_90', 'hijos_91','hijos_92', 'hijos_93','hijos_94', 'hijos_95','hijos_96', 'hijos_97','hijos_98',
				'hijos_99').order_by('-id')
			values_list = list(persona_vald.values('redcode',
				'hijos_0', 'hijos_1','hijos_2', 'hijos_3','hijos_4', 'hijos_5','hijos_6', 'hijos_7','hijos_8', 'hijos_9',
				'hijos_10', 'hijos_11','hijos_12', 'hijos_13','hijos_14', 'hijos_15','hijos_16', 'hijos_17','hijos_18', 'hijos_19',
				'hijos_20', 'hijos_21','hijos_22', 'hijos_23','hijos_24', 'hijos_25','hijos_26', 'hijos_27','hijos_28', 'hijos_29',
				'hijos_30', 'hijos_31','hijos_32', 'hijos_33','hijos_34', 'hijos_35','hijos_36', 'hijos_37','hijos_38', 'hijos_39',
				'hijos_40', 'hijos_41','hijos_42', 'hijos_43','hijos_44', 'hijos_45','hijos_46', 'hijos_47','hijos_48', 'hijos_49',
				'hijos_50', 'hijos_51','hijos_52', 'hijos_53','hijos_54', 'hijos_55','hijos_56', 'hijos_57','hijos_58', 'hijos_59',
				'hijos_60', 'hijos_61','hijos_62', 'hijos_63','hijos_64', 'hijos_65','hijos_66', 'hijos_67','hijos_68', 'hijos_69',
				'hijos_70', 'hijos_71','hijos_72', 'hijos_73','hijos_74', 'hijos_75','hijos_76', 'hijos_77','hijos_78', 'hijos_79',
				'hijos_80', 'hijos_81','hijos_82', 'hijos_83','hijos_84', 'hijos_85','hijos_86', 'hijos_87','hijos_88', 'hijos_89',
				'hijos_90', 'hijos_91','hijos_92', 'hijos_93','hijos_94', 'hijos_95','hijos_96', 'hijos_97','hijos_98',
				'hijos_99')) 
			json_hijos = []

			for i in persona_vald:
				suma_hijos_mas5 = i[6]+ i[7]+ i[8]+ i[9]+ i[10]

				suma_hijos_mas10 = ( i[11]+ i[12]+ i[13]+ i[14]+ i[15]+ i[16]+ i[17]+ i[18]+ i[19]+ i[20]
								+ i[21]+ i[22]+ i[23]+ i[24]+ i[25]+ i[26]+ i[27]+ i[28]+ i[29]+ i[30]
								+ i[31]+ i[32]+ i[33]+ i[34]+ i[35]+ i[36]+ i[37]+ i[38]+ i[39]+ i[40]
								+ i[41]+ i[42]+ i[43]+ i[44]+ i[45]+ i[46]+ i[47]+ i[48]+ i[49]+ i[50]
								+ i[51]+ i[52]+ i[53]+ i[54]+ i[55]+ i[56]+ i[57]+ i[58]+ i[59]+ i[60]
								+ i[61]+ i[62]+ i[63]+ i[64]+ i[65]+ i[66]+ i[67]+ i[68]+ i[69]+ i[70]
								+ i[71]+ i[72]+ i[73]+ i[74]+ i[75]+ i[76]+ i[77]+ i[78]+ i[79]+ i[80]
								+ i[81]+ i[82]+ i[83]+ i[84]+ i[85]+ i[86]+ i[87]+ i[88]+ i[89]+ i[90]
								+ i[91]+ i[92]+ i[93]+ i[94]+ i[95]+ i[96]+ i[97]+ i[98] )
				maximo = max(i[1], i[2], i[3], i[4], suma_hijos_mas10, suma_hijos_mas5)
				if maximo == 0 or maximo == '0' :
					json_hijos.append({'redcode': i[0], 'hijos': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_hijos.append({'redcode': i[0], 'hijos': '1', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_hijos.append({'redcode': i[0], 'hijos': '2', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_hijos.append({'redcode': i[0], 'hijos': '3', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_hijos.append({'redcode': i[0], 'hijos': '4', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_hijos.append({'redcode': i[0], 'hijos': '5', 'cantidad':maximo})
									else:
										if maximo == suma_hijos_mas5 :
											json_hijos.append({'redcode': i[0], 'hijos': '5mas', 'cantidad':maximo})
										else:
											if maximo == suma_hijos_mas10 :
												json_hijos.append({'redcode': i[0], 'hijos': '10mas', 'cantidad':maximo})

									
			return JsonResponse(json_hijos, safe=False)

		elif 'nuevoMapa_edades' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'edquinq_1','edquinq_2', 'edquinq_3', 'edquinq_4','edquinq_5',
			'edquinq_6','edquinq_7', 'edquinq_8', 'edquinq_9','edquinq_10',
			'edquinq_11','edquinq_12', 'edquinq_13', 'edquinq_14','edquinq_15',
			'edquinq_16', 'edquinq_17').order_by('id')
			values_list = list(persona_vald.values('redcode', 
			'edquinq_1','edquinq_2', 'edquinq_3', 'edquinq_4','edquinq_5',
			'edquinq_6','edquinq_7', 'edquinq_8', 'edquinq_9','edquinq_10',
			'edquinq_11','edquinq_12', 'edquinq_13', 'edquinq_14','edquinq_15',
			'edquinq_16', 'edquinq_17')) 
			json_edades = []

			for i in persona_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5],i[6],
				 i[7], i[8], i[9], i[10],i[11], i[12], i[13], i[14], i[15],
				 i[16], i[17])
				if maximo == 0 or maximo == '0' :
					json_edades.append({'redcode': i[0], 'quinquena': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_edades.append({'redcode': i[0], 'quinquena': '4', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_edades.append({'redcode': i[0], 'quinquena': '9', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_edades.append({'redcode': i[0], 'quinquena': '14', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_edades.append({'redcode': i[0], 'quinquena': '19', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_edades.append({'redcode': i[0], 'quinquena': '24', 'cantidad':maximo})
									else:
										if maximo == i[6] :
											json_edades.append({'redcode': i[0], 'quinquena': '29', 'cantidad':maximo})
										else:
											if maximo == i[7] :
												json_edades.append({'redcode': i[0], 'quinquena': '34', 'cantidad':maximo})
											else:
												if maximo == i[8] :
													json_edades.append({'redcode': i[0], 'quinquena': '39', 'cantidad':maximo})
												else:
													if maximo == i[9] :
														json_edades.append({'redcode': i[0], 'quinquena': '44', 'cantidad':maximo})
													else:
														if maximo == i[10] :
															json_edades.append({'redcode': i[0], 'quinquena': '49', 'cantidad':maximo})
														else:
															if maximo == i[11] :
																json_edades.append({'redcode': i[0], 'quinquena': '54', 'cantidad':maximo})
															else:
																if maximo == i[12] :
																	json_edades.append({'redcode': i[0], 'quinquena': '59', 'cantidad':maximo})
																else:
																	if maximo == i[13] :
																		json_edades.append({'redcode': i[0], 'quinquena': '64', 'cantidad':maximo})
																	else:
																		if maximo == i[14] :
																			json_edades.append({'redcode': i[0], 'quinquena': '69', 'cantidad':maximo})
																		else:
																			if maximo == i[15] :
																				json_edades.append({'redcode': i[0], 'quinquena': '74', 'cantidad':maximo})
																			else:
																				if maximo == i[16] :
																					json_edades.append({'redcode': i[0], 'quinquena': '79', 'cantidad':maximo})
																				else:
																					if maximo == i[17] :
																						json_edades.append({'redcode': i[0], 'quinquena': '84', 'cantidad':maximo})
			return JsonResponse(json_edades, safe=False)

		elif 'nuevoMapa_slaboral_trabajoIngreso' in request.POST: #si
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_1').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_1'))
			json_slab1 = []
			maximo_slab1 = persona_vald[0][1]
			minimo_slab1 = persona_vald[len(persona_vald)-1][1]
			json_slab1 = {'cantidad' : values_list, 'maxim' : maximo_slab1, 'minim' : minimo_slab1 }

			return JsonResponse(json_slab1, safe=False)

		elif 'nuevoMapa_slaboral_STCE' in request.POST: #si
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_2').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_2'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)

		elif 'nuevoMapa_slaboral_Busca' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_3').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_3'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)
		
		elif 'nuevoMapa_slaboral_Fam' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_4').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_4'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)
		
		elif 'nuevoMapa_slaboral_BuscaPrim' in request.POST: #si
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_5').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_5'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)

		elif 'nuevoMapa_slaboral_hogar' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_6').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_6'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)

		elif 'nuevoMapa_slaboral_Estudia' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_7').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_7'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)
		
		elif 'nuevoMapa_slaboral_Jubilado' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_8').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_8'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)
		
		elif 'nuevoMapa_slaboral_Incapacitado' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','slaboral_9').order_by('-slaboral_1')
			values_list = list(persona_vald.values('redcode','slaboral_9'))
			json_slab = []
			maximo_slab = persona_vald[0][1]
			minimo_slab = persona_vald[len(persona_vald)-1][1]
			json_slab = {'cantidad' : values_list, 'maxim' : maximo_slab, 'minim' : minimo_slab }

			return JsonResponse(json_slab, safe=False)

		elif 'nuevoMapa_analf' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode','lee_2').order_by('-lee_2')
			values_list = list(persona_vald.values('redcode','lee_2'))
			json_analf = [] 

			maximo_analf = persona_vald[0][1]
			minimo_analf = persona_vald[len(persona_vald)-1][1]
			json_analf = {'cantidad' : values_list, 'maxim' : maximo_analf, 'minim' : minimo_analf }

	


			return JsonResponse(json_analf, safe=False)

		elif 'nuevoMapa_genero' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'sexo_1','sexo_2').order_by('id')
			values_list = list(persona_vald.values('redcode','sexo_1','sexo_2'))
			json_gen = []
			for i in persona_vald:
				maximo = max(i[1],i[2])
				if i[1] == i[2] :
					json_gen.append({'redcode': i[0], 'genero': 'iguales', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_gen.append({'redcode': i[0], 'genero': 'Masculino', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_gen.append({'redcode': i[0], 'genero': 'Femenino', 'cantidad':maximo})

			return JsonResponse(json_gen, safe=False)
	

		elif 'nuevoMapa_femenino' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'sexo_2').order_by('-sexo_2')
			values_list = list(persona_vald.values('redcode', 
			'sexo_2'))
			maximo_fem = persona_vald[0][1]

			minimo_fem = persona_vald[len(persona_vald)-1][1]

			values_list = {'cantidad_muj' : values_list, 'max_fem' : maximo_fem, 'min_fem' : minimo_fem }
			
			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_masculino' in request.POST:
			persona_vald = Persona.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'sexo_1').order_by('-sexo_1')
			values_list = list(persona_vald.values('redcode', 
			'sexo_1'))
			maximo_mas = persona_vald[0][1]
			minimo_mas = persona_vald[len(persona_vald)-1][1]

			values_list = {'cantidad_hom' : values_list, 'max_mas' : maximo_mas, 'min_mas' : minimo_mas }
			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_combustion' in request.POST:
			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'combusti_1','combusti_2', 'combusti_3', 'combusti_4',
			'combusti_5','combusti_6', 'combusti_7', 'combusti_8').order_by('id')
			values_list = list(hogar_vald.values('redcode', 
			'combusti_1','combusti_2', 'combusti_3', 'combusti_4',
			'combusti_5','combusti_6', 'combusti_7', 'combusti_8')) 
			json_combustion = []

			for i in hogar_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
				if maximo == 0 or maximo == '0' :
					json_combustion.append({'redcode': i[0], 'tipo': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_combustion.append({'redcode': i[0], 'tipo': 'Natural', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_combustion.append({'redcode': i[0], 'tipo': 'Licuado', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_combustion.append({'redcode': i[0], 'tipo': 'Parafina', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_combustion.append({'redcode': i[0], 'tipo': 'Lena', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_combustion.append({'redcode': i[0], 'tipo': 'Carbon, Aserrin', 'cantidad':maximo})
									else:
										if maximo == i[6] :
											json_combustion.append({'redcode': i[0], 'tipo': 'Electricidad', 'cantidad':maximo})
										else:
											if maximo == i[7] :
												json_combustion.append({'redcode': i[0], 'tipo': 'Energia Solar', 'cantidad':maximo})
											else:
												if maximo == i[8] :
													json_combustion.append({'redcode': i[0], 'tipo': 'No cocina', 'cantidad':maximo})
											
			return JsonResponse(json_combustion, safe=False)

		elif 'nuevoMapa_internet' in request.POST: 
			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode','internet_1').order_by('-internet_1')
			values_list = list(hogar_vald.values('redcode','internet_1'))
			json_internet = []
			porcentaje_list  = []
			for i in hogar_vald:
				hogar = CHogar.objects.get(redcode = i[0])
				cantidad_hogares = float(hogar.cant)
				porcentaje  = float(0)
				if cantidad_hogares != 0 :
					porcentaje = int (float(i[1]) / cantidad_hogares * 100.0)
					porcentaje_list.append({'redcode': i[0], 'porcentaje': porcentaje})
				else:
					porcentaje_list.append({'redcode': i[0], 'porcentaje': 0 })


			maximo_internet = 100
			minimo_internet = 0
			json_internet = {'cantidad' : porcentaje_list, 'maxim' : maximo_internet, 'minim' : minimo_internet }

			return JsonResponse(json_internet, safe=False)

		elif 'nuevoMapa_cable' in request.POST: 
			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode','tvcable_1').order_by('-tvcable_1')
			values_list = list(hogar_vald.values('redcode','tvcable_1'))
			json_cable = []
			porcentaje_list  = []
			for i in hogar_vald:
				hogar = CHogar.objects.get(redcode = i[0])
				cantidad_hogares = hogar.cant
				cantidad_hogares = float(hogar.cant)
				porcentaje  = float(0)
				if cantidad_hogares != 0 :
					porcentaje = int(float(i[1]) / cantidad_hogares *100.0)
					porcentaje_list.append({'redcode': i[0], 'porcentaje': porcentaje})
				else:
					porcentaje_list.append({'redcode': i[0], 'porcentaje': 0 })

			maximo_cable = 100
			minimo_cable = 0
			json_cable = {'cantidad' : porcentaje_list, 'maxim' : maximo_cable, 'minim' : minimo_cable }

			return JsonResponse(json_cable, safe=False)

		elif 'nuevoMapa_computador' in request.POST: 
			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode','pc_1').order_by('-pc_1')
			values_list = list(hogar_vald.values('redcode','pc_1'))
			json_cable = []
			porcentaje_list  = []
			for i in hogar_vald:
				hogar = CHogar.objects.get(redcode = i[0])
				cantidad_hogares = float(hogar.cant)
				porcentaje  = float(0)
				if cantidad_hogares != 0 :
					porcentaje = int(float(i[1]) / cantidad_hogares *100.0)
					porcentaje_list.append({'redcode': i[0], 'porcentaje': porcentaje})
				else:
					porcentaje_list.append({'redcode': i[0], 'porcentaje': 0 })
			maximo_cable = 100
			minimo_cable = 0
			json_cable = {'cantidad' : porcentaje_list, 'maxim' : maximo_cable, 'minim' : minimo_cable }
			return JsonResponse(json_cable, safe=False)

		elif 'nuevoMapa_bicicleta' in request.POST: 
			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode','bicipart_1').order_by('-bicipart_1')
			values_list = list(hogar_vald.values('redcode','bicipart_1'))
			json_cable = []
			porcentaje_list  = []
			for i in hogar_vald:
				hogar = CHogar.objects.get(redcode = i[0])
				cantidad_hogares = float(hogar.cant)
				porcentaje  = float(0)
				if cantidad_hogares != 0 :
					porcentaje = int(float(i[1]) / cantidad_hogares * 100.0)
					porcentaje_list.append({'redcode': i[0], 'porcentaje': porcentaje})
				else:
					porcentaje_list.append({'redcode': i[0], 'porcentaje': 0 })

			maximo_cable = 100
			minimo_cable = 0
			json_cable = {'cantidad' : porcentaje_list, 'maxim' : maximo_cable, 'minim' : minimo_cable }
			return JsonResponse(json_cable, safe=False)

		elif 'nuevoMapa_auto' in request.POST: 
			print ("json_auto[0]")

			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode','autopart_1', 'camipart_1').order_by('id')
			values_list = list(hogar_vald.values('redcode','autopart_1', 'camipart_1'))
			json_auto = []
			porcentaje_list  = []
			hogares_val = CHogar.objects.filter(redcode__startswith ='10501')

			for i in hogar_vald:
				hogar = hogares_val.get(redcode = i[0])
				cantidad_hogares = float(hogar.cant)
				porcentaje  = float(0)

				if cantidad_hogares != 0 :
					if i[0] + i[1] > hogar.cant:
						porcentaje_list.append({'redcode': i[0], 'porcentaje': 100 })
					else:
						porcentaje= int(float(i[1]+ i[2]) / cantidad_hogares *100.0)
						porcentaje_list.append({'redcode': i[0], 'porcentaje': porcentaje})
						print(porcentaje)
				else:
					porcentaje_list.append({'redcode': i[0], 'porcentaje': 0 })

			maximo_auto = 100
			minimo_auto = 0
			json_auto = {'cantidad' : porcentaje_list, 'maxim' : maximo_auto, 'minim' : minimo_auto }
			
			return JsonResponse(json_auto, safe=False)

		elif 'nuevoMapa_moto' in request.POST: 
			hogar_vald = Hogar.objects.filter(redcode__startswith ='10501' ).values_list('redcode','motopart_1').order_by('-motopart_1')
			values_list = list(hogar_vald.values('redcode','motopart_1'))
			json_cable = []
			porcentaje_list  = []
			for i in hogar_vald:
				hogar = CHogar.objects.get(redcode = i[0])
				cantidad_hogares = float(hogar.cant)
				porcentaje  = float(0)
				if cantidad_hogares != 0 :
					porcentaje = int(float(i[1]) / cantidad_hogares *100.0)
					porcentaje_list.append({'redcode': i[0], 'porcentaje': porcentaje})
				else:
					porcentaje_list.append({'redcode': i[0], 'porcentaje': 0 })

			maximo_cable = 100
			minimo_cable = 0
			json_cable = {'cantidad' : porcentaje_list, 'maxim' : maximo_cable, 'minim' : minimo_cable }
			return JsonResponse(json_cable, safe=False)

		elif 'nuevoMapa_tipo' in request.POST:
			print("llega a nuevoMapa_tipo")
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'tipoviv_1','tipoviv_2', 'tipoviv_3', 'tipoviv_4',
			'tipoviv_5','tipoviv_6', 'tipoviv_7', 'tipoviv_8',
			 'tipoviv_9', 'tipoviv_10').order_by('id')
			values_list = list(viv_vald.values('redcode', 
			'tipoviv_1','tipoviv_2', 'tipoviv_3', 'tipoviv_4',
			'tipoviv_5','tipoviv_6', 'tipoviv_7', 'tipoviv_8',
			 'tipoviv_9', 'tipoviv_10')) 
			json_tipo = []

			for i in viv_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
				if maximo == 0 or maximo == '0' :
					json_tipo.append({'redcode': i[0], 'tipo': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_tipo.append({'redcode': i[0], 'tipo': 'Casa', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_tipo.append({'redcode': i[0], 'tipo': 'Departamento en edificio', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_tipo.append({'redcode': i[0], 'tipo': 'Piezas en casa antigua o conventillo', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_tipo.append({'redcode': i[0], 'tipo': 'Mejora, mediagua', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_tipo.append({'redcode': i[0], 'tipo': 'Rancho, choza', 'cantidad':maximo})
									else:
										if maximo == i[6] :
											json_tipo.append({'redcode': i[0], 'tipo': 'Ruca', 'cantidad':maximo})
										else:
											if maximo == i[7] :
												json_tipo.append({'redcode': i[0], 'tipo': 'Movil (carpa, vagon, container, bote, lancha, similar)', 'cantidad':maximo})
											else:
												if maximo == i[8] :
													json_tipo.append({'redcode': i[0], 'tipo': 'Otro tipo de vivienda particular', 'cantidad':maximo})
												else:
													if maximo == i[9] :
														json_tipo.append({'redcode': i[0], 'tipo': 'Vivienda colectiva (Residencial, Hotel, Hospital, etc.)', 'cantidad':maximo})
													else:
														if maximo == i[10] :
															json_tipo.append({'redcode': i[0], 'tipo': 'Viajeros (no es considerado vivienda)', 'cantidad':maximo})
											
			return JsonResponse(json_tipo, safe=False)

		elif 'nuevoMapa_condicion' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'condocup_1','condocup_2', 'condocup_3').order_by('id')
			values_list = list(viv_vald.values('redcode', 
			'condocup_1','condocup_2', 'condocup_3')) 
			json_condicion = []

			for i in viv_vald:
				maximo = max(i[1], i[2], i[3])
				if maximo == 0 or maximo == '0' :
					json_condicion.append({'redcode': i[0], 'tipo': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_condicion.append({'redcode': i[0], 'tipo': 'Ocupada con personas presentes', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_condicion.append({'redcode': i[0], 'tipo': 'Ocupada con personas ausentes', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_condicion.append({'redcode': i[0], 'tipo': 'Desocupada', 'cantidad':maximo})
											
			return JsonResponse(json_condicion, safe=False)

		elif 'nuevoMapa_tenencia' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode', 
			'tenencia_1','tenencia_2', 'tenencia_3', 'tenencia_4',
			'tenencia_5').order_by('id')
			values_list = list(viv_vald.values('redcode', 
			'tenencia_1','tenencia_2', 'tenencia_3', 'tenencia_4',
			'tenencia_5')) 
			json_tenencia = []

			for i in viv_vald:
				maximo = max(i[1], i[2], i[3], i[4], i[5])
				if maximo == 0 or maximo == '0' :
					json_tenencia.append({'redcode': i[0], 'tipo': 'ninguna', 'cantidad':maximo})
				else:
					if maximo == i[1]:
						json_tenencia.append({'redcode': i[0], 'tipo': 'Propia (pagada totalmente)', 'cantidad':maximo})
					else:
						if maximo == i[2]:
							json_tenencia.append({'redcode': i[0], 'tipo': 'Propia (pagando a plazo)', 'cantidad':maximo})
						else:
							if maximo == i[3]:
								json_tenencia.append({'redcode': i[0], 'tipo': 'Arrendada', 'cantidad':maximo})
							else:
								if maximo == i[4]:
									json_tenencia.append({'redcode': i[0], 'tipo': 'Cedida por trabajo o servicio', 'cantidad':maximo})
								else:
									if maximo == i[5] :
										json_tenencia.append({'redcode': i[0], 'tipo': 'Gratuita', 'cantidad':maximo})
								
			return JsonResponse(json_tenencia, safe=False)

		elif 'nuevoMapa_alumbra' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode','alumbra_4').order_by('-alumbra_4')
			values_list = list(viv_vald.values('redcode', 'alumbra_4'))
			maxim = viv_vald[0][1]
			minim = viv_vald[len(viv_vald)-1][1]

			values_list = {'cantidad' : values_list, 'maxim' : maxim, 'minim' : minim }
			return JsonResponse(values_list, safe=False)
		
		elif 'nuevoMapa_caneria' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode','caneria_3').order_by('-caneria_3')
			values_list = list(viv_vald.values('redcode', 'caneria_3'))
			maxim = viv_vald[0][1]
			minim = viv_vald[len(viv_vald)-1][1]

			values_list = {'cantidad' : values_list, 'maxim' : maxim, 'minim' : minim }
			print(values_list)
			print("values_list")

			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_red' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode','agua_1').order_by('-agua_1')
			values_list = list(viv_vald.values('redcode', 'agua_1'))
			maxim = viv_vald[0][1]
			minim = viv_vald[len(viv_vald)-1][1]

			values_list = {'cantidad' : values_list, 'maxim' : maxim, 'minim' : minim }
			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_pozo' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode','agua_2').order_by('-agua_2')
			values_list = list(viv_vald.values('redcode', 'agua_2'))
			maxim = viv_vald[0][1]
			minim = viv_vald[len(viv_vald)-1][1]

			values_list = {'cantidad' : values_list, 'maxim' : maxim, 'minim' : minim }
			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_rio' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode','agua_3').order_by('-agua_3')
			values_list = list(viv_vald.values('redcode', 'agua_3'))
			maxim = viv_vald[0][1]
			minim = viv_vald[len(viv_vald)-1][1]

			values_list = {'cantidad' : values_list, 'maxim' : maxim, 'minim' : minim }
			return JsonResponse(values_list, safe=False)

		elif 'nuevoMapa_alcantarillado' in request.POST:
			viv_vald = Vivienda.objects.filter(redcode__startswith ='10501' ).values_list('redcode','wc_6').order_by('-wc_6')
			values_list = list(viv_vald.values('redcode', 'wc_6'))
			maxim = viv_vald[0][1]
			minim = viv_vald[len(viv_vald)-1][1]

			values_list = {'cantidad' : values_list, 'maxim' : maxim, 'minim' : minim }
			return JsonResponse(values_list, safe=False)


		elif 'redcode' in request.POST:
			redcode_manz= request.POST['redcode'] 
			sigue = 1
			try:
				hogar = CHogar.objects.get(redcode = redcode_manz)
				cantidad_hogares = hogar.cant
				resp =  'REDCODE Manzana: ' + redcode_manz + '</br>'
				resp += 'Cantidad de hogares: ' + str(cantidad_hogares) 
			except:
				sigue = 0
				resp = 'No tiene Hogares'
			try:
				personas = CPersona.objects.get(redcode = redcode_manz)
				cantidad_personas = personas.cant
				resp = resp + '</br> Cantidad de habitantes: ' + str(cantidad_personas)
				resp = resp + '</br> Cantidad de habitantes por hogar: ' + str(float(cantidad_personas/cantidad_hogares))
			except:
				sigue = 0
				resp = resp + '</br> Cantidad de habitantes: '+ 'No tiene habitantes'
			if sigue == 1:
				persona = Persona.objects.get(redcode = redcode_manz)
				personas_sin_disc = persona.resdiscap_0
				personas_con_disc = cantidad_personas - int(personas_sin_disc)

				resp = resp + '</br> Cantidad de Mujeres: '+ str(persona.sexo_2) 
				resp = resp + '</br> Cantidad de Hombres: '+ str(persona.sexo_1 )
				resp = resp + '</br> Cantidad de Analfabetos: '+ str(persona.lee_2 ) + '</br>'

				resp = resp + '</br> <b> Cultura </b>' 

				resp = resp + '</br> Cantidad de Alacalufe: '+ str(persona.cultura_1 )
				resp = resp + '</br> Cantidad de Atacameno: '+ str(persona.cultura_2 )
				resp = resp + '</br> Cantidad de Aimara: '+ str(persona.cultura_3 )
				resp = resp + '</br> Cantidad de Colla: '+ str(persona.cultura_4 )
				resp = resp + '</br> Cantidad de Mapuche: '+ str(persona.cultura_5 )
				resp = resp + '</br> Cantidad de Quechua: '+ str(persona.cultura_6 )
				resp = resp + '</br> Cantidad de Rapa Nui: '+ str(persona.cultura_7 )
				resp = resp + '</br> Cantidad de Yamana: '+ str(persona.cultura_8 ) + '</br>'


				resp = resp + '</br> <b> Educacion </b>' 

				resp = resp + '</br> Nunca asistio: '+ str(persona.tipoer_1 )
				resp = resp + '</br> Pre-Basica: '+ str(persona.tipoer_2 )
				resp = resp + '</br> Especial/Diferencial: '+ str(persona.tipoer_3 )
				resp = resp + '</br> Basica/Primaria: '+ str(persona.tipoer_4 )
				resp = resp + '</br> Media Comun: '+ str(persona.tipoer_5 )
				resp = resp + '</br> Humanidades: '+ str(persona.tipoer_6 )
				resp = resp + '</br> Media Comercial: '+ str(persona.tipoer_7 )
				resp = resp + '</br> Media Industrial: '+ str(persona.tipoer_8 )
				resp = resp + '</br> Media Agricola: '+ str(persona.tipoer_9 )
				resp = resp + '</br> Media Maritima: '+ str(persona.tipoer_10 )
				resp = resp + '</br> Normal: '+ str(persona.tipoer_11 )
				resp = resp + '</br> Tecnica Femenina: '+ str(persona.tipoer_12 )
				resp = resp + '</br> Centro de Formacion Tecnica: '+ str(persona.tipoer_13 )
				resp = resp + '</br> Instituto Profesional: '+ str(persona.tipoer_14 )
				resp = resp + '</br> Universitaria: '+ str(persona.tipoer_15 )+ '</br>'


				resp = resp + '</br> <b> Discapacidad </b></br>' 
				#resp = resp + '</br> Cantidad de Personas sin discapacidad: '+ str(personas_sin_disc)
				resp = resp + '</br> Cantidad de Personas con discapacidad: '+ str(personas_con_disc) 
				resp = resp + '</br> Cantidad de Personas con ceguera: '+ str(persona.resdiscap_1)
				resp = resp + '</br> Cantidad de Personas con sordera: '+ str(persona.resdiscap_2) 
				resp = resp + '</br> Cantidad de Personas con mudez: '+ str(persona.resdiscap_3) 
				resp = resp + '</br> Cantidad de Personas lisiadas/paralisadas: '+ str(persona.resdiscap_4) 
				resp = resp + '</br> Cantidad de Personas con deficiencia mental: '+ str(persona.resdiscap_5) 
				resp = resp + '</br> Cantidad de Personas con dos discapacidades: '+ str(persona.resdiscap_6) 
				resp = resp + '</br> Cantidad de Personas con tres discapacidades: '+ str(persona.resdiscap_7) 
				resp = resp + '</br> Cantidad de Personas con cuatro discapacidades: '+ str(persona.resdiscap_8) 
				resp = resp + '</br> Cantidad de Personas con cinco discapacidades: '+ str(persona.resdiscap_9) + '</br>'
			else:
				print("no hay personas")
			return HttpResponse(resp)

	persona_vald = Persona.objects.filter(redcode__startswith ='10501').values_list('redcode', 
		'resdiscap_0','resdiscap_1','resdiscap_2', 'resdiscap_3','resdiscap_4','resdiscap_5',
		'resdiscap_6', 'resdiscap_7', 'resdiscap_8', 'resdiscap_9', 'sexo_1', 'sexo_2' ).order_by('id')
	
	cpersonas_query = CPersona.objects.filter(redcode__startswith ='10501').values_list('redcode', 'cant').order_by('-cant')
	maxima_cant = cpersonas_query[0][1]
	minima_cant = cpersonas_query[len(cpersonas_query)-1][1]

	total_mujeres = 0
	total_hombres = 0 
	for persona in persona_vald:
		total_mujeres = total_mujeres + int(persona[12])
		total_hombres = total_hombres + int(persona[11])

	context = {'personas': persona_vald, 'total_h': total_hombres, 'total_m' : total_mujeres,
		'personas_cant': cpersonas_query, 'max_cant': maxima_cant, 'min_cant': minima_cant}
	return render(request, 'index.html', context)

def contenido_indicadores(redcode_manz, valor_criterio):

	resp = "";
	if valor_criterio == "ninguno":
		resp = "Seleccione un indicador primero.. "
		tipo = 'torta'
		data = [{"nombre_label": "hombres", "valor": 5},
		 {"nombre_label": "mujeres", "valor": 15},
		 {"nombre_label": "otro", "valor": 2}]
		 
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif (valor_criterio == "normal" or valor_criterio ==  "densidad"):
		if Persona.objects.filter(redcode = redcode_manz).exists():

			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = '<b> Cantidad de habitantes: </b> ' + str(cantidad_personas)
		else: 
			resp = ( "No Existen habitantes")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data, }
		return resp

	elif valor_criterio == "genero":
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = '<b> Genero </b>'

			resp += ( "Existen " + str(persona_vald.sexo_1) + " Hombres y " + str(persona_vald.sexo_2)
				+ " Mujeres ") 
			if persona_vald.sexo_1 == persona_vald.sexo_2:
				resp = resp + " "
			else: 
				maximo = max(persona_vald.sexo_1, persona_vald.sexo_2)
				if maximo == persona_vald.sexo_1:
					resp = resp + "Mayoria de: Hombres"
				else:
					resp = resp + "Mayoria de: Mujeres"
		else: 
			resp = ( "No Existen habitantes")
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "femenino":
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = '<b> Mujeres </b>'
			resp += ( "Existen " + str(persona_vald.sexo_2) + " Mujeres ")
		else: 
			resp = ( "No Existen Mujeres")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "masculino":
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(persona_vald.sexo_1) + " Hombres")
		else: 
			resp = ( "No Existen Hombres")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
				
	elif valor_criterio == "analfabetismo":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( "<b>Analfabetismo:</b> </br>Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Analfabetismo:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.lee_2) + " Analfabetos </br>") 
			resp = ( resp + str(persona_vald.lee_1) + " No Analfabetos ")
		else:
			resp = "No existe informacion"
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "cultura":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( " <b>Cultura:</b> </br> Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Cultura:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.cultura_1) + " Alacalufe </br>") 
			resp = ( resp + str(persona_vald.cultura_2) + " Atacameno </br>")
			resp = ( resp + str(persona_vald.cultura_3) + " Aimara </br>")
			resp = ( resp + str(persona_vald.cultura_4) + " Colla </br>")
			resp = ( resp + str(persona_vald.cultura_5) + " Mapuche </br>")
			resp = ( resp + str(persona_vald.cultura_6) + " Quechua </br>")
			resp = ( resp + str(persona_vald.cultura_7) + " Rapa Nui </br>")
			resp = ( resp + str(persona_vald.cultura_8) + " Yamana </br>")
			resp = ( resp + str(persona_vald.cultura_9) + " Sin pertenencia a pueblos originarios o indigenas ")
		else:
			resp = "No existe informacion"


		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "religion":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( " <b>Religion:</b> </br> Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Religion:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.religion_1) + " Catolica </br>") 
			resp = ( resp + str(persona_vald.religion_2) + " Evangelica </br>")
			resp = ( resp + str(persona_vald.religion_3) + " Testigo de Jehova </br>")
			resp = ( resp + str(persona_vald.religion_4) + " Judaica </br>")
			resp = ( resp + str(persona_vald.religion_5) + " Mormon </br>")
			resp = ( resp + str(persona_vald.religion_6) + " Musulmana </br>")
			resp = ( resp + str(persona_vald.religion_7) + " Ortodoxa </br>")
			resp = ( resp + str(persona_vald.religion_8) + " Otra religion o credo </br>")
			resp = ( resp + str(persona_vald.religion_9) + " No profesa religion, es agnostico, o ateo ")
		else:
			resp = "No existe informacion"
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp											
			
	elif valor_criterio == "educacion":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( " <b>Educacion:</b> </br> Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Educacion:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.tipoer_1) + " Nunca Asistio </br>") 
			resp = ( resp + str(persona_vald.tipoer_2) + " Pre-Basica </br>")
			resp = ( resp + str(persona_vald.tipoer_3) + " Especial/Deliferencial </br>")
			resp = ( resp + str(persona_vald.tipoer_4) + " Basica/Primaria </br>")
			resp = ( resp + str(persona_vald.tipoer_5) + " Media Comun </br>")
			resp = ( resp + str(persona_vald.tipoer_6) + " Humanidades </br>")
			resp = ( resp + str(persona_vald.tipoer_7) + " Media Comercial </br>")
			resp = ( resp + str(persona_vald.tipoer_8) + " Media Industrial </br>")
			resp = ( resp + str(persona_vald.tipoer_9) + " Media Agricola </br>")
			resp = ( resp + str(persona_vald.tipoer_10) + " Media Maritima </br>")
			resp = ( resp + str(persona_vald.tipoer_11) + " Normal  </br>")
			resp = ( resp + str(persona_vald.tipoer_12) + " Tecnica Femenina </br>")
			resp = ( resp + str(persona_vald.tipoer_13) + " Centro de Formacion Tecnica </br>") 
			resp = ( resp + str(persona_vald.tipoer_14) + " Instituto Profesional </br>") 
			resp = ( resp + str(persona_vald.tipoer_15) + " Universitaria </br>") 
		else:
			resp = "No existe informacion"
		maximo = max(persona_vald.tipoer_1, persona_vald.tipoer_2, persona_vald.tipoer_3,
		 persona_vald.tipoer_4, persona_vald.tipoer_5 + persona_vald.tipoer_6 + persona_vald.tipoer_7 
		 + persona_vald.tipoer_8 + persona_vald.tipoer_9 + persona_vald.tipoer_10 + persona_vald.tipoer_11,
			persona_vald.tipoer_12 + persona_vald.tipoer_13, persona_vald.tipoer_14, persona_vald.tipoer_15)
		resp = ( resp + str(maximo) + " Maximo ")
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "empleabilidad":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( " <b>Empleabilidad:</b> </br> Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Empleabilidad:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.trabaja_1) + " trabajadores asalariados </br>") 
			resp = ( resp + str(persona_vald.trabaja_2) + " trabajadores de servicio domestico </br>")
			resp = ( resp + str(persona_vald.trabaja_3) + " trabajadores por cuenta propia </br>")
			resp = ( resp + str(persona_vald.trabaja_4) + " Empleadores, empresarios o patrones </br>")
			resp = ( resp + str(persona_vald.trabaja_5) + " Familiares no remunerados </br>")
			maximo = max(persona_vald.trabaja_1, persona_vald.trabaja_2, persona_vald.trabaja_3,
			 persona_vald.trabaja_4, persona_vald.trabaja_5 )
			resp = ( resp + str(maximo) + " Maximo ")
		else:
			resp = "No existe informacion"
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
			
	elif valor_criterio == "disc":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( " <b>Discapacitados:</b> </br> Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Discapacitados:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.discapac_0) + " Posee Alguna Discapacidad </br>") 
			resp = ( resp + str(persona_vald.discapac_1) + " No posee discapacidad ")
		else:
			resp = "No existe informacion"
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
		
	elif valor_criterio == "disc_tipos":
		if CPersona.objects.filter(redcode = redcode_manz).exists():
			personas = CPersona.objects.get(redcode = redcode_manz)
			cantidad_personas = personas.cant
			resp = ( " <b>Discapacitados:</b> </br> Existen " + str(cantidad_personas) + " Personas </br>")
		else:
			resp = "<b>Discapacitados:</b> </br>"
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.resdiscap_1) + " Personas con ceguera</br>") 
			resp = ( resp + str(persona_vald.resdiscap_2) + " Personas con sordera</br>") 
			resp = ( resp + str(persona_vald.resdiscap_3) + " Personas con mudez</br>") 
			resp = ( resp + str(persona_vald.resdiscap_4) + " Personas con Paralisis o lisiadas</br>") 
			resp = ( resp + str(persona_vald.resdiscap_5) + " Personas con deficiencia mental</br>") 
			resp = ( resp + str(persona_vald.resdiscap_6) + " Personas con dos discapacidades</br>") 
			resp = ( resp + str(persona_vald.resdiscap_7) + " Personas con tres discapacidades</br>") 
			resp = ( resp + str(persona_vald.resdiscap_8) + " Personas con cuatro discapacidades</br>") 
			resp = ( resp + str(persona_vald.resdiscap_9) + " Personas con cinco discapacidades") 
		else:
			resp = "No existe informacion"

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "trab_ingreso":
		if Persona.objects.filter(redcode = redcode_manz).exists():
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.slaboral_1) + " Personas trabajando con ingreso")
		else:
			resp = (resp + "No existe informacion")
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "sin_trabajo_con_ingreso":
		if Persona.objects.filter(redcode = redcode_manz).exists():		
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.slaboral_2) + " Personas sin trabajo, pero con empleo") 
		else:
			resp = (resp + "No existe informacion")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "trab_prim":

		persona_vald = Persona.objects.get(redcode = redcode_manz)
		resp = ( resp + str(persona_vald.slaboral_5) + " Personas que buscan trabajo por primera vez") 

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp


	elif valor_criterio == "trab_hogar":
		if Persona.objects.filter(redcode = redcode_manz).exists():		

			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.slaboral_6) + " Personas con trabajando en quehaceres de su hogar")
		else:
			resp = (resp + "No existe informacion") 
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "trab_estudia":
		if Persona.objects.filter(redcode = redcode_manz).exists():		
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.slaboral_7) + " Estudiantes") 
		else:
			resp = (resp + "No existe informacion") 		
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "trab_jubilado":
		if Persona.objects.filter(redcode = redcode_manz).exists():		
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.slaboral_8) + " Personas Jubiladas") 
		else:
			resp = (resp + "No existe informacion") 
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "trab_incapacitado":
		if Persona.objects.filter(redcode = redcode_manz).exists():		
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.slaboral_9) + " Personas Incapacitadas permanentes para trabajar") 
		else:
			resp = (resp + "No existe informacion") 
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
		
	elif valor_criterio == "hijos":
		if Persona.objects.filter(redcode = redcode_manz).exists():	
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			
			suma_hijos_mas5 = ( int(persona_vald.hijos_6) + int(persona_vald.hijos_7) + int(persona_vald.hijos_8) + int(persona_vald.hijos_9) + int(persona_vald.hijos_10) )

			suma_hijos_mas10 = int( persona_vald.hijos_11 + persona_vald.hijos_12 + persona_vald.hijos_13 + persona_vald.hijos_14 + persona_vald.hijos_15
								+ persona_vald.hijos_16 + persona_vald.hijos_17 + persona_vald.hijos_18 + persona_vald.hijos_19 + persona_vald.hijos_20
								+ persona_vald.hijos_21 + persona_vald.hijos_22 + persona_vald.hijos_23 + persona_vald.hijos_24 + persona_vald.hijos_25
								+ persona_vald.hijos_26 + persona_vald.hijos_27 + persona_vald.hijos_28 + persona_vald.hijos_29 + persona_vald.hijos_30
								+ persona_vald.hijos_31 + persona_vald.hijos_32 + persona_vald.hijos_33 + persona_vald.hijos_34 + persona_vald.hijos_35
								+ persona_vald.hijos_36 + persona_vald.hijos_37 + persona_vald.hijos_38 + persona_vald.hijos_39 + persona_vald.hijos_40
								+ persona_vald.hijos_41 + persona_vald.hijos_42 + persona_vald.hijos_43 + persona_vald.hijos_44 + persona_vald.hijos_45
								+ persona_vald.hijos_46 + persona_vald.hijos_47 + persona_vald.hijos_48 + persona_vald.hijos_49 + persona_vald.hijos_50
								+ persona_vald.hijos_51 + persona_vald.hijos_52 + persona_vald.hijos_53 + persona_vald.hijos_54 + persona_vald.hijos_55
								+ persona_vald.hijos_56 + persona_vald.hijos_57 + persona_vald.hijos_58 + persona_vald.hijos_59 + persona_vald.hijos_60	
								+ persona_vald.hijos_61 + persona_vald.hijos_62 + persona_vald.hijos_63 + persona_vald.hijos_64 + persona_vald.hijos_65
								+ persona_vald.hijos_66 + persona_vald.hijos_67 + persona_vald.hijos_68 + persona_vald.hijos_69 + persona_vald.hijos_70
								+ persona_vald.hijos_71 + persona_vald.hijos_72 + persona_vald.hijos_73 + persona_vald.hijos_74 + persona_vald.hijos_75
								+ persona_vald.hijos_76 + persona_vald.hijos_77 + persona_vald.hijos_78 + persona_vald.hijos_79 + persona_vald.hijos_80
								+ persona_vald.hijos_81 + persona_vald.hijos_82 + persona_vald.hijos_83 + persona_vald.hijos_84 + persona_vald.hijos_85
								+ persona_vald.hijos_86 + persona_vald.hijos_87 + persona_vald.hijos_88 + persona_vald.hijos_89 + persona_vald.hijos_90
								+ persona_vald.hijos_91 + persona_vald.hijos_92 + persona_vald.hijos_93 + persona_vald.hijos_94 + persona_vald.hijos_95
								+ persona_vald.hijos_96 + persona_vald.hijos_97 + persona_vald.hijos_98 )

			resp = ( resp + str(persona_vald.hijos_0) + " Personas sin hijos</br>") 
			resp = ( resp + str(persona_vald.hijos_1) + " Personas con un hijo</br>") 
			resp = ( resp + str(persona_vald.hijos_2) + " Personas con dos hijos</br>") 
			resp = ( resp + str(persona_vald.hijos_3) + " Personas con tres hijos</br>") 
			resp = ( resp + str(persona_vald.hijos_4) + " Personas con cuatro hijos</br>") 
			resp = ( resp + str(persona_vald.hijos_5) + " Personas con cinco hijos</br>") 
			resp = ( resp + str(suma_hijos_mas5) + " Personas que tienen entre 6 y 10 hijos </br>") 
			resp = ( resp + str(suma_hijos_mas10) + " Personas que tienen mas de 10 hijos ") 
		else:
			resp = "No existe informacion"

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "edad":
		if Persona.objects.filter(redcode = redcode_manz).exists():	
			persona_vald = Persona.objects.get(redcode = redcode_manz)
			resp = ( resp + str(persona_vald.edquinq_1) + " Personas que tienen entre 0-4 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_2) + " Personas que tienen entre 5-9 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_3) + " Personas que tienen entre 10-14 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_4) + " Personas que tienen entre 15-19 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_5) + " Personas que tienen entre 20-24 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_6) + " Personas que tienen entre 25-29 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_7) + " Personas que tienen entre 30-34 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_8) + " Personas que tienen entre 35-39 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_9) + " Personas que tienen entre 40-44 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_10) + " Personas que tienen entre 45-49 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_11) + " Personas que tienen entre 50-54 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_12) + " Personas que tienen entre 55-59 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_13) + " Personas que tienen entre 60-64 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_14) + " Personas que tienen entre 65-69 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_15) + " Personas que tienen entre 70-74 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_16) + " Personas que tienen entre 75-79 agnos </br>") 
			resp = ( resp + str(persona_vald.edquinq_17) + " Personas que tienen 80 y mas agnos ") 

		else:
			resp = "No existe informacion"

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
																	
	elif valor_criterio == "combustion":
		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( resp + str(hogar_vald.combusti_1) + " Hogares con combustion por Gas Natural </br>")
			resp = ( resp + str(hogar_vald.combusti_2) + " Hogares con combustion por Gas Licuado </br>") 
			resp = ( resp + str(hogar_vald.combusti_3) + " Hogares con combustion por Parafina </br>") 
			resp = ( resp + str(hogar_vald.combusti_4) + " Hogares con combustion por Lena </br>") 
			resp = ( resp + str(hogar_vald.combusti_5) + " Hogares con combustion por Carbon, Aserrin </br>") 
			resp = ( resp + str(hogar_vald.combusti_6) + " Hogares con combustion por Electricidad </br>") 
			resp = ( resp + str(hogar_vald.combusti_7) + " Hogares con combustion por Energia Solar </br>") 
			resp = ( resp + str(hogar_vald.combusti_8) + " Hogares que no cocinan ") 
		else:
			resp = "No existe informacion"


		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "internet":
		hogares_existen = True
		if (CHogar.objects.filter(redcode = redcode_manz).exists()):
			hogares = CHogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")
		else:
			resp = "No existen hogares"
			hogares_existen = False

		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( resp + str(hogar_vald.internet_1) + " Hogares con internet")
		else:
			if hogares_existen :
				resp = ( resp + "No existe informacion de internet en la manzana")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "cable":
		if (CHogar.objects.filter(redcode = redcode_manz).exists()):
			hogares = CHogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana")
			
		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( resp + str(hogar_vald.tvcable_1) + " Hogares con tv cable")
		else:
			if hogares_existen :
				resp = ( resp + "No existe informacion de tv cable en la manzana")
		
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "computador":
		if (CHogar.objects.filter(redcode = redcode_manz).exists()):
			hogares = CHogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")

		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")
			resp = ( resp + str(hogar_vald.pc_1) + " Hogares con computador")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "bicicleta":
		if (CHogar.objects.filter(redcode = redcode_manz).exists()):
			print ("en Chogar")
			hogares = CHogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")
		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")
			resp = ( resp + str(hogar_vald.bicipart_1) + " Hogares con bicicleta")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "auto":
		if (CHogar.objects.filter(redcode = redcode_manz).exists()):

			hogares = CHogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")

		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")
			resp = ( resp + str(hogar_vald.autopart_1 + hogar_vald.camipart_1) + " Hogares con vehiculo particular (automovil o camioneta)")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "moto":
		if (CHogar.objects.filter(redcode = redcode_manz).exists()):

			hogares = CHogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")

		if (Hogar.objects.filter(redcode = redcode_manz).exists()):
			hogar_vald = Hogar.objects.get(redcode = redcode_manz)
			resp = ( "Existen " + str(hogares.cant) + " Hogares en la manzana</br>")
			resp = ( resp + str(hogar_vald.motopart_1) + " Hogares con moto")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "tipo":				
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.tipoviv_1) + " Casas</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_2) + " Departamentos en Edificio</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_3) + " Piezas en casa antigua o conventillo</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_4) + " Mejoras, mediaguas</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_5) + " Ranchos, chozas</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_6) + " Rucas</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_7) + " Viviendas Moviles (carpa, vagon, container, bote, lancha, similar)</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_8) + " Otro tipo de vivienda particular</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_9) + " Vivienda colectiva (Residencial, Hotel, Hospital, etc.)</br>")
			resp = ( resp + str(vivienda_vald.tipoviv_10) + " Sin vivienda (viajeros)")


		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "condicion":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):

			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.condocup_1) + " Viviendas ocupadas con personas presentes</br>")
			resp = ( resp + str(vivienda_vald.condocup_2) + " Viviendas ocupadas con personas ausentes</br>")
			resp = ( resp + str(vivienda_vald.condocup_3) + " Viviendas desocupadas")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
																										
	elif valor_criterio == "tenencia":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
			
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.tenencia_1) + " Viviendas propias (pagadas totalmente)</br>")
			resp = ( resp + str(vivienda_vald.tenencia_2) + " Viviendas propias (pagando a plazo)</br>")
			resp = ( resp + str(vivienda_vald.tenencia_3) + " Viviendas arrendadas </br>")
			resp = ( resp + str(vivienda_vald.tenencia_4) + " Viviendas cedidas por trabajo o servicio</br>")
			resp = ( resp + str(vivienda_vald.tenencia_5) + " Viviendas gratuitas")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "alumbra":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
		
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.alumbra_4) + " Viviendas sin servicio de alumbrado</br>")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "caneria":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
		
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.caneria_3) + " Viviendas sin servivio de agua por caneria")


		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "agua_red":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
		
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.agua_1) + " Viviendas con origen del agua en la Red Publica")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "agua_pozo":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
		
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.agua_2) + " Viviendas con origen del agua en un pozo o noria")

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "agua_rio":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
		
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.agua_3) + " Viviendas con origen del agua en un rio, vertiente o estero")
		else:
			resp = "Indicador sin informacion"

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	elif valor_criterio == "carencia_alcantarillado":
		if (Vivienda.objects.filter(redcode = redcode_manz).exists()):
		
			vivienda_vald = Vivienda.objects.get(redcode = redcode_manz)
			resp = ( resp + str(vivienda_vald.wc_6) + " Viviendas sin disponibilidad de servicio higienico (W.C.)")
		else:
			resp = "Indicador sin informacion"

		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp

	else:
		resp = "Indicador sin informacion"
		tipo = "ninguno"
		data = []
		resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }
		return resp
	#resp = {'respuesta': resp, 'tipo_graf':tipo, 'datos': data }




#def mapa_region:
#	if r
#	return coord