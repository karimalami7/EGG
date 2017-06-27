#/bin/bash

#cd "/Users/mac/Desktop/code/EGG/schemas/trip"




mkdir -p "byobject"

mkdir -p "byproperty"

rm "egg.log"

python "../../src/main.py" "social" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject
