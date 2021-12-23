#General for all

import psycopg2 as psc #for integrating SQL with python
from prettytable import from_db_cursor #To get the output as table itself
conn = psc.connect(user="postgres",password="acrimonious",host="localhost",port="8101",database="Exoplanets")
cur = conn.cursor()
records = cur.fetchall()

#To view a table


def select_all(table_name):
    query = "SELECT * FROM " + table_name
    cur.execute(query)
    op = from_db_cursor(cur)
    return op 
print(select_all('star'))


#To see a particular column

t_eff = []
for row in records:
  t_eff.append(row[1]) #[1] represent the column index. Inside a for loop, it becomes the column as rows stackup 
print(t_eff)


#Finding datatype

for col in records[0]:
    print(type(col))


#To make the table a Numpy array
array = np.array(records)

#   
