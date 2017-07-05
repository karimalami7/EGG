#/bin/bash

######## gmark execution

mkdir "../watdiv_output"

../../gmark/src/test -c ../../use_cases/watdiv/watdiv.xml -g ../watdiv_output/watdiv-graph.txt -r ../watdiv_output/ -a


######## egg exection

mkdir -p "../watdiv_output/byobject"

mkdir -p "../watdiv_output/byproperty"

rm "../egg.log"

python "../../src/main.py" "watdiv" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject