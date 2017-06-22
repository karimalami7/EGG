import logging,re,os


def write(schema,egg):

	vg = open(schema+'-vg.txt','w')

	with open(schema+'-graph.txt','r') as f:
	
		for line in f.readlines():
		
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
		
			if match:

				true=list()

				egg_valid=egg[int(match.group(5))]["v"]

				for snap in range (0,len(egg_valid)):
					
                    
					if egg_valid[snap] == "T" and (snap == 0 or egg_valid[snap-1] == "F") :

						true.append(dict())

						true[len(true)-1].update({"min":snap})

					elif egg_valid[snap] == "F" and snap > 0 and egg_valid[snap-1] == "T":

						true[len(true)-1].update({"max":snap-1})
			 	

				if true : 

					if not "max" in true[len(true)-1]:

						true[len(true)-1]["max"] = len (egg_valid) -1

					edge_in_vg = match.group(3) + " " + match.group(7)

					for interval in true:

						edge_in_vg = edge_in_vg + " " + str(interval["min"])  + "," + str(interval["max"])

					vg.write(edge_in_vg + "\n")

	vg.close()

	logging.info ("vg end")


def write_suite(schema, egg, start_point):

	vg_suite = open(schema+'-vg.txt.suite','w')

	vg = open(schema+'-vg.txt','r')

	f = open(schema+'-graph.txt','r')

	for (line_vg,line_f) in zip(vg.readlines(),f.readlines()) :

		match_f=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line_f)

		if match_f:

			true=list()

			egg_valid=egg[int(match_f.group(5))]["v"]



			for snap in range (0,len(egg_valid)):
					
                   
				if egg_valid[snap] == "T" and (snap == 0 or egg_valid[snap-1] == "F") :

					true.append(dict())

					true[len(true)-1].update({"min":snap})

				elif egg_valid[snap] == "F" and snap > 0 and egg_valid[snap-1] == "T":

					true[len(true)-1].update({"max":snap-1})
			 	

			if true : 



				if not "max" in true[len(true)-1]:

					true[len(true)-1]["max"] = len (egg_valid) -1

				edge_in_vg = line_vg.rstrip()

				for interval in true:

					edge_in_vg = edge_in_vg + " " + str(start_point + interval["min"])  + "," + str(start_point + interval["max"])

				vg_suite.write(edge_in_vg + "\n")

	vg.close()
	f.close()
	vg_suite.close()

	os.rename(schema+'-vg.txt.suite',schema+'-vg.txt')
	
	logging.info ("vg_suite end")






