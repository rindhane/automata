#! /usr/bin/env python
import json 
from json import scanner

class tree_structure :
	def __init__(self, id_ ,name=None,parent=None,children=None):
		self.name = name
		self.id = id_ 
		self.parent = None		
		self.children = children #use append instead here
		self.separator = '/'
		#add function to add nodes and items on initiation.
	def get_path(self):
		if self.parent:
			return self.parent.get_path()+self.separator+self.id
		else :
			return self.id
	def is_path(self,path):
		if self.parent:
			return parent.is_path(path)
		else :
			traverse=[i for i in path.split('/') if i != '']
			while True:
				if traverse:
					if traverse[0] in self.children:
						self=self.children[traverse[0]]
						traverse=traverse[1:]
					else:
						return False
				else :
					return True
	def __repr__(self):
		return f'Tree:(id:{self.id},children:{self.children})'

class treeJsonEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, tree_structure):
             return {obj.id : obj.children}
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)

class treeJsonDecoder(json.JSONDecoder):
	def __init__(self, **kwargs):
		super().__init__( **kwargs )
		self.object_hook = self.converter
		self.scan_once = scanner.make_scanner(self)
	@staticmethod
	def converter(obj):
		tmp=list(obj.items())[0]
		#check why this is not working
		return tree_structure(id_=tmp[0], children=tmp[1])


if __name__== "__main__":
	print(json.loads('{"idx": ["folder1", "folder2"]}',cls=treeJsonDecoder))