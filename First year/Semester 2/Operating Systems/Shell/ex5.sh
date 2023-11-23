#  find files with a specified extension in the current directory and its subdirectories, checks if 
# each file has an odd word count and contains no even digits, and if so, prints their permission mode and name


#!/bin/bash

if test $# -ne 1; then
        echo "Enter one argument representing a file extension"
        exit 1
fi

if test ! "$(find . -name "*$1")"; then
        echo "There is no file with that extension"
        exit 1
fi

for F in `find . -name "*$1"`; do
        W=`wc -w $F | cut -d ' ' -f1`
        if test `expr $W % 2` -eq 1 && test ! `grep -q -E "[0-9]*[02468]" $F`; then
                ls -l "$F" | awk '{print $1, $9}'
        fi
done
