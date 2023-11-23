#!/bin/bash

files=0
size_of_files=0
directories=0
for argument in $@ ; do
        if test -f $argument ; then
                echo "Argument is a file"
                files=`expr $files + 1`
                size=`ls -l $argument | awk '{ print $5 }'`
                size_of_files=`expr $size_of_files + $size`
        elif test -d $argument ; then
                echo "Argument is a directory"
                directories=`expr $directories + 1`
                M=`ls -ld $argument | awk '{ print $1}' | grep -c "x"`
                if test $M -eq 1 ; then
                        echo $argument
                fi
        elif test `echo $argument | grep -E -c "^[0-9]+$"` -eq 1 ; then
                echo "Argument is a number"
                echo $argument >> mynumbers.txt
        fi
done
echo "The size occupied by the files is: " $size_of_files
cat mynumbers.txt
