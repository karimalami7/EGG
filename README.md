# EGG

An open-source project for generating evolving graphs.

The generation is driven by finely tuned constraint and parameters. It uses [gMark](https://github.com/karimalami7/gmark/tree/gmark_for_egg) to generate static graphs.

To begin working with EGG, please run the [requirement](https://github.com/karimalami7/EGG/blob/master/demo/scripts/requirement.sh) script, it checks and installs all software needed to run EGG.

Then feel free to modify gMark schema and EGG configuration in [play](https://github.com/karimalami7/EGG/tree/master/use_cases/play) scenario.

The final step, is to run EGG for this scenario by specifying the outputs you want:

* RDF output: serialization of the evolving graph in RDF.

* VG ouput: serialization of the evolving grpah in version graph format.

* Plot by property: generate evolution plots of all properties defined in the EGG configuration.

* Plot by object: generate evolution plots for properties of nodes and edges.  



