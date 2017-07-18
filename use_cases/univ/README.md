# Univ use case

Nodes: University, Professor, Student, Course.

Edges: has_course (University --> Course), teaches_course(Professor --> Course), takes_course (Student --> Course).

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

For this example, we consider snapshots as semesters

* Validity of nodes and edges

	* Universites are always valid. 
 	* Professor become valid and and teaches somes courses.
	* Students become valid for six snapshots only.
	* Courses are always valid and linked to a university
	
```json
"validity":{

		"University":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"Professor":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":"T","F":{"T":0.5,"F":0.5}}},
		"Student":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":1,"F":0},"F":{"T":0.5,"F":0.5}},"max":{"T":6}},
		"Course":{"type":"node","init":{"T"},"succ":{"T":"T"}},

		"teaches_course":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
		"has_course":{"type":"edge","init":{"T"},"succ":{"T":"T","F":"T"}},
		"takes_course":{"type":"edge","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
	}
```

There is no evolving property for this use case.
