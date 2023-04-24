import psycopg2

con = psycopg2.connect(host="localhost", database="phonebook", user="postgres", password="1234")
current = con.cursor()

current.execute('''CREATE TABLE phonebook(name varchar, number varchar);''')

current.close()
con.commit()
con.close()