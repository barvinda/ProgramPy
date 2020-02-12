import sqlite3

def create_table():
    conn=sqlite3.connect("lite1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, rating INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,rating):
    conn=sqlite3.connect("lite1.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (Null,?,?,?,?)",(title,author,year,rating))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    row=cur.fetchall()
    conn.close()
    return row

def search(title="",author="",year="",rating=""):
    conn=sqlite3.connect("lite1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store WHERE title=? OR author=? OR year=? OR rating=?",(title,author,year,rating))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("lite1.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,rating):
    conn=sqlite3.connect("lite1.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET title=?,author=?,year=?,rating=? WHERE id=?",(title,author,year,rating,id))
    conn.commit()
    conn.close()

create_table()
#update(3,"Anti-Fragile","Nasim Taleb",2013,4.2)
#insert("Antifragile","Naseem Taleb", 2004, 4.5)

#print(search(author="Yuval Harris"))
