from scipy.stats import randint,binom,norm,geom
import logging
############### distrib function debut

def distrib(param1,param2,param3,param4,egg):
	#param1 : liste d'elements du graph
	#param2 : config de la propriete
	#param3 : nom de la propriete
	#param4 : snapshot id

	############################ qualitatif 
	if param2['domain']['type']=="qualitatif":
		#############################  uniform	
		if param2['domain']['distribution']['type']=="uniform":
			random =  randint.rvs(0, len(param2['domain']['values']), size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:{param4:param2['domain']['values'][random[i]]}})
				i=i+1
		#############################  uniform	

		#############################  binom	
		if param2['domain']['distribution']['type']=="binom":
			random =  binom.rvs(len(param2['domain']['values']), param2['domain']['distribution']['p'] , size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:{param4:param2['domain']['values'][random[i]-1]}})
				i=i+1		
		#############################  binom

		#############################  geom
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
				egg[element].update({param3:{param4:param2['domain']['values'][geomValues[i]-1]}})
				i=i+1

		#############################  geom

	############################ qualitatif 
	
	############################ quantitatif:dis
	if param2['domain']['type']=="quantitatif:dis":
		#############################  binom
		if param2['domain']['distribution']['type']=="binom":
			random = binom.rvs(param2['domain']['values']['max']-param2['domain']['values']['min'],param2['domain']['distribution']['p'],size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:{param4:random[i]}})
				i=i+1
		#############################  binom
	############################ quantitatif:dis 

	############################ quantitatif:con
	if param2['domain']['type']=="quantitatif:con":
		############################# normal
		if param2['domain']['distribution']['type']=="normal":
			random = norm.rvs(size=len(param1))
			i=0
			for element in param1:
				egg[element].update({param3:{param4:round(((random[i]*param2['domain']['distribution']['sigma'])+param2['domain']['distribution']['mean']),1)}})
				i=i+1
		############################# normal
	############################ quantitatif:con
	return egg
############### distrib function fin