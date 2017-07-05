#/bin/bash

######## gmark execution

mkdir "../social_output"

../../gmark/src/test -c ../../use_cases/social/social.xml -g ../social_output/social-graph.txt -r ../social_output/ -a


######## egg exection

mkdir -p "../social_output/byobject"

mkdir -p "../social_output/byproperty"

rm "../egg.log"

python "../../src/main.py" "social" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject
