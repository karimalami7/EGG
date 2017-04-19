from scipy.stats import randint,binom,norm,geom,uniform
import json_parser
import plain_text_parser
import g0_distrib 
import gi_distrib 

(egg,graph_elements)=plain_text_parser.graph_parser()

#################evaluate config file json and put it in dict

obj=json_parser.eval_config()

#################property dependance dep_graph
L=json_parser.sorted_list(obj)
#################kahns algorithm : end






######################################  constitute T0 debut

for prop in L:
	if obj['ListDynP'][prop]['domain']['v'] == 'true': #### si la prop a un domaine bien defini.
	#######call distrib function   with 
	#######  graph_elements[obj['ListDynP'][prop]['elements_type']]
	#######	 obj['ListDynP'][prop]
	#######  update egg

		egg=g0_distrib.distrib(graph_elements[obj['ListDynP'][prop]['elements_type']],obj['ListDynP'][prop],prop,0,egg)

	else:
	#######call distrib function for each rule
		for rule in obj['ListDynP'][prop]['rules']:
			elements_with_rule=list()
			for elements in egg:
				if rule['if']['prop'] in egg[elements]: # si la prop if est presente pour ces elements 
					if egg[elements][rule['if']['prop']][0] in rule['if']['hasValues']: # l element a une valeur presente dans les regles
						elements_with_rule.append(elements)
			config_modif=dict(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
			config_modif["domain"].update(rule["then"]["config"]["domain"])
			egg=g0_distrib.distrib(elements_with_rule,config_modif,prop,0,egg)
			###### call distrib with
			###### elements_with_rule
			###### obj['ListDynP'][prop]
			###### update egg 


#######################################  constitute T0 end

####################################### constitute all snapshots

for i in range(1,obj['interval']):
	for prop in L:
		
		#############prop qui ont evolution bien definie

		if obj['ListDynP'][prop]['evolution']['e'] == 'true': ### si la propriete a un domaine d evolution bien defini
			for element in graph_elements[obj['ListDynP'][prop]['elements_type']]:
				if obj['ListDynP'][prop]['duration']//i==0 and obj['ListDynP'][prop]['evolution']['staticity']<uniform.rvs(): ###check if it has to change now
					if obj['ListDynP'][prop]['evolution']['relation']=="true":
						#### succession function
						for rulee in obj['ListDynP'][prop]['rulese']:
							if "change" in rulee['if']:
								if egg[element][rulee['if']['prop']][i-1]==rulee['if']['change'][0] and egg[element][rulee['if']['prop']][i]==rulee['if']['change'][1]:
									### une regle change est satisfaite ici
									print "une regle change est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
							if "sens" in rulee['if']:
								if rulee['if']['sens']=='up' :
									### une regle sens est satisfaite ici
									if (obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and egg[element][rulee['if']['prop']][i-1]<egg[element][rulee['if']['prop']][i]:
										print "une regle sens up est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
									if obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and obj['ListDynP'][rule['if']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i-1]) < obj['ListDynP'][rule['of']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i]):
										print "une regle sens up est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
								if rulee['if']['sens']=='down':
									### une regle sens est satisfaite ici
									if (obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and egg[element][rulee['if']['prop']][i-1]>egg[element][rulee['if']['prop']][i]:
										print "une regle sens down est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
									if obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and obj['ListDynP'][rule['if']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i-1]) > obj['ListDynP'][rule['of']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i]):
										print "une regle sens down est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
						egg=gi_distrib.distrib(element,obj['ListDynP'][prop],prop,i,egg)
					else:
						pass#### general random generator
				else:
					if i-1 in egg[element][prop]:
						egg[element][prop].update({i:egg[element][prop][i-1]})
		


		#############prop qui ont evolution non definie

		else:
			for rule in obj['ListDynP'][prop]['rules']:
				elements_with_rule=list()
				for elements in egg:
					if rule['if']['prop'] in egg[elements]: # si la prop if est presente pour ces elements 
						if egg[elements][rule['if']['prop']][i] in rule['if']['hasValues']: # l element a une valeur presente dans les regles
							elements_with_rule.append(elements)
				config_modif=dict(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
				config_modif["evolution"].update(rule["then"]["config"]["evolution"])

				#### constitution de elements with rule and config modif

				for element in elements_with_rule:
					if obj['ListDynP'][prop]['duration']//i==0 and obj['ListDynP'][prop]['evolution']['staticity']<uniform.rvs(): ###check if it has to change now
						if obj['ListDynP'][prop]['evolution']['relation']=="true":
							#### succession function
							for rulee in obj['ListDynP'][prop]['rulese']:
								if "change" in rulee['if']:
									if egg[element][rulee['if']['prop']][i-1]==rulee['if']['change'][0] and egg[element][rulee['if']['prop']][i]==rulee['if']['change'][1]:
										### une regle change est satisfaite ici
										print "une regle change est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
								if "sens" in rulee['if']:
									if rulee['if']['sens']=='up' :
										### une regle sens est satisfaite ici
										if (obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and egg[element][rulee['if']['prop']][i-1]<egg[element][rulee['if']['prop']][i]:
											print "une regle sens up est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
										if obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and obj['ListDynP'][rule['if']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i-1]) < obj['ListDynP'][rule['of']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i]):
											print "une regle sens up est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
									if rulee['if']['sens']=='down':
										### une regle sens est satisfaite ici
										if (obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and egg[element][rulee['if']['prop']][i-1]>egg[element][rulee['if']['prop']][i]:
											print "une regle sens down est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
										if obj['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and obj['ListDynP'][rule['if']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i-1]) > obj['ListDynP'][rule['of']['prop']]['domain']['values'].index(egg[element][rule['if']['prop']][i]):
											print "une regle sens down est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,element,"va influencer",prop
							egg=gi_distrib.distrib(element,config_modif,prop,i,egg)
						else:
							pass
					else:
						if i-1 in egg[element][prop]:
							egg[element][prop].update({i:egg[element][prop][i-1]})

#######################################

for e in egg:
	if not egg[e] == {} :
		print e,egg[e],"\n\n\n"




