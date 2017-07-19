# Univ use case

The univ use case stores the relation between students, professors, courses, and universities. It consits of four node types (*student*,*professor*,*course*,*university*), and the edge types: *has_course* (connects a university to a course), *teaches_course* (connects a professor to a course) and *takes_course*(connects a student to a course).

```xml
<types>
		<size>4</size>

		<alias type="0">University</alias>
		<proportion type="0">0.05</proportion>

		<alias type="1">Professor</alias>
		<proportion type="1">0.15</proportion>

		<alias type="2">Student</alias>
		<fixed type="2">0.5</fixed>

		<alias type="3">Course</alias>
		<fixed type="3">0.30</fixed>

	</types>

	<predicates>
		<size>3</size>

		<alias symbol="0">has_course</alias>
		<alias symbol="1">teaches_course</alias>
		<alias symbol="2">takes_course</alias>

	</predicates>

	<schema>

		<source type="0"> <!-- University -->
			<target type="3" symbol="0" > <!-- course -->
				<outdistribution type="uniform">
					<min>3</min>
					<max>10</max>
				</outdistribution>
				<indistribution type="uniform">
					<min>1</min>
					<max>1</max>
				</indistribution>
			</target>
		</source>

		<source type="1"> <!-- Professor -->
			<target type="3" symbol="1"> <!-- course -->
				<outdistribution type="uniform">
					<min>1</min>
					<max>2</max>
				</outdistribution>
				<indistribution type="uniform">
					<min>1</min>
					<max>1</max>
				</indistribution>
			</target>
		</source>

		<source type="2"> <!-- Student -->
			<target type="3" symbol="2" > <!-- course -->
				<outdistribution type="uniform">
					<min>1</min>
					<max>10</max>
				</outdistribution>
				<indistribution type="uniform">
					<min>1</min>
					<max>10</max>
				</indistribution>
			</target>
		</source>
	</schema>

```

For this example, we assume that a snapshots correspond to a semester. The **EGG** evolving properties are as follows:

* Validity of node type *university*: valid from the first snapshot to the last one. 
* Validity of node type *professor*: at the beginning, each node has 50% probability to be valid. Once it becomes valid, it remains until the last snapshot. 
* Validity of node type *student*: at the beginning, each node has 50% probability to be valid. Once it becomes valid, it remains valid for six snapshots only.
* Validity of node type *course*: valid from the first snapshot to the last one.
* Validity of edge type *has_course*: valid from the first snapshot to the last one. (A course is always linked to a university).
* Validity of edge type *teaches_course*: at the beginning, each node has 50% probability to be valid. And it has 50% probability to become valid after being invalid, and vice-versa
* Validity of edge type *takes_course*: similar to the validity of edge type *teaches_course*.


```json
"validity":{

		"University":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"Professor":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":"T","F":{"T":0.5,"F":0.5}}},
		"Student":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":{"T"},"F":{"T":0.5,"F":0.5}},"max":{"T":6}},
		"Course":{"type":"node","init":{"T"},"succ":{"T":"T"}},

		"teaches_course":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
		"has_course":{"type":"edge","init":{"T"},"succ":{"T":"T","F":"T"}},
		"takes_course":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
	}
```


