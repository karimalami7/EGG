#######################################
#
#	Project: EGG 
#
#	File: succ_func.py
#
#
#	Description: Modify the configuration for properties that have rules of evolution.



import gi_distrib 
import gi_distrib_new
import logging
import copy

logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

def succ_func(element_list,elementConfig,configG,prop,i,egg):

	element_in_egg_pr=dict()
	element_in_egg_nw=dict()

	config_list = list()
	elements_by_rulee = list()

	for rulee in configG['ListDynP'][prop]['rulese']:

		config_list.append(copy.deepcopy(elementConfig))

		config_list[len(config_list)-1]=then_func(rulee['then'],config_list[len(config_list)-1])

		elements_by_rulee.append(list())

	elements_no_rule=list()
	

	for elementId in element_list:
		

		boolean_elements=False
		rulee_index=0
		for rulee in configG['ListDynP'][prop]['rulese']:


			element_in_egg_nw[rulee['if']['prop']]=egg[elementId][rulee['if']['prop']][i]
			element_in_egg_pr[rulee['if']['prop']]=egg[elementId][rulee['if']['prop']][i-1]



			if "change" in rulee['if']:
				if element_in_egg_pr[rulee['if']['prop']]==rulee['if']['change'][0] and element_in_egg_nw[rulee['if']['prop']]==rulee['if']['change'][1]:
					### une regle change est satisfaite ici
					#logging.info ("une regle change est satisfaite ici pour la prop"+rulee['if']['prop']+str(i-1)+str(i)+elementId+"va influencer"+prop)
					#logging.info (rulee['then'])
					elementConfig=then_func(dict(rulee['then']),dict(elementConfig))
					elements_by_rulee[rulee_index].append(elementId)
					boolean_elements=True
			if "sens" in rulee['if']:
				if rulee['if']['sens']=='up' :
					### une regle sens est satisfaite ici
					if (configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and element_in_egg_pr[rulee['if']['prop']]<element_in_egg_nw[rulee['if']['prop']]:
						#logging.info ("une regle sens up est satisfaite ici pour la prop"+rulee['if']['prop']+str(i-1)+str(i)+elementId+"va influencer"+prop)
						#logging.info (rulee['then'])
					
						elementConfig=then_func(dict(rulee['then']),dict(elementConfig))
						elements_by_rulee[rulee_index].append(elementId)
						boolean_elements=True
					if configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and configG['ListDynP'][rule['if']['prop']]['domain']['values'].index(element_in_egg_pr[rule['if']['prop']]) < configG['ListDynP'][rule['of']['prop']]['domain']['values'].index(element_in_egg_nw[rule['if']['prop']]):
						#logging.info ("une regle sens up est satisfaite ici pour la prop"+rulee['if']['prop']+str(i-1)+str(i)+elementId+"va influencer"+prop)
						#logging.info (rulee['then'])
						elementConfig=then_func(dict(rulee['then']),dict(elementConfig))
						elements_by_rulee[rulee_index].append(elementId)
						boolean_elements=True
				if rulee['if']['sens']=='down':
					### une regle sens est satisfaite ici
					if (configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and element_in_egg_pr[rulee['if']['prop']]>element_in_egg_nw[rulee['if']['prop']]:
						#logging.info ("une regle sens down est satisfaite ici pour la prop"+rulee['if']['prop']+str(i-1)+str(i)+elementId+"va influencer"+prop)
						#logging.info (rulee['then'])
					
						elementConfig=then_func(dict(rulee['then']),dict(elementConfig))
						elements_by_rulee[rulee_index].append(elementId)
						boolean_elements=True
					if configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and configG['ListDynP'][rule['if']['prop']]['domain']['values'].index(element_in_egg_pr[rule['if']['prop']]) > configG['ListDynP'][rule['of']['prop']]['domain']['values'].index(element_in_egg[rule['if']['prop']][i]):
						#logging.info ("une regle sens down est satisfaite ici pour la prop"+rulee['if']['prop']+str(i-1)+str(i)+elementId+"va influencer"+prop)
						#logging.info (rulee['then'])
						elementConfig=then_func(dict(rulee['then']),dict(elementConfig))
						elements_by_rulee[rulee_index].append(elementId)
						boolean_elements=True

			rulee_index=rulee_index+1

		if boolean_elements == False: 
			elements_no_rule.append(elementId)


	egg=gi_distrib_new.distrib(elements_no_rule,elementConfig,prop,i,egg)#### run for those that doesnt suit any rule

	rulee_index=0

	for rulee in configG['ListDynP'][prop]['rulese']:

		egg=gi_distrib_new.distrib(elements_by_rulee[rulee_index],config_list[rulee_index],prop,i,egg)

		rulee_index=rulee_index+1
	


	#egg=gi_distrib.distrib(elementId,elementConfig,prop,i,egg)
	return egg

def then_func(param1,param2):
	#param1 rulee[then]
	#param2 elementconfig 
	if "change" in param1:
		pass
	if "sens" in param1:
		if param1['sens']=='down':
			param2['evolution']['offset']['max']=0
		if param1['sens']=='up':
			param2['evolution']['offset']['min']=0


	return param2