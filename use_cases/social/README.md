# Social use-case:

Nodes: person.

Edges: friendOf (person -> person).

```xml
<graph>
		<nodes>50</nodes>
	</graph>
	<predicates>
		<size>1</size>

		<alias symbol="0">friendOf</alias>

	</predicates>
	<types>
		<size>1</size>
		<alias type="0">person</alias>
		<proportion type="0">1</proportion>

	</types>
	<schema>
		<source type="0"> <!-- person -->
			<target type="0" symbol="0" > <!-- friendOf person -->
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

EGG Evolution properties:

* person: all nodes are valid from the first snapshot to the last one.

* friendOf: can change from invalid to valid but not the contrary.

```json
"validity":{
		"person":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"friendOf":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":"T","F":{"T":0.5,"F":0.5}}},
	}
```
