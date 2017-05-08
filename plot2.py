import numpy as np
import matplotlib.pyplot as plt

def plot_one(element_dict,element_id):

	x=list()
	y1=list()
	y2=list()
	y3=list()


	for i in range(0, len(element_dict["hotelPrice"])):
		x.append(i)
		y1.append(element_dict["hotelPrice"][i])
		y2.append(element_dict["availRoom"][i])
		y3.append(element_dict["star"][i])

	plt.figure(1)

	plt.subplot(311)
	plt.plot(x, y1, 'b-')
	plt.title(element_id)
	plt.xlabel('interval', fontsize=14, color='black')
	plt.ylabel('values', fontsize=14, color='black')
	plt.subplot(312)
	plt.plot(x, y2, 'r-')
	plt.xlabel('interval', fontsize=14, color='black')
	plt.ylabel('values', fontsize=14, color='black')
	plt.subplot(313)
	plt.plot(x, y3, 'g-')
	plt.xlabel('interval', fontsize=14, color='black')
	plt.ylabel('values', fontsize=14, color='black')
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