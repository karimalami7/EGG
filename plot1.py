import numpy as np
import matplotlib.pyplot as plt

formdict={"1":['b-','r-'],"2":['b--','r--'],"3":['b^','r^'],"4":['b-','r-'],"5":['b+','r+']}

x=list()
y=list()
for m in range (0,10):
	y.append(list())

def plot(egg,starplot):

	for e in  egg[starplot['1'][0]]['star'].keys():

		x.append(e)
		
	print "starplot: ",starplot
	i=0
	for star in starplot:

		if len (starplot[star])>=2:

			for j in range(0, len (egg[starplot[star][0]]['star'])):
				
				y[i].append(egg[starplot[star][0]]['hotelPrice'][j])
			plt.plot(x,y[i],formdict[star][0])	
			i=i+1

			for k in range(0, len (egg[starplot[star][1]]['star'])):
				
				y[i].append(egg[starplot[star][1]]['hotelPrice'][k])
			plt.plot(x,y[i],formdict[star][1])	
			i=i+1



	plt.show() # affiche la figure a l'ecran