#######################################
#
#	EGG 
#
#	main.py
#
#
#
#

##################################
# Packages
##################################

from scipy.stats import randint,binom,norm,geom,uniform
import json_parser
import plain_text_parser
import g0_distrib 
import gi_distrib 
import gi_distrib_new
import succ_func
import copy
import argparse
import logging
import plot1
import plot2
import psutil
import os


################### 
#put log in egg.log
###################
logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')


logging.info ("Let EGG begin")


############################
#check the arguments : Begin 
############################

parser = argparse.ArgumentParser(description='define the input schema.')

parser.add_argument('schema', metavar='schema', type=str, nargs=1,
                   help='the schema to process')

parser.add_argument('--plot-byproperty', metavar='property', type=str, nargs='?', const="all",
                   help='plot all graph element that have this property')

parser.add_argument('--plot-byobject', metavar='object', type=str, nargs='?', const="all",
                   help='plot all properties of an elements')

parser.add_argument('--rdf-output', action='store_true',
                   help='outout egg in rdf')

parser.add_argument('--vg-output', action='store_true',
                   help='outout egg in vg')

parser.add_argument('--log', action='store_true',
                   help='outout egg in rdf')

args = parser.parse_args()

if args.log == False :
	logging.disable(logging.INFO)

###########################
#check the arguments : End
###########################


#######################
#Parse the gmark output
#######################

(egg,graph_elements)=plain_text_parser.graph_parser(args.schema[0])

logging.info ("gmark output parse")

#############################################
#evaluate config file json and put it in dict
#############################################

obj=json_parser.eval_config(args.schema[0])

##############################
#property dependance dep_graph
##############################

L=json_parser.sorted_list(obj)

logging.info ("config parse")







######################################
# T0 : Begin
######################################


######################### 
#T0 validity : Begin 
#########################

for node_label in obj["nodes"]:

	
	g0_distrib.validity(graph_elements[node_label],obj['validity'][node_label],node_label,0,egg)


for edge_label in obj["edges"]:

	changing_element=list()    
    
	for edge_element in graph_elements[edge_label] :

		out_element = egg[edge_element]["out"]

		in_element = egg[edge_element]["in"]

		if egg[out_element]["v"][0] == "T" and egg[in_element]["v"][0] == "T":

			changing_element.append(edge_element)

		else :

			egg[edge_element].update({"v":["F"]})

	g0_distrib.validity(changing_element,obj['validity'][edge_label],edge_label,0,egg)


#########################
#T0 validity : End
#########################


#########################
#T0 for properties : Begin
#########################


