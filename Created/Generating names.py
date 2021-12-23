import pandas as pd
import psycopg2

male_names = pd.read_csv("male_names.csv")
female_names = pd.read_csv("female_names.csv")
last_names = pd.read_csv("last_names.csv")

listm= dict(male_names)
print(listm)