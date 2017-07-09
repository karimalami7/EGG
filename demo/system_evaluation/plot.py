import numpy as np
import matplotlib.pyplot as plt



	
	
N = 3


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

sparql_values =  (60.1594,658.7458,1000)
rects1 = ax.bar(ind, sparql_values, width, color='r')

DBFS_values = (76.2883,111.2985,165.9069)

rects2 = ax.bar(ind + width, DBFS_values, width, color='y')

ax.set_ylabel('Time')
ax.set_title('Sparql vs D-BFS for 100kn and 500ke')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10s', '100s', '1000s'))

ax.legend((rects1[0], rects2[0]), ('Sparql', 'D-BFS'))

plt.savefig("exp1.png")
plt.savefig("exp1.pdf")

plt.clf()


N = 4

							

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

sparql_values =  (633.2873,634.9834,633.4736,635.0977)
rects1 = ax.bar(ind, sparql_values, width, color='r')

DBFS_values = (47.8177,44.993,32.4027,33.1677)

rects2 = ax.bar(ind + width, DBFS_values, width, color='y')

ax.set_ylabel('Time')
ax.set_title('Sparql vs D-BFS for 100kn and 500ke')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('i = 50', 'i = 45->54', 'i = 25->74', 'i = 0->99'))

ax.legend((rects1[0], rects2[0]), ('Sparql', 'D-BFS'))

plt.savefig("exp2.png")
plt.savefig("exp2.pdf")