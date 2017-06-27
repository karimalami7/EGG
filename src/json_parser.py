import logging
#################evaluate config file json and put it in dict
def eval_config(schema):
	f=open('../../use_cases/'+schema+'/'+schema+'-config.json','r')	
	obj=eval(f.read())
	return obj

#################property dependance graph
def sorted_list(obj):
	graph=dict()
	if "ListDynP" in obj:
		for Prop in obj["ListDynP"]:
			graph[Prop]=set();
			for rules_prop in obj["ListDynP"][Prop]["rules"]:
				graph[Prop].add(rules_prop["if"]["prop"]) # destination node are keys 
			for rules_prop in obj["ListDynP"][Prop]["rulese"]:
				graph[Prop].add(rules_prop["if"]["prop"]) # destination node are keys 
	
		#################kahns algorithm : begin
		L=list()
		S=set()
		####remplissage S
		for e in graph:
			if not graph[e]:
				S.add(e)
		#### algorithms body
		while S:
			unlinked_node=S.pop()
			L.append(unlinked_node)
			for link_node in graph:
				if unlinked_node in graph[link_node]:
					graph[link_node].remove(unlinked_node)
					if not graph[link_node]:
						S.add(link_node)
		#logging.info ("sorted properties list is : "+str(L))
		#################kahns algorithm : end
		return L

	else :

		return []
