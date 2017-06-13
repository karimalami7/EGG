import rdflib,re
import logging

logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

def write_rdf(schema,graph_elements,egg,configG):

	g = rdflib.ConjunctiveGraph()

	i=0
	


	with open(schema+'-graph.txt','r') as f:
		for line in f.readlines():
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
			if match:
				s=rdflib.URIRef(match.group(2)+":"+match.group(3))
				p=rdflib.URIRef(":"+match.group(4))
				o=rdflib.URIRef(match.group(6)+":"+match.group(7))


				for keys in egg[match.group(5)]["valid"]:
					
					if egg[match.group(5)]["valid"][keys] == "1":
						
						n=rdflib.URIRef("http://egg/ng/snap"+str(keys))
						g.add((s,p,o,n))



	with open(schema+"-output.trig","w") as f:
		f.write(g.serialize(format='trig'))