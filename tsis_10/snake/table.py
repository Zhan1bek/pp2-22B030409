import psycopg2

con = psycopg2.connect(host="localhost", database="snake", user="postgres", password="1234")
current = con.cursor()

current.execute('''CREATE TABLE snake(name varchar, score varchar, level varchar);''')

current.close()
con.commit()
con.close()