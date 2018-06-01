import csv
import psycopg2

fname = 'nachos-list.csv'

conn = psycopg2.connect(dbname="resto",user="postgres",password="pink123",host="localhost",port="")
cur = conn.cursor()

fieldnames = ("name","descp","cost","type")

with open(fname,newline='\n') as cf:
	reader = csv.DictReader(cf,delimiter=':',fieldnames=fieldnames)
	for row in reader:
		print(row)
		cost = float(row['cost'][4:])
		print(cost)
		if "Vegetarian" in row['type']:
			ntype=True
		else:
			ntype=False
		query= "INSERT INTO nachos(name,des,cost,veg) VALUES('{}','{}',{},{}) ".format(row['name'],row['descp'],cost,ntype)
		print(query)
		cur.execute(query)

conn.commit()
conn.close()
