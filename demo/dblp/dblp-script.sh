#/bin/bash

######## gmark execution

mkdir "../dblp_output"

../../gmark/src/test -c ../../use_cases/dblp/dblp.xml -g ../dblp_output/dblp-graph.txt -r ../dblp_output/ -a


######## egg exection

mkdir -p "../dblp_output/byobject"

mkdir -p "../dblp_output/byproperty"

rm "../egg.log"

python "../../src/main.py" "dblp" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject