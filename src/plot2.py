import numpy as np
import matplotlib.pyplot as plt

### plot by object

color_dict=['b','g','r','y','p']

def plot_one(element_dict,element_id,interval,config_egg,label,configG,schema):

	element_dict.pop('in', None)
	element_dict.pop('out', None)
	valid_dict=element_dict.pop('v', None)

	if len(element_dict) > 0 :
		plt.figure(1)
		plt.xlabel("time")
		
	
		f,axarr=plt.subplots(len(element_dict)+1, sharex=True)

		plot_id=[None,None]
		for i in range(0,interval):
			if valid_dict[i] == "T":
				plot_id[0]=axarr[0].bar(i,1,color=color_dict[0])
			else:
				plot_id[1]=axarr[0].bar(i,1,color=color_dict[1])

			axarr[0].legend(plot_id,["T","F"])
			axarr[0].set_yticks([])
			axarr[0].set_title("Validity of "+configG["validity"][label]["type"]+" "+element_id+" of type "+label)


		j=1

		for prop in element_dict:
				
			if  config_egg[prop]["domain"]["type"]=="quantitatif:con" or config_egg[prop]["domain"]["type"]=="quantitatif:dis" or ( config_egg[prop]["domain"]["type"]=="qualitatif" and config_egg[prop]["domain"]["order"]=="true" ) :
	
				y=list()
				x=list()
	
				for i in range(0, interval):
					x.append(i)
					y.append(int(element_dict[prop][i]))
			
				if type(axarr) is np.ndarray	:
					axarr[j].plot(x, y, 'b-')
					axarr[j].set_title("Property "+prop+" of "+config_egg[prop]['element']+" "+element_id+" of type "+config_egg[prop]['elements_type'])
					# axarr[j].set_xlabel('Time', fontsize=14, color='black')
					axarr[j].set_ylabel('Values', fontsize=14, color='black').set_fontsize(12)
				else :
					axarr.plot(x, y, 'b-')
					axarr.set_title("Property "+prop+" of "+config_egg[prop]['element']+" "+element_id+" of type "+config_egg[prop]['elements_type'])
					# axarr[j].set_xlabel('Time', fontsize=14, color='black')
					axarr.set_ylabel('Values', fontsize=14, color='black').set_fontsize(12)

				if config_egg[prop]["domain"]["type"]=="qualitatif" and config_egg[prop]["domain"]["order"]=="true":


					tab =list()
					for i in range (0,len(config_egg[prop]["domain"]["values"])) :
						tab.append(int(config_egg[prop]["domain"]["values"][i]))
					axarr[j].set_yticks(tab)
					
			else : ########qualitatif plot 

				var=[None]*len(config_egg[prop]['domain']['values'])
				if type(axarr) is np.ndarray:
					for i in range(0, interval):
						index_of_value=config_egg[prop]['domain']['values'].index(element_dict[prop][i])
						var[index_of_value]=axarr[j].bar(i,1,color=color_dict[config_egg[prop]["domain"]["values"].index(element_dict[prop][i])])
					axarr[j].legend(var,config_egg[prop]['domain']['values'])
					axarr[j].set_title("Property "+prop+" of "+config_egg[prop]['element']+" "+element_id+" of type "+config_egg[prop]['elements_type'])
					axarr[j].set_yticks([])
				else: 
					for i in range(0, interval):
						index_of_value=config_egg[prop]['domain']['values'].index(element_dict[prop][i])
						var[index_of_value]=axarr.bar(i,1,color=color_dict[config_egg[prop]["domain"]["values"].index(element_dict[prop][i])])
					axarr.legend(var,config_egg[prop]['domain']['values'])
					axarr.set_title("Property "+prop+" of "+config_egg[prop]['element']+" "+element_id+" of type "+config_egg[prop]['elements_type'])
					axarr[j].set_yticks([])
			j=j+1
	
		# if node " node type " + le type du noeud
		# else " edge predicate " + le type de l'arrete
		f.subplots_adjust(hspace=0.4)
		plt.xlabel("Time").set_fontsize(16)





	if len(element_dict) == 0 : ### because axarr doesnot support set_yticks when there is only one plot

		plot_id=[None,None]
		for i in range(0,interval):

			if valid_dict[i] == "T":
				plot_id[0]=plt.bar(i,1,color=color_dict[0])
			else:
				plot_id[1]=plt.bar(i,1,color=color_dict[1])
			
			plt.legend(plot_id,("T","F"))
			plt.yticks([])
			plt.title("Validity of "+configG["validity"][label]["type"]+" "+element_id+" of type "+label)

	

	plt.savefig("../"+schema+"_output/"+"byobject/"+element_id+".png")
	plt.clf()