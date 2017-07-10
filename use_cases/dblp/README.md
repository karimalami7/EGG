# Dblp use-case:

Nodes: author.

Edges: coauthor (author -> author).

EGG evolution properties:

* author: can become valid after being invalid, but not the contrary.

* coauthor: validity depends on probability defined in the configuration,

    *  #_of_publications: integer value, defines the number of publications between the two authors, depends on previous value.
