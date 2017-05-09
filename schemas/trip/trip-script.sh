#/bin/bash

#cd "/Users/mac/Desktop/code/EGG/schemas/trip"
cd "/Users/mac/Desktop/code/EGG/schemas/trip"



mkdir -p "byobject"

mkdir -p "byproperty"

rm "egg.log"

python "../../main.py" "trip" --log


# no decimals for values for star property
# plot min, max values for uniform
# plot avg for Gaussian
# voir legende cf. plot1.py
# stacked histogram for discrete unordered properties e.g., weather
# voir TODOs in plot2.py
# fusioner les deux fonctions de plot2.py
# byobject -> histograms for weather : same size, color varies (using same color codes as in stacked histograms)
# a bit of space between the vertical plots
# play with probabilities to see stronger corelation between hotelPrice and availRooms

# fork gmark and prune everything that is not necessary (query workload generator, query translator, query interface...), keep only graph generator

# start preparing scalability scripts (run both gmark and egg)
