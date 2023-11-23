#!/bin/bash

#Find recursively in a directory all ".c" files having more than 500 lines.
# Stop after finding 2 such files.
count=0
for F in `find dir -type f -name "*.c"`; do
        if test `wc -l $F | cut -d ' ' -f 1` -ge 500; then
                echo $F
                count=`expr $count + 1`
                if test $count -eq 2; then
                        break
                fi
        fi
done
