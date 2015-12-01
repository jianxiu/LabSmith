import sqlite3
cxn = sqlite3.connect('db.sqlite3')
cur = cxn.cursor()
cur.execute('alter table post_office_email \
			add column backend_alias varchar(32)')
			
cur.close()
cxn.commit()
cxn.close()