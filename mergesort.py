def mergesort(a):
	m=len(a)//2
	if m==0:
		return a
	fh=a[0:m]
	lh=a[m:]
	fh = mergesort(fh)
	lh = mergesort(lh)
	i=0
	j=0
	ans=[]
	while i<len(fh) and j<len(lh):
		x=fh[i]
		y=lh[j]
		if x<y:
			ans.append(x)
			i+=1
		else:
			ans.append(y)
			j+=1
	while i<len(fh):
		ans.append(fh[i])
		i+=1
	while j<len(lh):
		ans.append(lh[j])
		j+=1
	return ans
if __name__=="__main__":
	from random import shuffle
	def runtest(n):
		ans=list(range(1,n))
		shuffle(ans)
		print(ans)
		print(mergesort(ans))
	runtest(5)
	runtest(10)
	runtest(15)
	runtest(20)