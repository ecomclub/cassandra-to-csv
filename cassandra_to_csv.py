from  cassandra.cluster  import Cluster
import csv
import sys

#cassandra DB connection

cluster=Cluster(['127.0.0.1'],port=9042)
session=cluster.connect()

#Access to Keyspace

keyspace=sys.argv[1]
arg=sys.argv[2]

use='USE '
session.execute(use +keyspace)

#define head

head=[]

row=session.execute(
    """
    SELECT * FROM system_schema.columns  WHERE keyspace_name = %s AND table_name =%s
    """,
    (keyspace,arg)
)


for i in row:
        head.append(i[2])

# convert list in string

result = ', '.join(head)
convert=str(result)


query="SELECT " +"".join(convert)+" FROM "

# data recovery


column=session.execute(query +arg)



# csv data conversion

with open(sys.argv[3], 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter='|',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in row:
        head.append(i[2])
    filewriter.writerow(head)
    for i in column:
        filewriter.writerow(i)
