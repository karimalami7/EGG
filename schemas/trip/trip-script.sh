#/bin/bash

cd "/Users/mac/Desktop/code/EGG/schemas/trip"

rm "egg.log"

python "../../main.py" "trip" --plot-byproperty "qAir" --plot-byobject "46"