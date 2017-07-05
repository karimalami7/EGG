#/bin/bash

######## gmark execution

mkdir "../trip_output"

../../gmark/src/test -c ../../use_cases/trip/trip.xml -g ../trip_output/trip-graph.txt -r ../trip_output/ -a


######## egg exection

mkdir -p "../trip_output/byobject"

mkdir -p "../trip_output/byproperty"

rm "../egg.log"

python "../../src/main.py" "trip" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject