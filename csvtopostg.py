import psycopg2
import csv
import json


conn = psycopg2.connect(dbname="resto",user="postgres",password="pink123",host="localhost",port="")
cur = conn.cursor()

fname = 'restos.csv'

#reader = csv.DictReader(f)
fieldnames = ("lat","lng","name")

with open(fname,newline='\n') as cf:
	reader = csv.DictReader(cf,fieldnames)
	for row in reader:
		print(row['lat'],row['lng'])
		name = row['name'].replace("'","")
		query_str = "INSERT INTO restaurant(name, geom) VALUES ('{}', ST_GeomFromText('POINT({} {})',4326))".format(name,row['lat'],row['lng']);
		print(query_str)
		cur.execute(query_str)
conn.commit()
cur.close()
conn.close()
