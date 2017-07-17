# Dblp use-case:

Nodes: author.

Edges: coauthor (author -> author).

```xml
<graph>
		<nodes>50</nodes>
	</graph>
	<predicates>
		<size>1</size>

		<alias symbol="0">coauthor</alias>

	</predicates>
	<types>
		<size>1</size>
		<alias type="0">author</alias>
		<proportion type="0">1</proportion>

	</types>
	<schema>
		<source type="0"> <!-- author -->
			<target type="0" symbol="0" > <!-- co-author author -->
				<indistribution type="gaussian">
					<mu>3</mu>
					<sigma>1</sigma>
				</indistribution>	
				<outdistribution type="uniform">
					<min>0</min>
					<max>6</max>
				</outdistribution>
			</target>
		</source>
	</schema>
```

EGG evolution properties:

* author: can become valid after being invalid, but not the contrary.

* coauthor: validity depends on probability defined in the configuration,

    *  #_of_publications: integer value, defines the number of publications between the two authors, depends on previous value.

```json
"validity":{
		"author":{"type":"node","init":{"F"},"succ":{"F":{"T":0.5,"F":0.5},"T":"T"}},
		"coauthor":{"type":"edge","init":{"T"},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
	},
   
   "num_publi":
		{		
			"element":"edge",
			"elements_type":"coauthor",
			"domain":{
				"type":"quantitatif:dis",
				"v":"true",
				"values":{"min":0,"max":10},
				"distribution":{"type":"binom","p":0.4}
			},
			"duration":1,
			"evolution":{
				"e":"true",
				"relation":"true",
				"staticity":0.7,
				"offset":{
					"min":-1,
					"max":1,
					"distribution":{"type":"binom","p":0.5}
				}
			}
```
