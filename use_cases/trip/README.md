# Trip use-case:

The trip schema is for generating graphs simulating a geographical database, that store information about cities, and different facilities such as transportation and hotels. 

For generating the static graph by gMark, we need to indicate size of the graph (number of nodes), node types, edge predicates, proportion of each node type, and distribution of the triple: node -- edge --> node.

For our example, we want 50 nodes, 10% cities, and 90% hotels. We want a predicate "train" that links a node city to an other node city, and a predicate "contains",that links a node city to a node hotel. This is described in the following xml from the gMark configuration file.

'''xml
<graph>
		<nodes>50</nodes>
	</graph>
	<predicates>
		<size>2</size>

		<alias symbol="0">train</alias>
		<alias symbol="1">contains</alias>

	</predicates>
	<types>
		<size>2</size>
		<alias type="0">city</alias>
		<proportion type="0">0.1</proportion>

		<alias type="1">hotel</alias>
		<proportion type="1">0.9</proportion>

	</types>

'''

Nodes: City, Hotel.

Edges: Train (City -> City), contain (City -> Hotel)

EGG evolution properties:

* City : all nodes are valid from the first snapshot to the last one,
    * Weather: can have three values ["sunny","cloudy","rainy"].
    * qAir: describe quality of the air, have 10 values in [1..10], can be influenced by weather.

* Hotel : all nodes are valid from the first snapshot to the last one,
    * star: hotel number of stars, have value in [1,2,3,4,5].
    * availRoom: integer value in [0..100], change every snapshot.
    * hotelPrice: real value, its range depends on star, and the evolution depends on availRoom.

* Train: validity depends on adjacent nodes and distibution ,
    * trainPrice: real value, evolve freely in the range defined in the configuration. 

* contain: all edges are valid from the first snapshot to the last one
