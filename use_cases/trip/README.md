# Trip use-case:

Nodes: City, Hotel.
Edges: Train (City -> City), contain (City -> Hotel)

EGG evolution properties:

* City : all nodes are valid from the first snapshot to the last one,
    * Weather: can have three values ["sunny","cloudy","rainy"].
    * qAir: describe quality of the air, have 10 values in [1..10], can be influenced by weather.
* Hotel : all nodes are valid from the first snapshot to the last one,
    * star: hotel number of stars, have value in [1,2,3,4,5].
    * availRoom: integer value in [0..100], change every snapshot.
    * hotelPrice: real value, its range depends on star, and the evolution depends on availRoom.
* Train: validity depends on adjacent nodes and distibution ,
    * trainPrice: real value, evolve freely in the range defined in the configuration. 
* contain: all edges are valid from the first snapshot to the last one
