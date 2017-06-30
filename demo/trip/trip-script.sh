#/bin/bash

######## gmark execution


../../gmark/src/test -c ../../use_cases/trip/trip.xml -g trip-graph.txt -r ./ -a


######## egg exection

mkdir -p "byobject"

mkdir -p "byproperty"

rm "egg.log"

python "../../src/main.py" "trip" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject
