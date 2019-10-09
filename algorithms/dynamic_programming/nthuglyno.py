def finduglyno(n):
	i1,i2,i3=0,0,0
	u=[None]*n
	u[0]=0
	nextmul2,nextmul3,nextmul5=2,3,5
	for i in range(1,n):
		nextuglyno=min(nextmul2,nextmul3,nextmul5)
		u[i]=nextuglyno
		if nextuglyno==nextmul2:
			i1+=1
			nextmul2=u[i1]*2
		if nextuglyno==nextmul3:
			i2+=1
			nextmul3=u[i2]*3
		if nextuglyno==nextmul5:
			i3+=1
			nextmul5=u[i3]*3
	print(nextuglyno)
finduglyno(8)


