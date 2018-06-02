import csv
import psycopg2

fname = 'nachos-list.csv'

conn = psycopg2.connect(dbname="nachosfinder",user="postgres",password="pink123",host="localhost",port="")
cur = conn.cursor()

fieldnames = ("name","descp","cost","type","resto")

with open(fname,newline='\n') as cf:
	reader = csv.DictReader(cf,delimiter=':',fieldnames=fieldnames)
	for row in reader:
		print(row)
		cost = float(row['cost'][4:])
		if "Vegetarian" in row['type']:
			ntype=True
		else:
				ntype=False

		rname = row['resto'].strip()
		q1 = "select id from resto_resto where name like '{}'".format(rname)
		print(q1)
		
		cur.execute(q1)
		rids = cur.fetchall()
		print(rids)
		for rid in rids:
			query= "INSERT INTO resto_dish(name,description,cost,veg,resto_id) VALUES('{}','{}',{},{}, (select id from resto_resto where id={}))".format(row['name'],row['descp'],cost,ntype,rid[0])
			print(query)
			cur.execute(query)
			conn.commit()

conn.close()
