# System evaluation

System evaluation aims to evaluate Historical Reachibility queries using **EGG** output.

As described in [system evalution wiki](https://github.com/karimalami7/EGG/wiki/System-Evaluation:-Historical-Reachability-Queries), we have implemented two approches for this type of queries and run them against *social* use case.

To run Disjunctive_BFS, please follow the steps below.

1. modify the query size in [Dis-BFS-limited_length.py](https://github.com/karimalami7/EGG/blob/master/demo/system_evaluation/Dis-BFS-limited_length.py)

      i = "list of bits with size equal to # of snapshots of the evolving graph"

2. run the script by mentioning the use case, # of snapshots of the evolving graph, source node, target node, max depth:

  ```shell
  python Dis-BFS-limited_length.py "use-case" "# of snapshots" "source node" "target node" "max depth" 
  ```
To run SPARQL script, please follow the steps below:

1. define the source node and the target node in the script file

  ```sparql
  GRAPH ?x {<source node> predicate <target node> }}
  ```
2. call SPARQL engine and mention the evolving graph rdf file and the SPARQL script

  ```shell
  sparql --query His_Reach_social_sparql --data ../"use case"_output/"use case"_output.trig
  ```
