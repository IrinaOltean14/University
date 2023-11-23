#!/bin/bash

# Consider a file containing a username on each line. Generate a comma-separated string with email addresses4
# of the users that exist. The email address will be obtained by appending "@scs.ubbcluj.ro" at the
# end of each username. Make sure the generated string does NOT end in a comma.

`sed "s/^\(.*\)/\1@scs.ubbcluj.ro/" ex7.txt > dup.txt`

string=""
while read line; do
        if test ${#string} -ne 0; then
                string+=", "
        fi
        string+=$line
done < dup.txt
