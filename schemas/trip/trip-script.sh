#/bin/bash

#cd "/Users/mac/Desktop/code/EGG/schemas/trip"




mkdir -p "byobject"

mkdir -p "byproperty"

rm "egg.log"

python "../../main.py" "trip" --plot-byobject --plot-byproperty --rdf-output --log

# no decimals for values for star property   *** ne depend pas de la valeur de la propriete
# plot min, max values for uniform   ***   put min max for discrete properties ***done
# plot avg for Gaussian  ***done
# voir legende cf. plot1.py ***done
# stacked histogram for discrete unordered properties e.g., weather
# voir TODOs in plot2.py   ***done
# fusioner les deux fonctions de plot2.py ***done
# byobject -> histograms for weather : same size, color varies (using same color codes as in stacked histograms) ***done
# a bit of space between the vertical plots *** done



# play with probabilities to see stronger corelation between hotelPrice and availRooms

# fork gmark and prune everything that is not necessary (query workload generator, query translator, query interface...), keep only graph generator ***done

# start preparing scalability scripts (run both gmark and egg)  ***done
