# System Evaluation

To emphasize the ease of realizing empirical evaluations on top of **EGG**, we present a performance comparison
of approaches for answering historical reachability queries, a problem introduced in the article [**TimeReach: Historical Reachability Queries on Evolving Graphs**](http://openproceedings.org/2015/conf/edbt/paper-89.pdf).

As described in the [system evalution wiki](https://github.com/karimalami7/EGG/wiki/System-Evaluation:-Historical-Reachability-Queries), we have implemented two approches for this query paradigm and run them against *social* use case, which is actually inspired by the datasets used in the aforementioned TimeReach paper.

To run Disjunctive-BFS, please do the following steps.

1. in [Dis-BFS-limited_length.py](https://github.com/karimalami7/EGG/blob/master/demo/system_evaluation/Dis-BFS-limited_length.py), fix the interval in which we look for a snapshot where the input nodes are connected.
This should be encoded in the variable *i* as a bit vector e.g., *i=[00011110]* to encode the interval [3,6] in a case with a total of 8 snapshots.


2. run the script with the following parameters: the use case, # of snapshots of the evolving graph, source node, target node, max depth:

  ```shell
  python Dis-BFS-limited_length.py "use-case" "# of snapshots" "source node" "target node" "max depth" 
  ```
To run SPARQL, please do the following steps:

1. define the source node and the target node in the [SPARQL script file](https://github.com/karimalami7/EGG/blob/master/demo/system_evaluation/His_Reach_social_sparql)

  ```sparql
  GRAPH ?x {<source node> predicate <target node> }}
  ```
2. call the SPARQL engine while giving as parameters the SPARQL script and the RDF file encoding the evolving graph

  ```shell
  sparql --query His_Reach_social_sparql --data ../"use case"_output/"use case"_output.trig
  ```
