import rdflib,re



def write_rdf(graph_elements,egg,configG):

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

	
	g = rdflib.ConjunctiveGraph()
	i=0
	
	with open('trip-graph.txt','r') as f:
		for line in f.readlines():
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
			if match:
				s=rdflib.URIRef(match.group(2)+":"+match.group(3))
				p=rdflib.URIRef(match.group(4)+":"+match.group(5))
				o=rdflib.URIRef(match.group(6)+":"+match.group(7))
				n=rdflib.URIRef("G"+str(i))
				g.add((s,p,o,n))
				i=i+1

	for key in graph_elements:
		for element in graph_elements[key]:
			s=rdflib.URIRef(key+":"+element)
			p=rdflib.Literal("hasProperty")
			if key in configG["nodes_edges"]:
				for prop in configG["nodes_edges"][key]:
					o=rdflib.Literal(prop)
					n=rdflib.URIRef("G"+str(i))
					g.add((s,p,o,n))
					i=i+1
					j=i-1
					for snapshot in egg[element][prop]:
						s1=rdflib.URIRef("G"+str(j))
						p1=rdflib.Literal("moment")
						o1=rdflib.Literal(str(snapshot))
						n1=rdflib.URIRef("G"+str(i))
						p2=rdflib.Literal("value")
						o2=rdflib.Literal(str(egg[element][prop][snapshot]))
						g.add((s1,p1,o1,n1))
						g.add((s1,p2,o2,n1))
						i=i+1




	with open("rdfOutput.txt","w") as f:
		f.write(g.serialize(format='trig'))