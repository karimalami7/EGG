import numpy as np
import matplotlib.pyplot as plt

formdict={"1":['b-','r-'],"2":['b--','r--'],"3":['b^','r^'],"4":['b-','r-'],"5":['b+','r+']}
color_tab=['b','g','r','y','p']
### plot by property

def plot(egg,elements_list,prop,config_egg):

	
	x=list()
	y=list()

	for i in range(0,len(egg[elements_list[0]][prop])):

		x.append(i)

	

	### plot distribution

	if config_egg['ListDynP'][prop]['domain']['type']=='qualitatif':
		if config_egg['ListDynP'][prop]['domain']['order']=='false':	

			###### creation d'un dict des valeurs de la propriete
			prop_values_dict=dict()
			
			for prop_value in config_egg["ListDynP"][prop]['domain']['values']:

				prop_values_dict.update({prop_value:0})

			print prop_values_dict

			for i in range(0,len(egg[elements_list[0]][prop])):

				for e in elements_list:

					value = egg[e][prop][i]

					prop_values_dict[value]=prop_values_dict[value]+1
				
				print prop_values_dict

				for prop_value in prop_values_dict:

					if config_egg["ListDynP"][prop]['domain']['values'].index(prop_value)==0:

						plt.bar(i,prop_values_dict[prop_value],color=color_tab[config_egg["ListDynP"][prop]['domain']['values'].index(prop_value)])

					else :

						plt.bar(i,prop_values_dict[prop_value],color=color_tab[config_egg["ListDynP"][prop]['domain']['values'].index(prop_value)],bottom=prop_values_dict[config_egg["ListDynP"][prop]['domain']['values'][config_egg["ListDynP"][prop]['domain']['values'].index(prop_value)-1]])

					prop_values_dict[prop_value]=0






	
	if config_egg['ListDynP'][prop]['domain']['type']=='qualitatif':
		if config_egg['ListDynP'][prop]['domain']['order']=='true':

			j=0

			for e in elements_list:

				y.append(list())


				for keys in egg[e][prop]:
		
					y[j].append(egg[e][prop][keys])

				plt.plot(x,y[j],'r-')

				j=j+1


			y.append(list())
			for i in range (0, len(x)):
				y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['values'][0])
			plt.plot(x,y[len(y)-1],'b+')
			y.append(list())
			for i in range (0, len(x)):
				y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['values'][len(config_egg['ListDynP'][prop]['domain']['values'])-1])
			plt.plot(x,y[len(y)-1],'b+')

	if config_egg['ListDynP'][prop]['domain']['type']=='quantitatif:dis':

		j=0
		for e in elements_list:
			y.append(list())
			for keys in egg[e][prop]:
	
				y[j].append(egg[e][prop][keys])
			plt.plot(x,y[j],'r-')
			j=j+1

		y.append(list())
		for i in range (0, len(x)):
			y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['values']["min"])
		plt.plot(x,y[len(y)-1],'b+')
		y.append(list())
		for i in range (0, len(x)):
			y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['values']["max"])
		plt.plot(x,y[len(y)-1],'b+')


	if config_egg['ListDynP'][prop]['domain']['type']=='quantitatif:con':
		if config_egg['ListDynP'][prop]['domain']['distribution']['type']=="normal":

			j=0

			for e in elements_list:

				y.append(list())


				for keys in egg[e][prop]:
		
					y[j].append(egg[e][prop][keys])

				plt.plot(x,y[j],'r-')

				j=j+1


			y.append(list())
			for i in range (0,len(x)):
				y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['distribution']['mean'])
			plt.plot(x,y[len(y)-1],'b+')
			y.append(list())
			for i in range (0,len(x)):
				y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['distribution']['mean']+config_egg['ListDynP'][prop]['domain']['distribution']['sigma'])
			plt.plot(x,y[len(y)-1],'g+')
			y.append(list())
			for i in range (0,len(x)):
				y[len(y)-1].append(config_egg['ListDynP'][prop]['domain']['distribution']['mean']-config_egg['ListDynP'][prop]['domain']['distribution']['sigma'])
			plt.plot(x,y[len(y)-1],'g+')

	for rule in config_egg['ListDynP'][prop]['rules']:
		if rule['then']['config']['domain']['distribution']['type']=="normal":
		
			j=0

			for e in elements_list:

				y.append(list())


				for keys in egg[e][prop]:
		
					y[j].append(egg[e][prop][keys])

				plt.plot(x,y[j],'r-')

				j=j+1

			y.append(list())
			for i in range (0,len(x)):
				y[len(y)-1].append(rule['then']['config']['domain']['distribution']['mean'])
			plt.plot(x,y[len(y)-1],'b+')
			y.append(list())
			for i in range (0,len(x)):
				y[len(y)-1].append(rule['then']['config']['domain']['distribution']['mean']+rule['then']['config']['domain']['distribution']['sigma'])
			plt.plot(x,y[len(y)-1],'g+')
			y.append(list())
			for i in range (0,len(x)):
				y[len(y)-1].append(rule['then']['config']['domain']['distribution']['mean']-rule['then']['config']['domain']['distribution']['sigma'])
			plt.plot(x,y[len(y)-1],'g+')

	###

	plt.xlabel('Time', fontsize=14, color='black')
	plt.ylabel('Values', fontsize=14, color='black')
	plt.title('Property ' + prop + ' of '+ config_egg['ListDynP'][prop]["elements_type"])



	plt.savefig("byproperty/"+prop+".png")
	plt.clf() # clear plot 
