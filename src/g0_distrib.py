#######################################
#
#	Project: EGG 
#
#	File: g0_distrib.py
#
#
#	Description: Assign values for the initial snapshots 


from scipy.stats import randint,binom,norm,geom,uniform
import logging
############### distrib function begin

def distrib(param1,param2,param3,param4,egg):
	#param1 : liste d'elements du graph
	#param2 : config de la propriete
	#param3 : nom de la propriete
	#param4 : snapshot id

	############################	
	# qualitatif :begin
	############################
	if param2['domain']['type']=="qualitatif":
		#############################
		#  uniform	: begin
		#############################
		if param2['domain']['distribution']['type']=="uniform":
			random =  randint.rvs(0, len(param2['domain']['values']), size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:[param2['domain']['values'][random[i]]]})
				i=i+1
		############################# 
		# uniform :end 
		#############################


		############################# 
		# binom	:begin
		#############################

		if param2['domain']['distribution']['type']=="binom":
			random =  binom.rvs(len(param2['domain']['values']), param2['domain']['distribution']['p'] , size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:[param2['domain']['values'][random[i]-1]]})
				i=i+1		
		############################# 
		# binom: end
		#############################

		#############################  
		# geom : begin
		#############################
		if param2['domain']['distribution']['type']=="geom":
			
			geomValues=list()
			for i in range (0,len(param1)):
				while True:
					value=geom.rvs(param2['domain']['distribution']['p'],size=1)[0]
					if  value > len(param2['domain']['values']):
						pass
					else :
						geomValues.append(value)
						break
			i=0
			for element in param1:
				egg[element].update({param3:[param2['domain']['values'][geomValues[i]-1]]})
				i=i+1

		#############################
		#  geom: end
		#############################

	############################ 
	#qualitatif :end  
	############################





	############################
	# quantitatif:dis : begin
	############################
	if param2['domain']['type']=="quantitatif:dis":
		
		#############################  
		# binom: begin
		#############################
		
		if param2['domain']['distribution']['type']=="binom":
			random = binom.rvs(param2['domain']['values']['max']-param2['domain']['values']['min'],param2['domain']['distribution']['p'],size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:[random[i]]})
				i=i+1
		#############################  
		# binom: end
		#############################
	############################
	# quantitatif:dis : end
	############################







	############################
	# quantitatif:con : begin
	############################
	if param2['domain']['type']=="quantitatif:con":
		#############################  
		# normal: begin
		#############################
		if param2['domain']['distribution']['type']=="normal":
			random = norm.rvs(size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:[round(((random[i]*param2['domain']['distribution']['sigma'])+param2['domain']['distribution']['mean']),1)]})
				i=i+1
		#############################  
		# normal: end
		#############################

		#############################  
		# uniform: begin
		#############################
		if param2['domain']['distribution']['type']=="uniform":
			random = uniform.rvs(size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:[round(((param2['domain']['values']['max']-param2['domain']['values']['min'])*random[i])+param2['domain']['values']['min'],1)]})
				i=i+1
		#############################  
		# uniform: end
		#############################
	############################
	# quantitatif:con : end
	############################
	


	return egg
############################
# distrib function: end
############################





#######################
#validity distribution
#######################

def validity(param1,param2,param3,param4,egg):


	#param1 : liste d'elements du graph
	#param2 : config de la propriete
	#param3 : nom de la propriete
	#param4 : snapshot id
	
	

	if len(param2["init"]) == 1: # if the validity can take only one value

		for value in param2["init"]:

			for element in param1:
				
				egg[element].update({"v":[value]})


			
	else :

		random_for_all = list(uniform.rvs(size=(len(param1))))

		for element in param1:

			random = random_for_all.pop()

			if random < param2["init"]["T"]:

				egg[element].update({"v":["T"]})

			else :

				egg[element].update({"v":["F"]})


