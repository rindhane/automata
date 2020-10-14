import os 
import hashlib
import json

start_path=input("Enter the path")
def get_file_andHash_list():
	return list(), list()
def get_root_path():
	return ''

file_list , hash_list=get_file_andHash_list()
root_path=get_root_path()
for (base_path,dirs,files) in os.walk(start_path):	
	for file_ in files:
		file_name=root_path+base_path+"/"+file_
		file_list.append(file_name)
		hash_list.append(hashlib.md5(open(file_name,"rb").read()).hexdigest())

file_store = dict()
file_store['root_path']=os.getcwd()
file_store['start_path']=start_path
file_store['file_list']=file_list
file_store['hash_list']=hash_list

json_file=input("Enter Json file name")
with open(json_file+".json","w") as file_ :
	file_.write(json.dumps(file_store))
	print("files name and their hashes are stored in the file " + '"{0}.json"'.format(json_file)+" at location" + ": "+os.getcwd())


 
		
