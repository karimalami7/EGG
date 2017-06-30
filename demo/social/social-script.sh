#/bin/bash

######## gmark execution


../../gmark/src/test -c ../../use_cases/social/social.xml -g social-graph.txt -r ./ -a


######## egg exection

mkdir -p "byobject"

mkdir -p "byproperty"

rm "egg.log"

python "../../src/main.py" "social" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject
