import networkx as nx
import re
import argparse
import numpy as np
import logging
import os

if os.path.isfile('BFS.log'):
        os.remove('BFS.log')

logging.basicConfig(filename='BFS.log', level=logging.DEBUG,format='%(asctime)s %(message)s')

G=nx.Graph()
CL=nx.Graph()


parser = argparse.ArgumentParser(description='define the input schema.')

parser.add_argument('schema', metavar='schema', type=str, nargs=5,
                   help='the schema to process')

parser.add_argument('--log', action='store_true',
                   help='log')

args = parser.parse_args()

if args.log == False :
	logging.disable(logging.INFO)

#######################
#Construct vg in memory
#######################

with open('../'+args.schema[0]+'_output/'+args.schema[0]+'-vg.txt','r') as f:
		
	for line in f.readlines():
		
		match=re.match(r"^(\d*) (\d*) (\d*),(\d*)",line)
		
		if match:

			bitlist=[0]*int(args.schema[1])

			for i in range(int(match.group(3)),int(match.group(4))+1):

				bitlist[i]=1

			G.add_edge(match.group(1),match.group(2),Le=bitlist)

u = args.schema[2]
v = args.schema[3]
########## Please define the query interval i as a list of binaries with length equal to the interval
i = [1]*int(args.schema[1])

#######################
# BFS
#######################


IN=list()

def explore(niv, i, depth_ex):
	
	N_ex=list()
	
	for n in niv:
		IN.append(n)

		logging.info("n",n)

		for w in G.nodes():
			logging.info("w",w)
			if (n,w) in G.edges() or (w,n) in G.edges():

				ki = [x&y for (x,y) in zip(i,G[n][w]['Le'])]
				
				if ki != [0]*int(args.schema[1]):
				
					if w == v :

						print "yes"
						exit()

					if not w in IN :
			
						N_ex.append(w)

	logging.info("IN",IN)
	logging.info("N_ex",N_ex)

	if depth_ex + 1 < int(args.schema[4]) and N_ex:

		explore(N_ex, i, depth_ex+1)	

explore([u], i, 0)

print "no"
