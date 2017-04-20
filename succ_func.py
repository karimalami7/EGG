import gi_distrib 



def succ_func(elementId,elementConfig,configG,prop,i,egg):

	for rulee in configG['ListDynP'][prop]['rulese']:
		if "change" in rulee['if']:
			if egg[elementId][rulee['if']['prop']][i-1]==rulee['if']['change'][0] and egg[elementId][rulee['if']['prop']][i]==rulee['if']['change'][1]:
				### une regle change est satisfaite ici
				print "une regle change est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,elementId,"va influencer",prop
				print rulee['then']
				elementConfig=then_func(rulee['then'],elementConfig)
		if "sens" in rulee['if']:
			if rulee['if']['sens']=='up' :
				### une regle sens est satisfaite ici
				if (configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and egg[elementId][rulee['if']['prop']][i-1]<egg[elementId][rulee['if']['prop']][i]:
					print "une regle sens up est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,elementId,"va influencer",prop
					print rulee['then']
					elementConfig=then_func(rulee['then'],elementConfig)
				if configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and configG['ListDynP'][rule['if']['prop']]['domain']['values'].index(egg[elementId][rule['if']['prop']][i-1]) < configG['ListDynP'][rule['of']['prop']]['domain']['values'].index(egg[elementId][rule['if']['prop']][i]):
					print "une regle sens up est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,elementId,"va influencer",prop
					print rulee['then']
					elementConfig=then_func(rulee['then'],elementConfig)
			if rulee['if']['sens']=='down':
				### une regle sens est satisfaite ici
				if (configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:dis" or configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="quantitatif:con") and egg[elementId][rulee['if']['prop']][i-1]>egg[elementId][rulee['if']['prop']][i]:
					print "une regle sens down est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,elementId,"va influencer",prop
					print rulee['then']
					elementConfig=then_func(rulee['then'],elementConfig)
				if configG['ListDynP'][rulee['if']['prop']]['domain']['type']=="qualitatif" and configG['ListDynP'][rule['if']['prop']]['domain']['values'].index(egg[elementId][rule['if']['prop']][i-1]) > configG['ListDynP'][rule['of']['prop']]['domain']['values'].index(egg[elementId][rule['if']['prop']][i]):
					print "une regle sens down est satisfaite ici pour la prop",rulee['if']['prop'],i-1,i,elementId,"va influencer",prop
					print rulee['then']
					elementConfig=then_func(rulee['then'],elementConfig)


	egg=gi_distrib.distrib(elementId,elementConfig,prop,i,egg)
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