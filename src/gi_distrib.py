from scipy.stats import randint,binom,norm,geom,uniform
import logging
def distrib(param1,param2,param3,param4,egg):
	#param1 : element
	#param2 : config de la propriete
	#param3 : nom de la propriete
	#param4 : snapshot id
	
	############################ qualitatif 
	
	value_pr=egg[param1][param3][param4-1] # value of the previous element, needed for offset
	if param2['domain']['type']=="qualitatif":
		###################################### qualitatif sans ordre	
		if param2['domain']['order']=="false":

			if value_pr in param2['evolution']['succesors']:
				random =  randint.rvs(0, len(param2['evolution']['succesors'][value_pr]), size=1)
				egg[param1][param3].update({param4:param2['evolution']['succesors'][value_pr][random[0]]})
			else:
				random =  randint.rvs(0, len(param2['domain']['values']), size=1)
				egg[param1][param3].update({param4:param2['domain']['values'][random[0]]})
		


		###################################qualitatif avec ordre
		else:
			indice=param2['domain']['values'].index(value_pr)
			offset_list=list()
			for m in range(0,param2['evolution']['offset']['max']-param2['evolution']['offset']['min']+1):
				### m ne va pas jusqu au bout
				offset_list.append(param2['evolution']['offset']['min'] + m)

			if param2['evolution']['offset']['distribution']['type']=="uniform":
				random =  randint.rvs(0, len(offset_list), size=1)
				
				if len(param2['domain']['values'])-1<indice+offset_list[random[0]]:########## enter here only when indice+offset_list[random[0]] is bigger than the biggest index
					egg[param1][param3].update({param4:param2['domain']['values'][len(param2['domain']['values'])-1]})##### we take the last value
				elif indice+offset_list[random[0]]<0:
					egg[param1][param3].update({param4:param2['domain']['values'][0]}) ######### we take the first value
				else:
					egg[param1][param3].update({param4:param2['domain']['values'][indice+offset_list[random[0]]]})	
	
			if param2['evolution']['offset']['distribution']['type']=="binom":
				random =  binom.rvs(len(offset_list)-1,param2['evolution']['offset']['distribution']["p"] , size=1)
				#logging.info( param3+param1+str(param4)+str(indice)+str(offset_list)+str(random[0]))
				if len(param2['domain']['values'])-1<indice+offset_list[random[0]]:########## enter here only when indice+offset_list[random[0]] is bigger than the biggest index
					egg[param1][param3].update({param4:param2['domain']['values'][len(param2['domain']['values'])-1]}) ##### we take the last value
				elif indice+offset_list[random[0]]<0:
					egg[param1][param3].update({param4:param2['domain']['values'][0]}) ######### we take the first value
				else:
					egg[param1][param3].update({param4:param2['domain']['values'][indice+offset_list[random[0]]]})



	############################ qualitatif

	############################ quantitatif:dis

	if param2['domain']['type']=="quantitatif:dis":
		offset_list=list()
		for m in range(0,param2['evolution']['offset']['max']-param2['evolution']['offset']['min']+1):
			### jai ajoute 1 car il yavait un bug que je ne comprenais pas , m n allait pas jusqu au plus grand nombre
			offset_list.append(param2['evolution']['offset']['min'] + m)
		if param2['evolution']['offset']['distribution']["type"]=="binom":
			random =  binom.rvs(len(offset_list)-1,param2['evolution']['offset']['distribution']["p"] , size=1)
			### j ajoute -1 pour que random soit entre 0 et le plus grand indice de offset list qui est sa taille -1
			previous_value=value_pr
			next_value=previous_value+offset_list[random[0]]
			if next_value < param2["domain"]["values"]["min"]:
				egg[param1][param3].update({param4:param2["domain"]["values"]["min"]})
			elif next_value >param2["domain"]["values"]["max"]: 
				egg[param1][param3].update({param4:param2["domain"]["values"]["max"]})
			else:
				egg[param1][param3].update({param4:next_value})




	############################ quantitatif:dis

	############################ quantitatif:con

	if param2['domain']['type']=="quantitatif:con":
		if param2['evolution']['offset']['distribution']["type"]=="normal":
			random = norm.rvs(size=1)
			previous_value=value_pr
			next_value=round(previous_value+((random[0]*param2['evolution']['offset']['distribution']['sigma'])+param2['evolution']['offset']['distribution']['mean']),1)
			if next_value < param2["domain"]["values"]["min"]:
				egg[param1][param3].update({param4:param2["domain"]["values"]["min"]})
			elif next_value >param2["domain"]["values"]["max"]: 
				egg[param1][param3].update({param4:param2["domain"]["values"]["max"]})
			else:
				egg[param1][param3].update({param4:next_value})
	############################ quantitatif:con

	return egg