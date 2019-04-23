def binsearch(a,x):
	i=0
	j=len(a)
	while i != j:
	    m = (i+j)//2
	    if x==a[m]:
	    	return True
	    elif x < a[m]: 
	    	j = m
	    else: 
	    	i = m+1
	return False
    
def appendsort(a, x):
    i=0
    j=len(a)
    while i != j:
        m = (i+j)//2
        if x < a[m]: 
        	j = m
        else: 
        	i = m+1
    a.insert(i,x)