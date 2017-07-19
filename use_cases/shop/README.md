# Shop Use Case

The shop use case stores the relation between offers and products in an online shop. It consists of three node types (product, offer, country), and two edge types: offer_includes (links an offer to a product) and eligi_region (links an offer to a country).

```xml
<types>
		<size>3</size>

		<alias type="0">Product</alias>
		<proportion type="0">0.1</proportion>

		<alias type="1">Offer</alias>
		<proportion type="1">0.85</proportion>

		<alias type="2">Country</alias>
		<proportion type="2">0.05</proportion>
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

In this use case, we assume that a snapshot corresponds to a month. The EGG evolving properties are as follows:

* Validity of node type *product*: at the beginning, a node *product* has 50% probability to be valid. When a node *product* becomes valid, it remains valid for 10 snapshots, and then becomes invalid until the last snapshot.
* Validity of node type *offer*: similarly to the validity of node type *product*, except that there is no limit in the number of snapshots where it is valid.
* Validity of node type *country*: valid from the first snapshot to the last one.
* Validity of edge type *offer_includes*: always valid when the adjacent node of type *offer* is valid.
* Validity of edge type *eligi_region*: always valid when the adjacent node of type *offer* is valid.

```json
	"validity":{
		"Product":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":"T","F":{"T":0.5,"F":0.5}},"max":{"T":10}},
		"Offer":{"type":"node","init":{"T":0.5,"F":0.5},"succ":{"T":{"T":0.5,"F":0.5},"F":{"T":0.5,"F":0.5}}},
		"Country":{"type":"node","init":{"T"},"succ":{"T":"T"}},
		"offer_includes":{"type":"edge","init":{"T"},"succ":{"T":"T","F":"T"}},
		"eligi_region":{"type":"edge","init":{"T"},"succ":{"T":"T","F":"T"}},
	}
```

* Evolving property *discount* of node type *offer*: ordered qualitative property with values in [10,20,30,40,50,60,70,80] distributed randomly (it intuitively encodes the percentage of the price that is discounted).
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


* Evolving property *productType* of node type *product*: unordered qualitative property that describes the type of the product and has values in ["book","music","movie"]. 
  
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
  
* Evolving property *productPrice* of node type *product*: continuous quantitative property that defines the price of a product. Its possible values are defined dynamically based on the property *productType* of a node. 

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
