l1 =[9,9,9,9,9,9,9];
l2 = [9,9,9,9];
Output=[8,9,9,9,0,0,0,1];

class Solution:
	def addTwoNumbers(self, l1, l2) :
		def get(node,tag):
			if node == None and tag=="val" : 
				return 0
			elif node == None :
				return None
			elif tag == "node":
				return node.next
			elif tag == "val":
				return node.val
		rem=0	
		store=list()
		while (l1!=None or l2!=None):
			totalTemp=get(l1,"val")+get(l2,"val")+rem
			store.append(ListNode(val=totalTemp%10))
			rem = int(totalTemp/10)
			l1=get(l1,"node");l2=get(l2,"node")
		if (rem!=0):
			store.append(ListNode(val=rem))
		i=1
		while (i<len(store)):
			store[i-1].next=store[i]
			i=i+1
		return store[0]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def create (cls,a) :
	start=None; 
	for nodes in cls.generate(a):
		start=nodes
	return start

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	@classmethod
	def generate(cls,l):
		a=None;
		l.reverse();l_=list(l);l.reverse();
		for nums in l_ : # make sure l is a list not a iterator
			tmp= cls(nums,next=a);			
			yield tmp;
			a = tmp;
	def output_val(self,container=list()):
		container.append(self.val)
		if self.next == None : 
			return container
		else :
			return self.next.output_val(container=container)
		



def equals(test, output):
	if (test==None and output==None):
		return True
	elif (test==None or output==None) :
		return False
	else :	
		if (test.val==output.val):
			test=test.next
			output=output.next	
			return equals(test,output)
		else :
			return False


def trial (l1,l2,Output):	
	l1=create(ListNode,l1)
	l2=create(ListNode,l2)
	test=create(ListNode,Output)
	sol=Solution()
	ans=sol.addTwoNumbers(l1,l2)
	print("expected output ;" , Output);
	print("result :", ans.output_val());
	print("Are solution and output same : ", equals(ans,test));

#trial(l1=l1,l2=l2,Output=Output)
def get_input (i):
	val=input(f"enter list: {i} >>")
	elem=val.split(',');
	l1=list();
	for a in elem :
		a=a.replace('[','');
		a=a.replace(']','');
		l1.append(int(a));
	return l1
	
l1=get_input(1)
l2=get_input(2)
l3=get_input("output")
trial(l1=l1,l2=l2,Output=l3)
