#!/bin/bash

if [ "$4" = "import" ]; then
  # csv -> cassandra
  echo "COPY "$1"."$2" FROM '"$3"' WITH HEADER = TRUE ;" | cqlsh
else
  # default
  # cassandra -> csv
  echo "COPY "$1"."$2" TO '"$3"' WITH HEADER = TRUE ;" | cqlsh
fi
