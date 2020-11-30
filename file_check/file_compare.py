import os 
import json
import hashlib
from pathlib import PureWindowsPath


file_name=input("enter reference Json file name: ")
with open(file_name, "r") as file_:
	file_store_ref =json.loads(file_.read())

print("reference file has been loaded")


start_path=input("Enter the start path")
def get_file_andHash_list():
	return list(), list()
def get_root_path():
	return ''

def get_unix_path(path):
	return str(PureWindowsPath(path)).replace("\\","/")


root_path=get_root_path()
file_list , hash_list =get_file_andHash_list()
for (base_path,dirs,files) in os.walk(start_path):	
	for file_ in files:
		file_name=root_path+base_path+"/"+file_
		file_list.append(file_name)
		hash_list.append(hashlib.md5(open(file_name,"rb").read()).hexdigest())

print("provided file path has been traversed")
#---Analysis begin------


ref_hash_list=file_store_ref["hash_list"]
ref_file_list=[get_unix_path(fp) for fp in file_store_ref["file_list"]]

#-------compare total number of files

print("total number of files in reference: " + str(len(ref_file_list)))
print("total number of files in given: " + str(len(file_list)))

#----find different files : 
ref_set=set(ref_file_list)
given_set=set(file_list)
common_set=ref_set.intersection(given_set)

print("Following files are not in given path")
for file_ in ref_set-common_set:
	print("   "+"file: "+file_)

print("Following files are not in reference path")
for file_ in given_set-common_set:
	print("   "+"file: "+file_)


#--trial_data

#----find different files : 
print("following files don't have same version in reference and given path")

for f in common_set:
	if ref_hash_list[ref_file_list.index(f)]!=hash_list[file_list.index(f)]:
		print("   "+"file: "+f)		

print("comparison is over")


	








