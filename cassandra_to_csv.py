
# coding: utf-8

# In[68]:


from  cassandra.cluster  import Cluster 

cluster=Cluster(['127.0.0.1'],port=9042)
session=cluster.connect()

import csv
import sys


# In[69]:



use='USE '
keyspace=sys.argv[1]

print keyspace



session.execute(use +keyspace)


# In[70]:


head=[]
row=session.execute("SELECT * FROM system_schema.columns  WHERE keyspace_name = 'sys.argv[1]' AND table_name = 'sys.argv[2]';")

arg=sys.argv[2]
select='SELECT * FROM '


coluna=session.execute(select +arg  )



# In[71]:


with open('keyspace_metadata.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter='|',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in row:
        head.append(i[2]) 
    filewriter.writerow(head)
    for i in coluna:
        filewriter.writerow(i)
