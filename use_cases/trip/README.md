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

In *EGG*, we indicate the number of snapshots, and we describe validity and dynamic properties evolution rules. 

> **NOTE**: We have to define validity evolution rules for each node type and edge predicate.

For our example, we want nodes: *city*, *hotel* and edges: *contains*  to be valid in all snapshots, but we want edge: *train* validity  to evolve randomly. Below, a part of the json configuration: 

```json
"validity":{
		"city":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"hotel":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"train":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
		"contains":{"type":"edge","init":{"T"},"succ":{"T":"T"}}
```

We defined six dynamic properties: _**Weather**_, _**qAir**_ for the node type *city*, _**Star**_, _**AvailableRooms**_, _**hotelPrice**_ for the node type *hotel*, and _**trainPrice**_ for the edge predicate * Train *.

Each property can be: ordered qualitative, unordered qualitative, discrete quantitative, continuous quantitive.

We begin by *weather* property for node type *city*. It is an ordered qualitative property, it can have 3 values: sunny, cloudy, rainy, can change with 50% probability, and we define one succession rule that is a city with weather sunny at a snapshot i, can not be rainy at snapshot i+1. 

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

*qAir* is an ordered property for node type *city*, it has its values in the list [1,2,3,4,5,6,7,8,9,10], the value with the bigger index is bigger. Its value can move by one index in the list with 80% probability. It has 3 rules of evolution where it depends on *weather* change, for example: when *weather* of a node x change from cloudy to sunny, *qAir* of node x becomes better.
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

AvailableRooms is a discrete quantitative for node type "hotel", it has values in the interal [1,100]. It changes each time with an offset within [-5,5] and binomial distribution centered in 0.
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

*Star* is an ordered qualitative property for node type *Hotel*, which have values in the list [1,2,3,4,5], following a geometric distribution. It can change every thirty snapshots with a probability of 1% and move by one position in the list.

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
*hotelPrice* is a continuous quantitative property for node type *city*. It is the most complicated property as it depends on *Star* for its domain and *AvailableRomms* for its evolution. 
In fact, to calculate *hotelPrice* for a node x, we need construct its domain regarding its *star* value. So we need to define in the configuration, for each *star* value, the interval of value of *hotelPrice* and the offset of evolution.
Also, *hotelPrice* depends on *availableRooms* as, if *availableRooms* rise, *hotelPrice* goes down, and if *availableRooms* goes down, *hotelPrice* rise. So the offset is modified, either maximium or minimum is set to 0. 

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
*TrainPrice* is a continuous quantitative property for edge predicate *train*, it has values in [20,100], following a normal distribution centered in 60. It can change every day with 30% probability, with an offset[-10,10] following a normal distribution centered in 0.

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
