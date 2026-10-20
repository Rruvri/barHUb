import sqlite3

con = sqlite3.connect('bar.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS stock_items (
					id INTEGER PRIMARY KEY,
                	name text NOT NULL,
                	category text NOT NULL,
                	size_per_unit INT,
                	unit_measure text,
                	stock_count INT
                );""")
                
con.commit()                
                
                
				

