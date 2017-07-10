import numpy as np
import matplotlib.pyplot as plt



	
	
N = 3



ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

ax.grid()
ax.set_axisbelow(True)

sparql_means =  (60.1594,658.7458,2000)
sparql_std = (11.71906606,43.71266781,0)
rects1 = ax.bar(ind + width, sparql_means, width, color='r',yerr=sparql_std)

DBFS_means = (76.2883,111.2985,165.9069)
DBFS_std = (121.7716176,186.0376419,231.2786242)
rects2 = ax.bar(ind, DBFS_means, width, color='y',yerr=DBFS_std)

oom_values = (0, 0, 2000)
rects3 = ax.bar(ind + width, oom_values, width, color='b',)

ax.set_ylabel('Time (in seconds)')
ax.set_title('Historical Reachability Queries: Disjunctive-BFS vs SPARQL\n Graph of size 100K nodes, 500K edges; Fixed query size=10')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10 snapshots\nInterval=[0,9]', '100 snapshots\nInterval=[45,54]', '1000 snapshots\nInterval=[495,504]'))

ax.legend((rects2[0], rects1[0], rects3[0]), ('Disjunctive-BFS', 'SPARQL', 'SPARQL \'out of memory\' exception'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.savefig("exp1.png")
plt.savefig("exp1.pdf")

plt.clf()


N = 4						

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

ax.grid()
ax.set_axisbelow(True)

sparql_means =  (633.2873,634.9834,633.4736,635.0977)
sparql_std = (5.880338427,5.666357799,4.634435917,4.725434725)
rects1 = ax.bar(ind + width, sparql_means, width, color='r',yerr=sparql_std)

DBFS_means = (47.8177,44.993,32.4027,33.1677)
DBFS_std = (34.49030971,38.86347258,34.03368506,37.17059919)

rects2 = ax.bar(ind, DBFS_means, width, color='y',yerr=DBFS_std)

ax.set_ylabel('Time (in seconds)')
ax.set_title('Historical Reachability Queries: Disjunctive-BFS vs SPARQL\n Graph of size 100K nodes, 500K edges; Fixed # of snapsots=100')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Interval=[50,50]', 'Interval=[45,54]', 'Interval=[25,74]', 'Interval=[0,99]'))

ax.legend((rects2[0], rects1[0]), ('Disjunctive-BFS', 'SPARQL'))




autolabel(rects1)
autolabel(rects2)




plt.savefig("exp2.png")
plt.savefig("exp2.pdf")
