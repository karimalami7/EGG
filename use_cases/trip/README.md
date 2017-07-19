# Trip Use Case

The **trip** use case is useful for generating graphs simulating a geographical database, which stores information about cities and different facilities such as transportation and hotels. 

For generating the static graph by gMark, we need to indicate size of the graph (number of nodes), node types, edge predicates, proportion of each node type, and distribution of the triple: *(source node type, edge predicate, target node type)*.

For example, the following snippet of a gMark configuration file generates a static graph having 50 nodes, out of which 10% are cities and 90% are hotels. 
Moreover, we want an edge predicate *train* (that links a node *city* to an other node *city*) and an edge predicate *contains*
(that links a node *city* to a node *hotel*). 

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

Then, we indicate degree distributions for each triple *(source node type, edge predicate, target node type)*.
For example, the following snippet specifies that an edge of type *contains* from a node of type *city* to a node of type *hotel* follows a Zipfian out-distribution (since it is realistic to assume that the number of hotels in a city follows such a power-law distribution) and a uniform [1,1] in-distribution (since a hotel is located in precisely one city).

```xml
	<schema>
		<source type="0"> <!-- city -->
			<target type="1" symbol="1"  > <!-- contains hotel -->
				<indistribution type="uniform">
					<min>1</min>
					<max>1</max>
				</indistribution>
				<outdistribution type="zipfian">
					<alpha>0.9</alpha>
				</outdistribution>
			</target>
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
		</source>
	</schema>
```

In the *EGG* evolving graph configuration, we indicate the number of snapshots (for this example we assume that a snapshot is a day), and we describe validity and evolution rules for evolving properties. 

For our example, we want the nodes of type *city* and *hotel*, and the edges of type *contains* to be valid in all snapshots, but we want that the validity of the edge type *train* evolves randomly. 
Intuitively, this is to encode that a train connection between two cities may not be valid during all snapshots.
This is done with the following code:

```json
"validity":{
		"city":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"hotel":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"train":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
		"contains":{"type":"edge","init":{"T"},"succ":{"T":"T"}}
```

We defined six evolving properties: _**weather**_ and _**qAir**_ for the node type *city*, _**star**_, _**availableRooms**_, and _**hotelPrice**_ for the node type *hotel*, and _**trainPrice**_ for the edge type *train*.

An evolving property has one of the following types: unordered qualitative, ordered qualitative, discrete quantitative, continuous quantitive.

We begin by *weather* property for the node type *city*. It is an unordered qualitative property, which can have 3 values: sunny, cloudy, rainy.
It can change with 50% probability, and we define one succession rule that is: a city with weather sunny at a snapshot i cannot be rainy at snapshot i+1. 

```json
		"weather":
		{		
			"element":"node",
			"elements_type":"city",
			"domain":{
				"type":"qualitatif",
				"order":"false",
				"v":"true",
				"values":["sunny","rainy","cloudy"],
				"distribution":{"type":"uniform"}
			},
			"duration":1,
			"evolution":{
				"e":"true",
				"staticity":0.5,
				"succesors":{"sunny":["sunny","cloudy"]}
			},
			"rules":[],
			"rulese":[]
		}
```

*qAir* is an ordered property for the node type *city*, which has ten possible values corresponding to integers between 1 and 10. 

There is a probability of 80% that qAir does not change from a snapshot to the next one, hence 20% to change.
Moreover, it can only increment or decrement by 1 between two consecutive snapshots.
There are 3 evolution rules where the change of *qAir* depends on the change of *weather* e.g., when *weather* of a node x changes from cloudy to sunny, then *qAir* of node x increases.

```json
		"qAir":
		{
			"element":"node",
			"elements_type":"city",
			"domain":{
				"type":"qualitatif",
				"order":"true",
				"v":"true",
				"values":["1","2","3","4","5","6","7","8","9","10"],
				"distribution":{"type":"binom","p":0.6}
			},
			"duration":7,
			"evolution":{
				"e":"true",
				"staticity":0.8,
				"offset":{
					"min":-1,
					"max":1,
					"distribution":{"type":"uniform"}
				}
			},
			"rules":[],
			"rulese":[
				{"if":{"prop":"weather","change":["cloudy","sunny"]},"then":{"prop":"qAir","sens":"up"}},
				{"if":{"prop":"weather","change":["rainy","sunny"]},"then":{"prop":"qAir","sens":"up"}},
				{"if":{"prop":"weather","change":["sunny","cloudy"]},"then":{"prop":"qAir","sens":"down"}}
			]

```

The evolving property *availableRooms* of the node type *hotel* is discrete quantitative, with values in the interal [1,100]. 
It always changes between two consecutive snapshots, and it can increment or decrement by an integer up to 5 (drawn according to a binomial distribution centered in 0).

