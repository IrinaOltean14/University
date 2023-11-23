#!/bin/bash

average=0
files=0
lines=0

for F in `find . -type f -name "*.sh"`; do
        N=`grep -E -vc "^$|^[ ]*$" $F`
        files=`expr $files + 1`
        lines=`expr $lines + $N`
done

average=`expr $lines / $files`
echo $average
