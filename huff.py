from collections import defaultdict
# from bisect import insort as appendsort
from binsearch import appendsort
class BinBuffer:
	def __init__(self):
		self.buff=""
		self.byte=""
		self.rb=0
	def __str__(self):
		return str(self.buff)
	def __iter__(self):#bit itter till n-1 byte
		haveFrag=(self.rb!=0)
		lb=-1 if haveFrag else None
		for byte in self.buff[0:lb]:
			for bit in (bin(ord(byte))[2::]).zfill(8):
				yield bit
		if haveFrag:
			for bit in (bin(ord(self.buff[-1]))[2::]).zfill(8)[0:self.rb]:
				yield bit
	def __consumeByte(self):
		self.buff+=chr(int(self.byte[0:8],2))
		self.byte=self.byte[8:]
	def append(self,s):
		assert type(s)==str
		self.byte+=s
		while (len(self.byte)//8)!=0:
			self.__consumeByte()
	def __len__(self):
		return len(self.buff)
	def flush(self):
		self.rb=len(self.byte) #quantidade de bits do ultimo byte
		assert self.rb<8
		if self.rb!=0:
			self.byte=self.byte+("0"*(8-self.rb))
			self.__consumeByte()
class HuffNode:
	left=None
	right=None
	def __init__(self,char,freq):
		self.char=char
		self.freq=freq
	def merge(l,r):
		ans=HuffNode(None,l.freq+r.freq)
		ans.left,ans.right=l,r
		return ans
	# STACK corruption????
	# def gentables(self,ans={},b=""):
	# 	if (self.left,self.right) == (None,None):
	# 		ans[b]=self.char
	# 	if self.left:self.left.gentables(ans,b+"0")
	# 	if self.right:self.right.gentables(ans,b+"1")
	# 	return dict((v,k)for k,v in ans.items()),ans
	def gentables(self):
		stack=[(self,"")]
		ans={}
		while(stack!=[]):
			aux,b=stack.pop()
			if (aux.left,aux.right) == (None,None):
				ans[b]=aux.char
			if aux.left:stack.append((aux.left,b+"0"))
			if aux.right:stack.append((aux.right,b+"1"))
		return dict((v,k)for k,v in ans.items()),ans
	def print(self):
		if self.left:self.left.print()
		print(self)
		if self.right:self.right.print()
	def __str__(self):
		return "HuffNode(%s,%i)"%(self.char,self.freq)
	def __repr__(self):
		return str(self)
	def __gt__(self,obj):
		assert type(obj)==HuffNode
		return self.freq>obj.freq
def huffcompressionrate(data,coded):
	return 100*((len(data)-len(coded))/len(data))
def hufftable(s):
	freq=defaultdict(int)
	for l in s:
		freq[l]+=1
	nodes=[]
	for k in freq.keys():
		appendsort(nodes,HuffNode(k,freq[k]))
	while(len(nodes)!=1):
		appendsort(nodes,HuffNode.merge(nodes.pop(0),nodes.pop(0)))
	return nodes[0].gentables()
def huffcode(cotable,s):
	ans=BinBuffer()
	for l in s:
		ans.append(cotable[l])
	ans.flush()
	return ans
def huffdecode(detable,bb):
	ans=""
	temp=""
	for bit in bb:
		temp+=bit
		nb=detable.get(temp,None)
		if nb!=None:
			ans+=nb
			temp=""
	assert temp==""
	return ans
class Huffman:#wrapper
	def __init__(self,data):
		assert len(data)!=0
		self.data=data
		self.cotable,self.detable=hufftable(self.data)
		self.coded=huffcode(self.cotable,self.data)
		self.decoded=huffdecode(self.detable,self.coded)
		self.compressionrate=huffcompressionrate(self.data,self.coded)
if __name__=="__main__":
	def foo(data):
		h=Huffman(data)
		print("original    =",h.data)
		print("codificado  =",bytes(str(h.coded),"utf-8"))
		print("decodificado=",h.decoded)
		print("medida de compressão:%f%%"%h.compressionrate)
		print("--------------")
	
	foo("abcdefghijklmnopqrst")
	foo("ddceeaeecceecebaaebbaddbdcaddebdccdbebca")
	# foo("ddceeaeecceecebaaebbaddbdcaddebdccdbebcaac")