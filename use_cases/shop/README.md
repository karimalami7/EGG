# Shop use case:

Nodes: Product, Offer, Country.

Edges: offer_includes (Offer --> Product), eligi_region (Offer --> Country).

```xml
<types>
		<size>3</size>

		<alias type="0">Product</alias>
		<proportion type="0">0.1</proportion>

		<alias type="1">Offer</alias>
		<proportion type="1">0.85</proportion>

		<alias type="2">Country</alias>
		<fixed type="2">0.5</fixed>
	</types>

	<predicates>
		<size>2</size>
		<alias symbol="0">offer_includes</alias>
		<alias symbol="1">eligi_region</alias>
	</predicates>

	<schema>
		<source type="1"> <!-- Offer -->
			<target type="0" symbol="0" multiplicity="1"> <!-- Product -->
				<indistribution type="uniform">
					<min>1</min>
					<max>1</max>
				</indistribution>
				<outdistribution type="uniform">
					<min>1</min>
					<max>10</max>
				</outdistribution>
			</target>
			<target type="2" symbol="1" multiplicity="*"> <!-- Country -->
				<indistribution type="uniform">
					<min>1</min>
					<max>15</max>
				</indistribution>
				<outdistribution type="uniform">
					<min>1</min>
					<max>2</max>
				</outdistribution>
			</target>
		</source>
	</schema>
```

EGG evolution properties:

Validity of nodes and edges:

```json
	"validity":{
		"Product":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":"T","F":{"T":0.5,"F":0.5}},"max":{"T":10}},
		"Offer":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
		"Country":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"offer_includes":{"type":"edge","init":{"T"},"succ":{"T":"T","F":"T"}},
		"eligi_region":{"type":"edge","init":{"T"},"succ":{"T":"T","F":"T"}},
	}
```

* Offer: has one evolving property "discount", which is qualitative with order and has values in [10,20,30,40,50,60,70,80].

```json
"discount":
		{		
			"element":"node",
			"elements_type":"Offer",
			"domain":{
				"type":"qualitatif",
				"order":"true",
				"v":"true",
				"values":["10","20","30","40","50","60","70","80"],
				"distribution":{"type":"uniform"}
			},
			"duration":1,
			"evolution":{
				"e":"true",
				"staticity":1,
			},
			"rules":[],
			"rulese":[]
		}
```

* Product: has two evolving properties:

  * productType: is qualitative with order, it describes the type of the product and has values in ["book","music","movie"]. 
  
  ```json
  "type_product":
		{		
			"element":"node",
			"elements_type":"Product",
			"domain":{
				"type":"qualitatif",
				"order":"false",
				"v":"true",
				"values":["book","music","movie"],
				"distribution":{"type":"uniform"}
			},
			"duration":1,
			"evolution":{
				"e":"true",
				"staticity":1,
				"succesors":{}
			},
			"rules":[],
			"rulese":[]
		}
  ```
  
  
  * productPrice: is quantitative continuous property, it is ruled by *productType*, as the range of price differ from a product type to another.

  ```json
  "productPrice":
		{		
			"element":"node",
			"elements_type":"Product",
			"domain":{
				"type":"quantitatif:con",	
				"v":"false",
				"distribution":{"type":""}
			},
			"duration":1,
			"evolution":{
				"e":"false",
				"staticity":1,
			},
			"rules":[
				{"if":{"prop":"type_product","hasValues":["book"]},"then":{"prop":"productPrice","config":{"domain":{"values":{"min":5,"max":50},"distribution":{"type":"uniform"}},"evolution":{"e":"false","staticity":1}}}},
				{"if":{"prop":"type_product","hasValues":["music"]},"then":{"prop":"productPrice","config":{"domain":{"values":{"min":10,"max":20},"distribution":{"type":"uniform"}},"evolution":{"e":"false","staticity":1}}}},
				{"if":{"prop":"type_product","hasValues":["movie"]},"then":{"prop":"productPrice","config":{"domain":{"values":{"min":25,"max":60},"distribution":{"type":"uniform"}},"evolution":{"e":"false","staticity":1}}}},
			],
			"rulese":[]
		}
  ```
