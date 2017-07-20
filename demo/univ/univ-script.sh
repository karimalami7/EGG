#/bin/bash

######## gmark execution

mkdir "../univ_output"

../../gmark/src/test -c ../../use_cases/univ/univ.xml -g ../univ_output/univ-graph.txt -r ../univ_output/ -a


######## egg exection

mkdir -p "../univ_output/byobject"

mkdir -p "../univ_output/byproperty"

rm "../egg.log"

rm "../univ_output/univ-output.trig"

python "../../src/main.py" "univ" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject