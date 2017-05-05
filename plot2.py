import numpy as np
import matplotlib.pyplot as plt

def plot(element_dict,element_id):

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
	plt.savefig(element_id+".png")

