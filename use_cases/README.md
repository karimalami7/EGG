# Use Cases:

The evolving graph generator is driven by a user configuration that describes the static and dynamic properties of the evolving graph.

![](../egg-architecture.png)

As shown in the figure above, we need to indicate the static graph configuration that is the input of **gMark**, and the evolving graph configuration that is the input of **EGG**.

During conception and developpement of EGG, we worked with the use-case Trip, which is a geographical database that match cities and hotels.

The trip use case includes almost all evolution characteristics that EGG can handle. In the repository use-case of [trip](https://github.com/karimalami7/EGG/tree/master/use_cases/trip), We have put in README details of this characteristics.

We defined also four other schemas:

* dblp: stores authors of articles and co-author relationship between authors. The co-author relationship has a dynamic property *number of publications*, which store number of publications between two authors at each snapshot. 

* social: stores persons as nodes, and friendship relation.

* univ: stores universities, professors, students and courses. Inspired from lubm benchmark.

* shop: stores shops, products and offers. Inspired from watdiv.
