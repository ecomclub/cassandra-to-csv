#!/bin/bash

if [ "$4" = "import" ]; then
 echo "COPY "$1"."$2" FROM '"$3"' WITH HEADER = TRUE ;"| cqlsh
else
 echo "COPY "$1"."$2" TO '"$3"' WITH HEADER = TRUE ;" | cqlsh
fi
