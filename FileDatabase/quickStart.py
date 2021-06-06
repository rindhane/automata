from src.manager import  Database
from src.MiddlewareSetup import localFileMiddleware

fileWare=localFileMiddleware(filepath='database.json', dataPath='trial_db')
db=Database(middleware=fileWare)

#***scripts for creating a fresh database ********
#following block also gives idea of complete schema
"""
table=db.create_table(name='articles')
SCHEMA_articles={'id':'$AUTO$','title':None, 'body':None, 'author':None , 'create_date':'$AUTO_DATETIME$'}
table.set_schema(SCHEMA_articles)
table=db.create_table(name='users')
SCHEMA_users={'id':'$AUTO$','name':None,'email':None,'username':'primaryKey','password':None , 'registered_date':'$AUTO_DATETIME$'}
table.set_schema(SCHEMA_users)
db.save_to_file()
"""
#********************************************************

db.load_from_file()
