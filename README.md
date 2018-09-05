# cassandra-to-csv
Python script to parse Cassandra table data to CSV

# Technology stack
+ [Python 2](https://www.python.org/downloads/release/python-2715/) 
+ [PIP](https://pypi.org/project/pip/)
+ [Casandra drive](https://datastax.github.io/python-driver/) 

# Setting up
Installing dependencies on RHEL based Linux:
```bash
sudo yum install python27 python27-devel python-pip
pip install cassandra-driver
```

## Running the script
```bash
python cassandra_to_csv.py keyspace table
```
