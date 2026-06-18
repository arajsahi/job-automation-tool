import psycopg2
conn = psycopg2.connect(
    dbname="mydb",
    user="arajsahi",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM jobs")
rows = cursor.fetchall()

for row in rows:
    print(row)



cursor.execute("INSERT INTO jobs(title,company,location)VALUES(%s,%s,%s)",
               ('Data Analyst','Google','Toronto')


)
conn.commit()
print("Job inserted")

conn.close()



