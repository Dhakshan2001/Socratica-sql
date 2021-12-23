import psycopg2 as psc #for integrating SQL with python
from prettytable import from_db_cursor #To get the output as table itself
import numpy as np
conn = psc.connect(user="postgres",password="acrimonious",host="localhost",port="8101",database="Exoplanets")
cur = conn.cursor()

def column_stats(table_name,col_name):
    query = "SELECT " + col_name +  " FROM " + table_name 
    cur.execute(query)
    column = cur.fetchall()
    column_matrix = []
    for each_row in column:
        column_matrix.append(each_row)
    mean = np.mean(column_matrix)
    median = np.median(column_matrix)
    return (mean,median)

print(column_stats('star','t_eff'))    
