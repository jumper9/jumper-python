if False:
	# Connect to the database.
	import pymysql
	conn = pymysql.connect(
	    db='example',
	    user='root',
	    passwd='rootpass',
	    host='localhost',
	    autocommit=True)

	c = conn.cursor()

	# Insert some example data.
	c.execute("INSERT INTO numbers VALUES (1, 'One!')")
	c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
	c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
	#conn.commit()

	# Print the contents of the database.
	c.execute("SELECT * FROM numbers")
	print([(r[0], r[1]) for r in c.fetchall()])

