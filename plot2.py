import numpy as np
import matplotlib.pyplot as plt

def plot(element):

	x=list()
	y1=list()
	y2=list()
	y3=list()


	for i in range(0, len(element["hotelPrice"])):
		x.append(i)
		y1.append(element["hotelPrice"][i])
		y2.append(element["availRoom"][i])
		y3.append(element["star"][i])

	plt.figure(1)

	plt.subplot(311)
	plt.plot(x, y1, 'b-')
	
	plt.subplot(312)
	plt.plot(x, y2, 'r-')

	plt.subplot(313)
	plt.plot(x, y3, 'g-')

	plt.show()