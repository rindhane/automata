class structure :
	def __init__(self,name=None,nodes = None, items=None):
		self.name=name		
		self.nodes=list()
		self.childs=list()
		#add function to add nodes and items on initiation.
	def get_more_path(self,path):
		tmp=self.is_path(path)
		if tmp:
			if type(tmp)==type('more'):
				node=get_node('path')
	
	def get_node(self,path):
		traverse=path.split('/')
		if traverse[0]==self.name
			if len(traverse[1:])==0:
				return node		
			else:				
				for node in self.nodes:
					return node.get_node('/'.join(traverse[1:]))
		else:
			return None		
	def is_path(self,path):
		traverse=path.split('/')
		if self.name==traverse[0]:
			for node in self.nodes:
					if len(traverse('/')[1:])>0 and node.name==traverse[1]  :
						return node.is_path('/'.join(traverse[1:]))
					else:
						return False
			if len(traverse[1:])>0:
				return '/'.join(traverse[1:])
			return True
		else:
			return False
	def add_childs(self,items):
		if items!=None :
			for item in items:
				self.childs.append(item)
		




import os 
root_path= "."
folder_tree=structure()
for points in os.walk(root_path):
	point=structure(points[0],points[1],points[2])
	
		
