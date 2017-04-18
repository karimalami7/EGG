import rdflib,re

type_namespace=dict()
type_namespace.update({"city":"http://example.org/city"})
type_namespace.update({"hotel":"http://example.org/hotel"})
type_namespace.update({"train":"http://example.org/train"})
type_namespace.update({"abrite":"http://example.org/abrite"})
type_namespace.update({"weather":"http://example.org/weather"})
type_namespace.update({"qAir":"http://example.org/qAir"})
type_namespace.update({"availRoom":"http://example.org/availRoom"})
type_namespace.update({"star":"http://example.org/star"})
type_namespace.update({"hotelPrice":"http://example.org/hotelPrice"})
type_namespace.update({"trainPrice":"http://example.org/trainPrice"})




g = rdflib.Graph()
with open('trip-graph.txt','r') as f:
	for line in f.readlines():
		match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
		if match:
			s=rdflib.URIRef(match.group(2)+":"+match.group(3))
			p=rdflib.URIRef(match.group(4)+":"+match.group(5))
			o=rdflib.URIRef(match.group(6)+":"+match.group(7))
			g.add((s,p,o))

#######serializing gmark to rdf


#####linking elements to properties in RDF

graph_elements=dict()
	
with open('trip-graph.txt','r') as f:
	for line in f.readlines():
		match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
		if match:
			# parse edges
			if match.group(4) in graph_elements: 
	  			elements_set=graph_elements[match.group(4)]
	  			elements_set.add(match.group(5))
	  			
			else:
	 			graph_elements[match.group(4)]={match.group(5)}
	 			
	 		# parse source nodes 
	 		if match.group(2) in graph_elements: 
	  			elements_set=graph_elements[match.group(2)]
	  			elements_set.add(match.group(3))
	  			
			else:
	 			graph_elements[match.group(2)]={match.group(3)}
	 		
	 		# parse object nodes
	 		if match.group(6) in graph_elements: 
	  			elements_set=graph_elements[match.group(6)]
	  			elements_set.add(match.group(7))
	  			
			else:
	 			graph_elements[match.group(6)]={match.group(7)}
	 			


f=open('config.json','r')	
obj=eval(f.read())



for key in graph_elements:
	for element in graph_elements[key]:
		s=rdflib.URIRef(key+":"+element)
		p=rdflib.Literal("hasProperty")
		if key in obj["nodes_edges"]:
			for prop in obj["nodes_edges"][key]:
				o=rdflib.Literal(prop)
				g.add((s,p,o))


print g.serialize(format='turtle')