#!/bin/bash

if test $# -eq 0; then
        echo "Enter some words"
        exit 1
fi

while true; do
        echo "Enter a file name"
        read F
        if test ! -f "$F"; then
                echo "Enter a valid file"
        else
                OK=0
                for word in $@; do
                        if test `grep -E -c "\<$word\>" $F` -eq 0; then
                                OK=1
                        fi
                done
                if test $OK -eq 0; then
                        break
                fi
        fi
done
