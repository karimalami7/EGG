import rdflib,re
import logging

logging.basicConfig(filename='egg.log',level=logging.DEBUG)

def write_rdf(schema,graph_elements,egg,configG):

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

	predicate=rdflib.Namespace("http://egg/predicate/")
	property_Nm=rdflib.Namespace("http://egg/property/")
	
	g = rdflib.ConjunctiveGraph()
	i=0
	
	with open(schema+'-graph.txt','r') as f:
		for line in f.readlines():
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
			if match:
				s=rdflib.URIRef(match.group(2)+":"+match.group(3))
				p=rdflib.URIRef(match.group(4)+":"+match.group(5))
				o=rdflib.URIRef(match.group(6)+":"+match.group(7))
				n=rdflib.URIRef("http://egg/ng/G"+str(i))
				g.add((s,p,o))
				

	for key in graph_elements:
		for element in graph_elements[key]:
			s=rdflib.URIRef(key+":"+element)
			p=rdflib.URIRef(predicate.hasProperty)
			if key in configG["nodes_edges"]:
				for prop in configG["nodes_edges"][key]:
					o=rdflib.URIRef(prop)
					n=rdflib.URIRef("http://egg/ng/G"+str(i))
					g.add((s,p,o,n))
					i=i+1
					j=i-1
					for snapshot in egg[element][prop]:
						s1=rdflib.URIRef("http://egg/ng/G"+str(j))
						p1=rdflib.URIRef(predicate.instant)
						o1=rdflib.Literal(str(snapshot))
						n1=rdflib.URIRef("http://egg/ng/G"+str(i))
						p2=rdflib.URIRef(predicate.value)
						o2=rdflib.Literal(str(egg[element][prop][snapshot]))
						g.add((s1,p1,o1,n1))
						g.add((s1,p2,o2,n1))
						i=i+1




	with open(schema+"-output.trig","w") as f:
		f.write(g.serialize(format='trig'))