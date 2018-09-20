# cassandra-to-csv
Shell script to import and export Cassandra table data to CSV

## Export
From Cassandra to CSV

```bash
sh cqlcsv.sh keyspace table filepath 
```

## Import
From CSV to Cassandra

```bash
sh cqlcsv.sh keyspace table filepath import
```
