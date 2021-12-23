import psycopg2
import time

#Number of rows to add in each batch
n=10000

#Generate single INSERT INTO query
single_query = """INSERT INTO post(user_id, post_text)
    VALUES (1,'All work and no play makes Jack a dull boy.');"""

#Generateone BIG query
big_query = "INSERT INTO post(user_id,post_text) VALUES"
for i in range(n):
    big_query += "(1,'All work and no play makes Jack a dull boy.'),"
big_query = big_query.strip(',') + ';' #Replace trailing ',' with ';'

#Connect to database & create cursor
conn = psycopg2.connect(user="postgres",password="acrimonious",host="localhost",port="8101",database="CHITTER")
cur = conn.cursor()

#Time the 'n' individual queries
start_time = time.process_time()
for i in range(n):
    cur.execute(single_query)
conn.commit()
stop_time = time.process_time()
print("{0} individual queries took {1} seconds.".format(n,stop_time-start_time))

#Time for BIG query
start_time = time.process_time()
cur.execute(big_query)
stop_time = time.process_time()
print("The query with {0} rows took {1} seconds.".format(n,stop_time-start_time))

#Close both cursor and connection to database
cur.close()
conn.close()
