import rdflib,re
import logging

logging.basicConfig(filename='egg.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

def write_rdf(schema,graph_elements,egg,configG):


	predicate=rdflib.Namespace("http://egg/predicate/")
	egg_nm=rdflib.Namespace("http://egg/")
	property_Nm=rdflib.Namespace("http://egg/property/")


	g = rdflib.ConjunctiveGraph()

	with open(schema+'-graph.txt','r') as f:
		
		for line in f.readlines():
			
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
			
			if match:
			
				s=rdflib.URIRef(match.group(2)+":"+match.group(3))
			
				p=rdflib.URIRef(match.group(4)+":"+match.group(5))
			
				o=rdflib.URIRef(match.group(6)+":"+match.group(7))

				n=rdflib.URIRef("http://egg/ng/gmark")

				g.add((s,p,o,n))

				p=rdflib.URIRef("edge"+":"+match.group(4))

				for snap in egg[match.group(5)]["valid"]:
					
					if egg[match.group(5)]["valid"][snap] == "T":
						
						n=rdflib.URIRef("http://egg/ng/snap"+str(snap))
					
						g.add((s,p,o,n))


	logging.info ("1 rdf end")
	
	i=0

	for key in graph_elements:

		for element in graph_elements[key]:

			s=rdflib.URIRef(key+":"+element)

			p=rdflib.URIRef(predicate.hasProperty)

			if key in configG["nodes"]:
				
				for prop in configG["nodes"][key]:
				
					o=rdflib.URIRef("Property:"+prop)
				
					n=rdflib.URIRef("http://egg/ng/G"+str(i))
				
					g.add((s,p,o,n))

					for snapshot in egg[element][prop]:

						s1=rdflib.URIRef("http://egg/ng/G"+str(i))

						p1=rdflib.URIRef(egg_nm.value)

						o1=rdflib.Literal(str(egg[element][prop][snapshot]))

						n1=rdflib.URIRef("http://egg/ng/snap"+str(snapshot))

						g.add((s1,p1,o1,n1))

					i=i+1					

			elif key in configG["edges"] :		

				for prop in configG["edges"][key]:
				
					o=rdflib.URIRef("Property:"+prop)
				
					n=rdflib.URIRef("http://egg/ng/G"+str(i))
				
					g.add((s,p,o,n))

					for snapshot in egg[element][prop]:

						s1=rdflib.URIRef("http://egg/ng/G"+str(i))

						p1=rdflib.URIRef(egg_nm.value)

						o1=rdflib.Literal(str(egg[element][prop][snapshot]))

						n1=rdflib.URIRef("http://egg/ng/snap"+str(snapshot))

						g.add((s1,p1,o1,n1))

					i=i+1



	logging.info ("2 rdf end")				
	

	with open(schema+"-output.trig","w") as f:
		f.write(g.serialize(format='trig'))	


	logging.info ("rdf end")	
