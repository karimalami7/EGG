#/bin/bash

######## gmark execution

mkdir "../play_output"

../../gmark/src/test -c ../../use_cases/play/play.xml -g ../play_output/play-graph.txt -r ../play_output/ -a


######## egg exection

mkdir -p "../play_output/byobject"

mkdir -p "../play_output/byproperty"

rm "../egg.log"

python "../../src/main.py" "play" --log   
