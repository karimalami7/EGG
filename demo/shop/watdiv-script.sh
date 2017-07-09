#/bin/bash

######## gmark execution

mkdir "../shop_output"

../../gmark/src/test -c ../../use_cases/shop/shop.xml -g ../shop_output/shop-graph.txt -r ../shop_output/ -a


######## egg exection

mkdir -p "../shop_output/byobject"

mkdir -p "../shop_output/byproperty"

rm "../egg.log"

python "../../src/main.py" "shop" --log   --vg-output --rdf-output --plot-byproperty --plot-byobject