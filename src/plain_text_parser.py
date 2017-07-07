#######################################
#
#	Project: EGG 
#
#	File: plain_text_parser.py
#
#
#	Description: Parse the output of gMark, create two storages in memory (graph_elements, egg)
#
#   			* graph_elements : is a dict, keys : types of edges and nodes
#											  values : set of elements of this type
#
#
#
#				* egg : is a dict: keys : elements of the gMark graph
#								   values : dict -> keys : properties of this element
#													values : list of values for each snapshot



import re
import logging

logging.basicConfig(filename='../egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

######################################################
# parse gmark output and return egg and graph_elements
######################################################

def graph_parser(schema):

	egg=dict() #### global variable : keys are graph nodes and edges id
	
	graph_elements=dict()
	
	with open("../"+schema+"_output/"+schema+'-graph.txt','r') as f:
		for line in f.readlines():
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
			if match:
				# parse edges
				if match.group(4) in graph_elements: 
	  				graph_elements[match.group(4)].add(match.group(5))
	  				egg[match.group(5)]=dict()
	  				egg[match.group(5)].update({"out":match.group(3)})
	  				egg[match.group(5)].update({"in":match.group(7)})
				else:
	 				graph_elements[match.group(4)]={match.group(5)}
	 				egg[match.group(5)]=dict()
	 				egg[match.group(5)].update({"out":match.group(3)})
	  				egg[match.group(5)].update({"in":match.group(7)})
	 			# parse source nodes 
	 			if match.group(2) in graph_elements: 
	  				graph_elements[match.group(2)].add(match.group(3))
	  				egg[match.group(3)]=dict()
				else:
	 				graph_elements[match.group(2)]={match.group(3)}
	 				egg[match.group(3)]=dict()
	 			# parse object nodes
	 			if match.group(6) in graph_elements: 
	  				graph_elements[match.group(6)].add(match.group(7))
	  				egg[match.group(7)]=dict()
				else:
	 				graph_elements[match.group(6)]={match.group(7)}
	 				egg[match.group(7)]=dict()

	

	return (egg,graph_elements)