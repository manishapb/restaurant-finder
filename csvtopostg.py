import psycopg2
import csv
import json
import sys


conn = psycopg2.connect(dbname="nachosfinder",user="postgres",password="pink123",host="localhost",port="")
cur = conn.cursor()

fname = sys.argv[1]


#reader = csv.DictReader(f)
fieldnames = ("lat","lng","name")

with open(fname,newline='\n') as cf:
	reader = csv.DictReader(cf,fieldnames)
	for row in reader:
		print(row['lat'],row['lng'])
		name = row['name'].replace("'","")
		query_str = "INSERT INTO resto_resto(name, address) VALUES ('{}', ST_GeomFromText('POINT({} {})',4326))".format(name,row['lng'],row['lat']);
		print(query_str)
		cur.execute(query_str)
conn.commit()
cur.close()
conn.close()
