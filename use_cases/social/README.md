# Social Use Case 

All nodes are of type *person* and all edge predicates are of type *friendOf* (connecting two persons).

```xml
<types>
	<size>1</size>
	<alias type="0">person</alias>
	<proportion type="0">1</proportion>
</types>
<predicates>
	<size>1</size>
	<alias symbol="0">friendOf</alias>
</predicates>
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

In this use case, we assume that a snapshot correspond to a day. The EGG evolving properties are as follows:

* Validity of nodes *person*: all nodes are valid from the first snapshot to the last one.

* Validity of edges *friendOf*: at the beggining, each edge has 50% probability to be valid. Then, if an edge is invalid, it has 50% probability to become valid in the next snapshot. Once an edge becomes valid, it remains valid until the last snapshot.

```json
"validity":{
		"person":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"friendOf":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":"T","F":{"T":0.5,"F":0.5}}},
	}
```
