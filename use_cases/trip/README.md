# Trip use-case:

The trip schema is for generating graphs simulating a geographical database, that store information about cities, and different facilities such as transportation and hotels. 

For generating the static graph by gMark, we need to indicate size of the graph (number of nodes), node types, edge predicates, proportion of each node type, and distribution of the triple: *node -- edge --> node*.

For our example, we want 50 nodes, 10% cities, and 90% hotels. We want a predicate *train* that links a node *city* to an other node *city*, and a predicate *contains*, that links a node *city* to a node *hotel*. This is described in the following xml from the gMark configuration file.

```xml
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
```

Then, we need to indicate distribution of each relation described bofore. So, for the relation *city -- train --> city*, we want for the in distribution a gaussian distribution with mean=3 and std=1, and for the out distribution, a uniform distribution with maximum and minimum set to 1, in order to have one *train* predicate that goes out from a node *city*, and possibly, multiple ones that go in. For the relation *city -- contains --> hotel*, we put for the out distribution, the zipfian distribution, and for the in distribution, uniform distribution with maximum and minimum set to 1, in order to link few cities to a big number of hotels, to link a big number of cities to few hotels, and to link each hotel to only one city. The following xml encodes such configuration.

```xml
	<schema>
		<source type="0"> <!-- city -->
			<target type="0" symbol="0" > <!-- train city -->
				<indistribution type="gaussian">
					<mu>3</mu>
					<sigma>1</sigma>
				</indistribution>	
				<outdistribution type="uniform">
					<min>1</min>
					<max>1</max>
				</outdistribution>
			</target>
			<target type="1" symbol="1"  > <!-- contains hotel -->
				<indistribution type="uniform">
					<min>1</min>
					<max>1</max>
				</indistribution>
				<outdistribution type="zipfian">
					<alpha>0.9</alpha>
				</outdistribution>
			</target>
		</source>
	</schema>
```

> **NOTE**: Satisfying some distribution can be a very long process for large graphs. So, in order to have a fast response from gMark for large graphs, make sure that distributions are reasonable.



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
