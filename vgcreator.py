import logging,re


def write(schema,egg):

	vg = open(schema+'-vg.txt','w')

	with open(schema+'-graph.txt','r') as f:
	
		for line in f.readlines():
		
			match=re.match(r"(^(\w+):(\w+) (\w+):(\w+) (\w+):(\w+))",line)
		
			if match:

				true=list()

				egg_valid=egg[match.group(5)]["valid"]

				for snap in egg_valid:
					
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