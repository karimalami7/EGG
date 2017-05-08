#/bin/bash

cd "/Users/mac/Desktop/code/EGG/schemas/trip"

mkdir "byobject"

mkdir "byproperty"

rm "egg.log"

python "../../main.py" "trip" --plot-byobject --plot-byproperty --rdf-output