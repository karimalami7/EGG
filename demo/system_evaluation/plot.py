import numpy as np
import matplotlib.pyplot as plt



	
	
N = 3



ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

#plt.grid()

sparql_values =  (60.1594,658.7458,1000)
rects1 = ax.bar(ind + width, sparql_values, width, color='r')

DBFS_values = (76.2883,111.2985,165.9069)

rects2 = ax.bar(ind, DBFS_values, width, color='y')

oom_values = (0, 0, 2000)
rects3 = ax.bar(ind + width, oom_values, width, color='b')

ax.set_ylabel('Time')
ax.set_title('Historical Reachability Queries: Disjunctive-BFS vs SPARQL\n Graph of size 100K nodes, 500K edges; Fixed query size=10')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10 snapshots\nInterval=[0,9]', '100 snapshots\nInterval=[45,54]', '1000 snapshots\nInterval=[495,504]'))

ax.legend((rects2[0], rects1[0], rects3[0]), ('Disjunctive-BFS', 'SPARQL', 'SPARQL \'out of memory\' exception'))

plt.savefig("exp1.png")
plt.savefig("exp1.pdf")

plt.clf()


N = 4

							

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

sparql_values =  (633.2873,634.9834,633.4736,635.0977)
rects1 = ax.bar(ind + width, sparql_values, width, color='r')

DBFS_values = (47.8177,44.993,32.4027,33.1677)

rects2 = ax.bar(ind, DBFS_values, width, color='y')

ax.set_ylabel('Time')
ax.set_title('Historical Reachability Queries: Disjunctive-BFS vs SPARQL\n Graph of size 100K nodes, 500K edges; Fixed # of snapsots=100')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Interval=[50,50]', 'Interval=[45,54]', 'Interval=[25,74]', 'Interval=[0,99]'))

ax.legend((rects2[0], rects1[0]), ('Disjunctive-BFS', 'SPARQL'))

plt.savefig("exp2.png")
plt.savefig("exp2.pdf")
