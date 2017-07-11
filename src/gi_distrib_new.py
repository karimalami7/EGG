#######################################
#
#	Project: EGG 
#
#	File: gi_distrib_new.py
#
#
#	Description: Define offsets and changes between snapshot i and snapshot i+1



from scipy.stats import randint,binom,norm,geom,uniform
import logging

def distrib(param1,param2,param3,param4,egg):
	#param1 : list_element
	#param2 : config de la propriete
	#param3 : nom de la propriete
	#param4 : snapshot id
	#egg which is egg




	############################	
	# qualitatif :begin
	############################

	if param2['domain']['type']=="qualitatif":
		

		############################	
		# qualitatif sans ordre:begin
		############################	
		

		if param2['domain']['order']=="false":

			no_succ_elements=list()
			succ_elements=list()

			for  succ_key in param2["evolution"]["succesors"]:
				
				succ_elements.append(list())

			######################### division de l'ensemble des elements en plusieurs ensembles selon la regle de succession
				
			for param1_element in param1:

				succ_index=0
				bool_succ=False

				for succ_key in param2["evolution"]["succesors"]:

					value_pr=egg[param1_element][param3][param4-1]

					if succ_key == value_pr :

						succ_elements[succ_index].append(param1_element)

						bool_succ=True

					succ_index=succ_index+1		

				if bool_succ == False:

					no_succ_elements.append(param1_element)

			######################### end

			#########################  affectation des valeurs a no succ elements

			random =  list(randint.rvs(0, len(param2['domain']['values']), size=len(no_succ_elements)))

			for elementId in no_succ_elements:

				egg[elementId][param3].insert(param4,param2['domain']['values'][random.pop()])

			######################### end

			######################### affectation des valeurs aux elements de succ_elements

			succ_index =0

			for  succ_key in param2["evolution"]["succesors"]:

				succ_list=succ_elements[succ_index]

				random =  list(randint.rvs(0, len(param2['evolution']['succesors'][succ_key]), size=len(succ_list)))

				for elementId in succ_list:

					egg[elementId][param3].insert(param4,param2['evolution']['succesors'][succ_key][random.pop()])

				succ_index=succ_index+1

			######################### end

		############################	
		# qualitatif sans ordre:fin
		############################



		############################	
		# qualitatif avec ordre:begin
		############################
		
		else:


			offset_list=list()
			for m in range(0,param2['evolution']['offset']['max']-param2['evolution']['offset']['min']+1):
				### m ne va pas jusqu au bout
				offset_list.append(param2['evolution']['offset']['min'] + m)

			############################	
			# uniform:begin
			############################
	
			if param2['evolution']['offset']['distribution']['type']=="uniform":

				random =  randint.rvs(0, len(offset_list), size=len(param1))
				i=0
				for param1_element in param1 :

					value_pr=egg[param1_element][param3][param4-1] # value of the previous element, needed for offset
					indice=param2['domain']['values'].index(value_pr)

					if len(param2['domain']['values'])-1<indice+offset_list[random[i]]:########## enter here only when indice+offset_list[random[0]] is bigger than the biggest index
						egg[param1_element][param3].insert(param4,param2['domain']['values'][len(param2['domain']['values'])-1])##### we take the last value
					elif indice+offset_list[random[i]]<0:
						egg[param1_element][param3].insert(param4,param2['domain']['values'][0]) ######### we take the first value
					else:
						egg[param1_element][param3].insert(param4,param2['domain']['values'][indice+offset_list[random[i]]])	
					i=i+1
			############################	
			# uniform:end
			############################


			############################	
			# binom:begin
			############################
			if param2['evolution']['offset']['distribution']['type']=="binom":
				random =  binom.rvs(len(offset_list)-1,param2['evolution']['offset']['distribution']["p"] , size=len(param1))

				i=0
				for param1_element in param1 :

					value_pr=egg[param1_element][param3][param4-1] # value of the previous element, needed for offset
					indice=param2['domain']['values'].index(value_pr)


					#logging.info( param3+param1+str(param4)+str(indice)+str(offset_list)+str(random[0]))
					if len(param2['domain']['values'])-1<indice+offset_list[random[i]]:########## enter here only when indice+offset_list[random[0]] is bigger than the biggest index
						egg[param1_element][param3].insert(param4,param2['domain']['values'][len(param2['domain']['values'])-1]) ##### we take the last value
					elif indice+offset_list[random[i]]<0:
						egg[param1_element][param3].insert(param4,param2['domain']['values'][0]) ######### we take the first value
					else:
						egg[param1_element][param3].insert(param4,param2['domain']['values'][indice+offset_list[random[i]]])
					i=i+1

			############################	
			# binom:end
			############################

		############################	
		# qualitatif avec ordre:end
		############################



	############################	
	# qualitatif :end
	############################






















	############################	
	# quantitatif:dis :begin
	############################

	if param2['domain']['type']=="quantitatif:dis":
		

		offset_list=list()
		for m in range(0,param2['evolution']['offset']['max']-param2['evolution']['offset']['min']+1):
			### jai ajoute 1 car il yavait un bug que je ne comprenais pas , m n allait pas jusqu au plus grand nombre
			offset_list.append(param2['evolution']['offset']['min'] + m)

		random =  binom.rvs(len(offset_list)-1,param2['evolution']['offset']['distribution']["p"] , size=len(param1))

		i=0
		for param1_element in param1 :

			value_pr=egg[param1_element][param3][param4-1] # value of the previous element, needed for offset
				
			### j ajoute -1 pour que random soit entre 0 et le plus grand indice de offset list qui est sa taille -1
			
			previous_value=value_pr
			next_value=previous_value+offset_list[random[i]]
			if next_value < param2["domain"]["values"]["min"]:
				egg[param1_element][param3].insert(param4,param2["domain"]["values"]["min"])
			elif next_value >param2["domain"]["values"]["max"]: 
				egg[param1_element][param3].insert(param4,param2["domain"]["values"]["max"])
			else:
				egg[param1_element][param3].insert(param4,next_value)

			i=i+1



	############################	
	# quantitatif:dis :end
	############################








	############################	
	# quantitatif:con : begin
	############################

	if param2['domain']['type']=="quantitatif:con":
		
		random = norm.rvs(size=len(param1))

		i=0
		for param1_element in param1 :

			value_pr=egg[param1_element][param3][param4-1] # value of the previous element, needed for offset

			
			previous_value=value_pr
			offset = (random[i]*param2['evolution']['offset']['distribution']['sigma'])+param2['evolution']['offset']['distribution']['mean']
			if offset > param2['evolution']['offset']['max']:
				offset = param2['evolution']['offset']['max']
			elif offset < param2['evolution']['offset']['min']:
				offset = param2['evolution']['offset']['min']

			next_value=round(previous_value+offset,1)
			
			if next_value < param2["domain"]["values"]["min"]:
				egg[param1_element][param3].insert(param4,param2["domain"]["values"]["min"])
			elif next_value >param2["domain"]["values"]["max"]: 
				egg[param1_element][param3].insert(param4,param2["domain"]["values"]["max"])
			else:
				egg[param1_element][param3].insert(param4,next_value)

			i=i+1
	############################	
	# quantitatif:con : end
	############################

	return egg




	###############################	
	# Validity succession function
	###############################


def validity(param1,param2,param3,param4,egg):
	#param1 : list_element
	#param2 : config de la propriete
	#param3 : nom de la propriete
	#param4 : snapshot id
	#egg which is egg

	random_for_all = list(uniform.rvs(size=(len(param1))))

	for element in param1:

		if "max" in param2:

			value = param2["max"].keys()[0]

			if egg[element]["v"].count(value) >= param2["max"][value]:

				if value == "T":

					egg[element]["v"].insert(param4,"F")

				else:

					egg[element]["v"].insert(param4,"T")

				continue

		valid_pr = egg[element]["v"][param4-1]

		if len (param2["succ"][valid_pr]) == 1:

			egg[element]["v"].insert(param4,param2["succ"][valid_pr]) 

		else :

			random = random_for_all.pop()

			if random < param2["succ"][valid_pr]["T"]:

				egg[element]["v"].insert(param4,"T")

			else :

				egg[element]["v"].insert(param4,"F")

















































