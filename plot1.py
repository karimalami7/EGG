import numpy as np
import matplotlib.pyplot as plt

formdict={"1":['b-','r-'],"2":['b--','r--'],"3":['b^','r^'],"4":['b-','r-'],"5":['b+','r+']}



def plot(egg,elements_list,prop):

	import matplotlib.pyplot as plt
	x=list()
	y=list()

	for i in range(0,len(egg[elements_list[0]][prop])):

		x.append(i)

	j=0

	for e in elements_list:

		y.append(list())


		for keys in egg[e][prop]:
		
			y[j].append(egg[e][prop][keys])

		plt.plot(x,y[j],'r-')

		j=j+1

	plt.xlabel('interval', fontsize=14, color='black')
	plt.ylabel('values', fontsize=14, color='black')
	plt.title(prop)
	plt.savefig("byproperty/"+prop+".png")
	plt.clf() # clear plot 