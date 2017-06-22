import re
import logging

logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

def graph_parser(schema):

	egg=list() #### global variable : keys are graph nodes and edges id
	
	graph_elements=dict()
	
	with open(schema+'-graph.txt','r') as f:
		a=f.readlines()
 	match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",a[len(a)-1])

	egg=[None]*(int(match.group(5))+1)
	for line in range(0, len(a)):
		match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",a[line])
		if match:
			# parse edges
			if match.group(4) in graph_elements: 
				graph_elements[match.group(4)].add(int(match.group(5)))
	  			egg[int(match.group(5))]=dict()
	  			egg[int(match.group(5))].update({"out":int(match.group(3))})
	  			egg[int(match.group(5))].update({"in":int(match.group(7))})
			else:
	 			graph_elements[match.group(4)]={int(match.group(5))}
	 			egg[int(match.group(5))]=dict()
                  
	 			##### insert    : insert in first place
                    
	 			egg[int(match.group(5))].update({"out":int(match.group(3))})
	  			egg[int(match.group(5))].update({"in":int(match.group(7))})
	 		# parse source nodes 
	 		if match.group(2) in graph_elements: 
	  			graph_elements[match.group(2)].add(int(match.group(3)))
	  			egg[int(match.group(3))]=dict()
			else:
	 			graph_elements[match.group(2)]={int(match.group(3))}
	  			egg[int(match.group(3))]=dict()
	 		# parse object nodes
	 		if match.group(6) in graph_elements: 
	  			graph_elements[match.group(6)].add(int(match.group(7)))
	  			egg[int(match.group(7))]=dict()
			else:
	 			graph_elements[match.group(6)]={int(match.group(7))}
	 			egg[int(match.group(7))]=dict()
	del a[:]
	

	return (egg,graph_elements)