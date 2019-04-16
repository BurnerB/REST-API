import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()


#define shema(how data is going to look)
create_table = "CREATE TABLE users(id int,username text,password text )"
cursor.execute(create_table)

user = (1, "Abu", "abcd")
insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, "Aba", "abcde"),
    (3, "Abe", "abcdf")
]

cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()