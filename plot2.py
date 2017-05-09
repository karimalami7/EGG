import numpy as np
import matplotlib.pyplot as plt

### plot by object

def plot_one(element_dict,element_id,interval,config):

	plt.figure(1)

	j=1
	for prop in element_dict:
			
		if  config[prop]["domain"]["type"]=="quantitatif:con" or config[prop]["domain"]["type"]=="quantitatif:dis" or ( config[prop]["domain"]["type"]=="qualitatif" and config[prop]["domain"]["order"]=="true" ) :

			y=list()
			x=list()

			for i in range(0, interval):
				x.append(i)
				y.append(int(element_dict[prop][i]))
				
			subplot=(100*len(element_dict)) + 10 + j
				
			plt.subplot(subplot)
			plt.plot(x, y, 'b-')
			plt.title(element_id+prop)
			plt.xlabel('Time', fontsize=14, color='black')
			plt.ylabel('Values', fontsize=14, color='black')
			j=j+1	
		
	plt.savefig("byobject/"+element_id+".pdf")
	plt.clf()



def plot_all(egg,interval,config):

	for element_id in egg:
		
		plt.figure(1)

		j=1
		for prop in egg[element_id]:
			
			if  config[prop]["domain"]["type"]=="quantitatif:con" or config[prop]["domain"]["type"]=="quantitatif:dis" or ( config[prop]["domain"]["type"]=="qualitatif" and config[prop]["domain"]["order"]=="true" ) :

				y=list()
				x=list()

				for i in range(0, interval):
					x.append(i)
					y.append(int(egg[element_id][prop][i]))
				
				subplot=(100*len(egg[element_id])) + 10 + j
				
				plt.subplot(subplot)
				plt.plot(x, y, 'b-')
				plt.title("Property " + prop + " of node/edge TODO " + element_id + " (type + TODO type" + ")")
				plt.xlabel('Time', fontsize=14, color='black')
				plt.ylabel('Values', fontsize=14, color='black')
				j=j+1	
		
		plt.savefig("byobject/"+element_id+".pdf")
		plt.clf()
