# DBLP Use Case

All nodes are of type *author* and all edges are of type *coauthor* (connecting two authors).

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

In this use case, we assume that a snapshot corresponds to a year.
The **EGG** evolving properties are as follows:

* validity of *author* nodes: at the beginning, we assume that no author is valid (intuitively, at year 0 no author is yet active) and between two consecutive years there is 50% probability that an author becomes valid (intuitively, new authors appear every year). Once an author becomes valid, it remains valid until the end of time.

* validity of *coauthor* edges: it is similar to the aforementioned evolving property, except that after becoming valid, a *coauthor* edge may become invalid again (intuitively, two authors may publish together for some years, but stop their collaboration afterwise).

*  property *num_publi* of edge *coauthor*: is an integer defining the number of publications between two authors, which is computed only when the coauthorship between two authors is valid and can evolve according to its rule defined below.

```json
"validity":{
		"author":{"type":"node","init":{"F"},"succ":{"F":{"T":0.5,"F":0.5},"T":"T"}},
		"coauthor":{"type":"edge","init":{"F"},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
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