```json
		"availableRooms":
		{
			"element":"node",
			"elements_type":"hotel",
			"domain":{
				"type":"quantitatif:dis",
				
				"v":"true",
				"values":{"min":1,"max":100},
				"distribution":{"type":"binom","p":0.5}
			},
			"duration":1,
			"evolution":{
				"e":"true",
				"staticity":0,
				"offset":{
					"min":-5,
					"max":5,
					"distribution":{"type":"binom","p":0.5}
				}
			},
			"rules":[],
			"rulese":[]
			
		}
```

The evolving property *star* of the node type *hotel* is ordered qualitative, with values in the list [1,2,3,4,5], following a geometric distribution. It can change every thirty snapshots with a probability of 1% and move by one position in the list.

```json
"star":
		{	
			"element":"node",
			"elements_type":"hotel",
			"domain":{
				"type":"qualitatif",
				"order":"true",
				"v":"true",
				"values":["1","2","3","4","5"],
				"distribution":{"type":"geom","p":0.65}
			},
			"duration":30,
			"evolution":{
				"e":"true",
				"staticity":0.9,
				"offset":{
					"min":-1,
					"max":1,
					"distribution":{"type":"binom","p":0.5}
				}
			},
			"rules":[],
			"rulese":[]
			
		}
```
The evolving property *hotelPrice* of the node type *city* is continuous quantitative. It is the most complex property of this use case as it depends both on *star* for its domain and *availableRomms* for its evolution. 
More precisely, to compute *hotelPrice* for a node x, we need to construct its domain depending on its *star* value. 
Hence, we need to define in the configuration, for each *star* value, the interval of *hotelPrice* values and the offset of the evolution.
Moreover, *hotelPrice* depends on *availableRooms* in the sense that these two properties are anti-correlated: if *availableRooms* increases, then *hotelPrice* decreases, and vice-versa. 

```json
		"hotelPrice":
		{		
			"element":"node",
			"elements_type":"hotel",
			"domain":{
				"type":"quantitatif:con",	
				"v":"false",
				"distribution":{"type":""}
			},
			"duration":1,
			"evolution":{
				"e":"false",
				"staticity":0,
			},
			"rules":[
				{"if":{"prop":"star","hasValues":["1"]},"then":{"prop":"hotelPrice","config":{"domain":{"values":{"min":10,"max":20},"distribution":{"type":"normal","mean":15,"sigma":1}},"evolution":{"offset":{"min":-1,"max":1,"distribution":{"type":"normal","mean":0,"sigma":0.5}}}}}},
				{"if":{"prop":"star","hasValues":["2"]},"then":{"prop":"hotelPrice","config":{"domain":{"values":{"min":21,"max":50},"distribution":{"type":"normal","mean":35,"sigma":4}},"evolution":{"offset":{"min":-3,"max":3,"distribution":{"type":"normal","mean":0,"sigma":1}}}}}},
				{"if":{"prop":"star","hasValues":["3"]},"then":{"prop":"hotelPrice","config":{"domain":{"values":{"min":51,"max":100},"distribution":{"type":"normal","mean":75,"sigma":8}},"evolution":{"offset":{"min":-7,"max":7,"distribution":{"type":"normal","mean":0,"sigma":3}}}}}},
				{"if":{"prop":"star","hasValues":["4"]},"then":{"prop":"hotelPrice","config":{"domain":{"values":{"min":101,"max":300},"distribution":{"type":"normal","mean":200,"sigma":20}},"evolution":{"offset":{"min":-20,"max":20,"distribution":{"type":"normal","mean":0,"sigma":7}}}}}},
				{"if":{"prop":"star","hasValues":["5"]},"then":{"prop":"hotelPrice","config":{"domain":{"values":{"min":301,"max":1000},"distribution":{"type":"normal","mean":650,"sigma":65}},"evolution":{"offset":{"min":-50,"max":50,"distribution":{"type":"normal","mean":0,"sigma":20}}}}}}
			],
			"rulese":[
				{"if":{"prop":"availableRooms","sens":"down"},"then":{"prop":"hotelPrice","sens":"up"}},
				{"if":{"prop":"availableRooms","sens":"up"},"then":{"prop":"hotelPrice","sens":"down"}}
			]
		}
```

The evolving property *trainPrice* of the edge prdicate *train* is continuous quantitative with values in the interval [20,100], following a normal distribution centered in 60. It can change every day with 30% probability, with an offset[-10,10] following a normal distribution centered in 0.

```json
		"trainPrice":
		{		
			"element":"edge",
			"elements_type":"train",
			"domain":{
				"type":"quantitatif:con",
				
				"v":"true",
				"values":{"min":20,"max":100},
				"distribution":{"type":"normal","mean":60,"sigma":6}
			},
			"duration":1,
			"evolution":{
				"e":"true",
				"staticity":0.7,
				"offset":{
					"min":-10,
					"max":10,
					"distribution":{"type":"normal","mean":0,"sigma":3}
				}
			},
			"rules":[],
			"rulese":[]
			
		}
```
