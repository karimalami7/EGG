from scipy.stats import randint,binom,norm,geom,uniform
import json_parser
import plain_text_parser
import g0_distrib 
import gi_distrib 
import rdfcreator
import succ_func
import copy
import argparse
import logging
import plot1
import plot2
#import plot3
#import plot4

################# put log in egg.log

logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

################# check the arguments

parser = argparse.ArgumentParser(description='define the input schema.')

parser.add_argument('schema', metavar='schema', type=str, nargs=1,
                   help='the schema to process')

parser.add_argument('--plot-byproperty', metavar='property', type=str, nargs='?', const="all",
                   help='plot all graph element that have this property')

parser.add_argument('--plot-byobject', metavar='object', type=str, nargs='?', const="all",
                   help='plot all properties of an elements')

parser.add_argument('--rdf-output', action='store_true',
                   help='outout egg in rdf')

parser.add_argument('--log', action='store_true',
                   help='outout egg in rdf')

args = parser.parse_args()

if args.log == False :
	logging.disable(logging.INFO)

logging.info (args)

#################parse the gmark output

(egg,graph_elements)=plain_text_parser.graph_parser(args.schema[0])

#################evaluate config file json and put it in dict

obj=json_parser.eval_config(args.schema[0])

#################property dependance dep_graph
L=json_parser.sorted_list(obj)







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
			config_modif=copy.deepcopy(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
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
				if i%obj['ListDynP'][prop]['duration']==0 and obj['ListDynP'][prop]['evolution']['staticity']<uniform.rvs(): ###check if it has to change now
					if obj['ListDynP'][prop]['evolution']['relation']=="true":
						#### succession function
						
						egg=succ_func.succ_func(element,copy.deepcopy(obj['ListDynP'][prop]),obj,prop,i,egg)
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
				config_modif=copy.deepcopy(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
				config_modif["domain"].update(rule["then"]["config"]["domain"])
				config_modif["evolution"].update(rule["then"]["config"]["evolution"])


				#### constitution de elements with rule and config modif

				for element in elements_with_rule:
					if i%obj['ListDynP'][prop]['duration']==0 and obj['ListDynP'][prop]['evolution']['staticity']<uniform.rvs(): ###check if it has to change now
						if obj['ListDynP'][prop]['evolution']['relation']=="true":
							#### succession function
							egg=succ_func.succ_func(element,copy.deepcopy(config_modif),obj,prop,i,egg)
						else:
							pass
					else:
						if i-1 in egg[element][prop]:
							egg[element][prop].update({i:egg[element][prop][i-1]})

####################################### fin egg


for e in egg:
	if not egg[e] == {} :
		logging.info (e+str(egg[e])+"\n\n\n")

if args.rdf_output == True:

	rdfcreator.write_rdf(args.schema[0],graph_elements,egg,obj)


########################   plot1 by property : debut

if args.plot_byproperty=="all": 

	for prop in obj["ListDynP"]:

		elements_list=graph_elements[obj["ListDynP"][prop]["elements_type"]]

		plot1.plot(egg,list(elements_list),prop,obj)

elif not args.plot_byproperty==None:

	elements_list=graph_elements[obj["ListDynP"][args.plot_byproperty]["elements_type"]]

	plot1.plot(egg,list(elements_list),args.plot_byproperty,obj)

########################   plot1 : fin

########################   plot2 : debut


if args.plot_byobject=="all" : 

	for element in egg:
		if len(egg[element])>0:
			
			plot2.plot_one(egg[element],element,obj["interval"],obj["ListDynP"])

elif not args.plot_byobject==None:

	plot2.plot_one(egg[args.plot_byobject],args.plot_byobject,obj["interval"],obj["ListDynP"])

########################   plot2 : fin
