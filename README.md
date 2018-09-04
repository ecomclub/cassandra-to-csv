# cassandra-to-csv

Service to parse Cassandra table data to CSV

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Technology stack

What things you need to install the software and how to install them

* [Python 2](https://www.python.org/downloads/release/python-2715/) 
* [PIP](https://pypi.org/project/pip/)
* [Casandra drive](https://datastax.github.io/python-driver/) 

### Installing
Intalação python:
```
yum install python27 python27 -devel 
```
Instalação PIP:
```
sudo yum install python-pip
```
Instalação CASANDRA DRIVE:
```
pip install cassandra-driver
```
## Running the tests


```sh
python cassandra_to_csv.py ARG1[KEYSPACE] ARG2[TABLE NAME]
```



