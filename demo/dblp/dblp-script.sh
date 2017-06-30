#/bin/bash

######## gmark execution

../../gmark/src/test -c ../../use_cases/dblp/dblp.xml -g dblp-graph.txt -r ./ -a


######## egg exection

mkdir -p "byobject"

mkdir -p "byproperty"

rm "egg.log"

python "../../src/main.py" "dblp" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject
