import numpy as np
import matplotlib.pyplot as plt

### plot by object

def plot_one(element_dict,element_id,interval,config):

	plt.figure(1)

	j=1
	for prop in egg[element_id]:
			
		if  config[prop]["domain"]["type"]=="quantitatif:con" or config[prop]["domain"]["type"]=="quantitatif:dis" or ( config[prop]["domain"]["type"]=="qualitatif" and config[prop]["domain"]["order"]=="true" ) :

			y=list()
			x=list()

			for i in range(0, interval):
				x.append(i)
				y.append(egg[element_id][prop][i])
				
			subplot=(100*len(egg[element_id])) + 10 + j
				
			plt.subplot(subplot)
			plt.plot(x, y, 'b-')
			plt.title(element_id+prop)
			plt.xlabel('interval', fontsize=14, color='black')
			plt.ylabel('values', fontsize=14, color='black')
			j=j+1	
		
	plt.savefig("byobject/"+element_id+".png")
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
					y.append(egg[element_id][prop][i])
				
				subplot=(100*len(egg[element_id])) + 10 + j
				
				plt.subplot(subplot)
				plt.plot(x, y, 'b-')
				plt.title(element_id+prop)
				plt.xlabel('interval', fontsize=14, color='black')
				plt.ylabel('values', fontsize=14, color='black')
				j=j+1	
		
		plt.savefig("byobject/"+element_id+".png")
		plt.clf()