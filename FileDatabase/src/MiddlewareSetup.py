from .utilities import self_setup_class
import os 

#skeleton class for inheritance 
class Middleware(self_setup_class):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def save_database(self,string):
        pass
    def load_database(self):
        string=''#returns jsonString of Database
        return string
    def store_entry(self,entry):
        pass
    def getHeaders(self, entry):
        pass
    def store_entry(self,entry):
        pass
    def tableCreate(self,name):
        pass
    def table_accessible(self,name):
        pass
    def delete_entry(self,entry):
        pass

#Middleware for local filesystem
class localFileMiddleware(Middleware):
    def __init__(self,**kwargs):
        self.filepath=None#'database.json'
        self.dataPath=None
        super().__init__(**kwargs)
    def load_database(self):
        with open(self.filepath,'r') as fp:
            string=fp.read()
        return string
    def save_database(self,string):
        with open(self.filepath,'w') as fp:
            fp.write(string)
        return True
    def getHeaders(self, entry):
        table=entry.getTable()
        index=entry.getIndex()
        if table is not None and index is not None :
            #here folders are tables
            path=('' if not self.dataPath else self.dataPath+'/')+\
                str(table)+'/'+str(index)+".dbEntry"
            return path
        else:
            raise Exception("entry is not completely valid to have submitted")
    def store_entry(self,entry):
        path=self.getHeaders(entry)
        with open(path,'w') as fp:
            fp.write(str(entry.content))
        return True
    def delete_entry(self,entry):
        path=self.getHeaders(entry)
        os.remove(path)
        return True
    def get_entry(self,entry):
        path=self.getHeaders(entry)  
        with open(path,'r') as fp:
            content=fp.read()
        return content
    def get_table_path(self,tableName):
        path=('' if not self.dataPath else self.dataPath+'/')+str(tableName)
        return path
    def checkTable(self,name):
        return os.path.isdir(self.get_table_path(name))
    def tableCreate(self,name):
        if self.checkTable(name):
            return False
        os.mkdir(self.get_table_path(name))
        return True
    def table_accessible(self,name):
        if self.checkTable(name):
            return True
        print(self.get_table_path(name))
        os.mkdir(self.get_table_path(name))
        return True
    def entry_accessible(self,entry):
        path =self.getHeaders(entry)
        if os.path.isfile(path):
            return True
        return None 