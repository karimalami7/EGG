# EGG: Evolving Graph Generator

An open-source project for generating evolving graphs.

The generation is driven by finely tuned constraint and parameters. It uses [gMark](https://github.com/karimalami7/gmark/tree/gmark_for_egg) to generate static graphs.

The EGG repository is organised as follow:

* src/: directory of source code of EGG.

* use-cases/: one directory for each scenario, where we put gMark schema and EGG configuration.

* demo/: 

  * For every scenario:  script to run EGG and directory of its ouputs.
  
  * Scalability: script to evaluate scalability of EGG. More informations in [EGG scalability wiki](https://github.com/karimalami7/EGG/wiki/EGG-scalability).
  
  * System evaluation: informations in the [system evaluation wiki](https://github.com/karimalami7/EGG/wiki/System-Evaluation:-Historical-Reachability-Queries).

To begin working with EGG, please run the [requirement](https://github.com/karimalami7/EGG/blob/master/demo/scripts/requirement.sh) script, it checks and installs all software needed to run EGG.

Then feel free to modify gMark schema and EGG configuration in [play](https://github.com/karimalami7/EGG/tree/master/use_cases/play) scenario.

The final step, is to run EGG for this scenario by specifying the outputs you want in [play script](https://github.com/karimalami7/EGG/blob/master/demo/play/play-script.sh):

* RDF output: serialization of the evolving graph in RDF.

* VG output: serialization of the evolving graph in version graph format.

* Plot by property: generate evolution plots of all properties defined in the EGG configuration.

* Plot by object: generate evolution plots for properties of nodes and edges.  



