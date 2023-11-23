#!/bin/bash

# Display a report showing the full name of all the users currently connected,
# and the number of processes belonging to each of them.

for name in `cat who.fake | cut -d ' ' -f1`; do
        M=`grep -c "^$name" ps.fake`
        echo $name $M
done