for prop in L:

	if obj['ListDynP'][prop]['domain']['v'] == 'true': #### si la prop a un domaine bien defini.

		g0_distrib.distrib(graph_elements[obj['ListDynP'][prop]['elements_type']],obj['ListDynP'][prop],prop,0,egg)

	else:	####### call distrib function for each rule
		
		for rule in obj['ListDynP'][prop]['rules']:
		
			elements_with_rule=list()
		
			for elements in egg:
		
				if rule['if']['prop'] in egg[elements]: # si la prop if est presente pour ces elements 
		
					if egg[elements][rule['if']['prop']][0] in rule['if']['hasValues']: # l element a une valeur presente dans les regles
		
						elements_with_rule.append(elements)
		
			config_modif=copy.deepcopy(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
		
			config_modif["domain"].update(rule["then"]["config"]["domain"])
		
			egg=g0_distrib.distrib(elements_with_rule,config_modif,prop,0,egg)
		
	logging.info (prop+ "end")

logging.info ("T0 end")

#########################
#T0 for properties : End
#########################

#########################
#T0 : End
#########################



#######################################
# Ti : Begin
#######################################
i=1

for k in range(1,obj['interval']):


	################################# 
	#Ti validity : Begin 
	################################# 

	for node_label in obj["nodes"]:

		gi_distrib_new.validity(graph_elements[node_label],obj['validity'][node_label],node_label,i,egg)


	for edge_label in obj["edges"]:

		changing_element=list()

		for edge_element in graph_elements[edge_label] :

			out_element = egg[edge_element]["out"]

			in_element = egg[edge_element]["in"]

			if egg[out_element]["v"][i] == "T" and egg[in_element]["v"][i] == "T":

				changing_element.append(edge_element)

			else :

				egg[edge_element]["v"].insert(i, "F")

		gi_distrib_new.validity(changing_element,obj['validity'][edge_label],edge_label,i,egg)





	################################# 
	# Ti validity : end
	#################################


	#################################
	# Ti for Dyn Properties : Begin
	#################################


	##############################  generate random numbers for all elements

	size_of_graph=0

	for prop in L:

		size_of_graph=size_of_graph+len(graph_elements[obj['ListDynP'][prop]['elements_type']])

	random_for_all = list(uniform.rvs(size=(size_of_graph)))
	


	############################## loop on properties

	for prop in L:
		
		if obj['ListDynP'][prop]['rulese']: #### properties that have dependence to other prop #############prop qui ont evolution bien definie
		
			if obj['ListDynP'][prop]['evolution']['e'] == 'true': ### si la propriete a un domaine d evolution bien defini
	
				changing_element=list()
		
				for element in graph_elements[obj['ListDynP'][prop]['elements_type']]:
		
					if i%obj['ListDynP'][prop]['duration']==0 and egg[element]["v"][i] == "T" and obj['ListDynP'][prop]['evolution']['staticity']<random_for_all.pop(): ###check if it has to change now
		
						if obj['ListDynP'][prop]['evolution']['relation']=="true":
							
							changing_element.append(element)
							
						else:
				
							pass    #### general random generator
			
					else:
				
						if i-1 in egg[element][prop]:
				
							egg[element][prop].update({i:egg[element][prop][i-1]})
			
				if changing_element:
			
					egg=succ_func.succ_func(changing_element,copy.deepcopy(obj['ListDynP'][prop]),obj,prop,i,egg)

			

			else:			#############prop qui ont evolution non definie
				
				for rule in obj['ListDynP'][prop]['rules']:
					
					elements_with_rule=list()
				
					for elements in egg:
				
						if rule['if']['prop'] in egg[elements]: # si la prop if est presente pour ces elements 
				
							if egg[elements][rule['if']['prop']][i] in rule['if']['hasValues']: # l element a une valeur presente dans les regles
				
								elements_with_rule.append(elements)
				
					config_modif=copy.deepcopy(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
				
					config_modif["domain"].update(rule["then"]["config"]["domain"])
				
					config_modif["evolution"].update(rule["then"]["config"]["evolution"])

					changing_element=list()
					
					for element in elements_with_rule: #### constitution de elements with rule and config modif
						
						if i%obj['ListDynP'][prop]['duration']==0 and egg[element]["v"][i] == "T" and obj['ListDynP'][prop]['evolution']['staticity']<random_for_all.pop(): ###check if it has to change now
						
							if obj['ListDynP'][prop]['evolution']['relation']=="true":

								changing_element.append(element)	
							
							else:
							
								pass
						
						else:
					
							if i-1 in egg[element][prop]:
				
								egg[element][prop].update({i:egg[element][prop][i-1]})
				
					if changing_element:
				
						egg=succ_func.succ_func(changing_element,copy.deepcopy(config_modif),obj,prop,i,egg)
		


		else:   #### properties that does not have dependence to other prop

			changing_element = list()

			if obj['ListDynP'][prop]['evolution']['e'] == 'true': ### si la propriete a un domaine d evolution bien defini
			
				for element in graph_elements[obj['ListDynP'][prop]['elements_type']]:
			
					if i%obj['ListDynP'][prop]['duration']==0 and egg[element]["v"][i] == "T" and obj['ListDynP'][prop]['evolution']['staticity']<random_for_all.pop(): ###check if it has to change now
			
						if obj['ListDynP'][prop]['evolution']['relation']=="true":
			
							changing_element.append(element)

						else:
			
							pass#### general random generator
			
					else:
			
						if i-1 in egg[element][prop]:
			
							egg[element][prop].update({i:egg[element][prop][i-1]})
			
				egg=gi_distrib_new.distrib(changing_element,copy.deepcopy(obj['ListDynP'][prop]),prop,i,egg)

		

			else:   #############prop qui ont evolution non definie
				
				for rule in obj['ListDynP'][prop]['rules']:
				
					elements_with_rule=list()
				
					for elements in egg:
				
						if rule['if']['prop'] in egg[elements]: # si la prop if est presente pour ces elements 
				
							if egg[elements][rule['if']['prop']][i] in rule['if']['hasValues']: # l element a une valeur presente dans les regles
				
								elements_with_rule.append(elements)
				
					config_modif=copy.deepcopy(obj['ListDynP'][prop])# on recupere la config et on la modifie avec les regles
				
					config_modif["domain"].update(rule["then"]["config"]["domain"])
				
					config_modif["evolution"].update(rule["then"]["config"]["evolution"])


					for element in elements_with_rule: #### constitution de elements with rule and config modif
		
						if i%obj['ListDynP'][prop]['duration']==0 and egg[element]["v"][i] == "T" and obj['ListDynP'][prop]['evolution']['staticity']<random_for_all.pop(): ###check if it has to change now
		
							if obj['ListDynP'][prop]['evolution']['relation']=="true":
		
								changing_element.append(element)
		
							else:
		
								pass
						else:
		
							if i-1 in egg[element][prop]:
		
								egg[element][prop].update({i:egg[element][prop][i-1]})

					egg=gi_distrib_new.distrib(changing_element,copy.deepcopy(config_modif),prop,i,egg)


		logging.info (str(i)+" "+prop+" "+"end")
	logging.info (str(i)+" "+"end")

	i=i+1

	if k % 50 == 0:

		
		
		
		if k == 50:

			if args.vg_output == True:
	
				import vgcreator
				vgcreator.write(args.schema[0],egg)

		else:
			
			if args.vg_output == True:
	
				import vgcreator
				vgcreator.write_suite(args.schema[0],egg,k)

		if args.rdf_output == True:
	
			import rdfcreator
			rdfcreator.write_rdf(args.schema[0],graph_elements,egg,obj,k-50)


		for x in egg:

			for y in x:

				if not ( y=="out" or y=="in" ):

					x[y] = list(x[y][50])
		i=1			

		logging.info("clear")







	#################################
	# Ti for Dyn Properties : end
	#################################
logging.info ("Ti end")
#################################
# Ti : end
#################################





##########################
# memory usage at the end 
##########################
print os.getpid()
p = psutil.Process(os.getpid())

print p.memory_info()






# for e in egg:
# 	if not egg[e] == {} :
# 		logging.info (e+str(egg[e])+"\n\n\n")

################################
# vg output 
################################

if args.vg_output == True:

	import vgcreator

	if obj["interval"] < 50:
		
		vgcreator.write(args.schema[0],egg)

	else:

		vgcreator.write_suite(args.schema[0],egg,(obj["interval"]/50)*50)

################################
# rdf output 
################################

if args.rdf_output == True:
	
	import rdfcreator
	rdfcreator.write_rdf(args.schema[0],graph_elements,egg,obj,(obj["interval"]/50)*50)


################################
# plot by property
################################

if args.plot_byproperty=="all": 

	plot1.plot_validity(egg,graph_elements,obj)

	if "ListDynP" in obj:

		for prop in obj["ListDynP"]:

			elements_list=graph_elements[obj["ListDynP"][prop]["elements_type"]]

			plot1.plot(egg,list(elements_list),prop,obj)

elif not args.plot_byproperty == None:

	if args.plot_byproperty == "valid":

		plot1.plot_validity(egg,graph_elements,obj)

	else:

		elements_list=graph_elements[obj["ListDynP"][args.plot_byproperty]["elements_type"]]

		plot1.plot(egg,list(elements_list),args.plot_byproperty,obj)

################################
# plot by object 
################################

def element_label(element):

	for label in graph_elements:

		if element in graph_elements[label]:

			return label



if args.plot_byobject=="all" : 

	for element in egg:
		if len(egg[element])>0:
			
			plot2.plot_one(egg[element],element,obj["interval"],obj["ListDynP"],element_label(element),obj)

elif not args.plot_byobject==None:

	plot2.plot_one(egg[args.plot_byobject],args.plot_byobject,obj["interval"],obj["ListDynP"],element_label(element),obj)


