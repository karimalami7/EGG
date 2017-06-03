import numpy as np
import matplotlib.pyplot as plt

### plot by object

color_dict=['b','g','r','y','p']

def plot_one(element_dict,element_id,interval,config_egg):

	if len(element_dict) > 0 :
		plt.figure(1)
		plt.xlabel("time")
		j=0
	
		f,axarr=plt.subplots(len(element_dict), sharex=True)
	
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
					
			else :
				var=[None]*len(config_egg[prop]['domain']['values'])
				if type(axarr) is np.ndarray:
					for i in range(0, interval):
						index_of_value=config_egg[prop]['domain']['values'].index(element_dict[prop][i])
						var[index_of_value]=axarr[j].bar(i,1,color=color_dict[config_egg[prop]["domain"]["values"].index(element_dict[prop][i])])
					axarr[j].legend(var,config_egg[prop]['domain']['values'])
					axarr[j].set_title("Property "+prop+" of "+config_egg[prop]['element']+" "+element_id+" of type "+config_egg[prop]['elements_type'])
					axarr[j].set_yticks([0,1])
				else: 
					for i in range(0, interval):
						index_of_value=config_egg[prop]['domain']['values'].index(element_dict[prop][i])
						var[index_of_value]=axarr.bar(i,1,color=color_dict[config_egg[prop]["domain"]["values"].index(element_dict[prop][i])])
					axarr.legend(var,config_egg[prop]['domain']['values'])
					axarr.set_title("Property "+prop+" of "+config_egg[prop]['element']+" "+element_id+" of type "+config_egg[prop]['elements_type'])
					axarr[j].set_yticks([0,1])
			j=j+1
	
		# if node " node type " + le type du noeud
		# else " edge predicate " + le type de l'arrete
		f.subplots_adjust(hspace=0.4)
		plt.xlabel("TIME").set_fontsize(16)
		plt.savefig("byobject/"+element_id+".png")
		plt.clf()

	else :

		print "this object has no properties"