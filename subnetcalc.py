
import math

ip=input("Enter IP Address : ")
subnet=int(input("Enter Subnet Mask : "))


def IptoBinary(ip):
	n=ip.split('.')
	#print(n)
	c=''
	count=0
	for i in n:
		count+=1
		b=bin(int(i)).replace("0b", "")
		if(len(b) < 8):
			r=8-len(b)
			for z in range(r):
				c+='0'
		c+=b
		if(count<4):
			c+='.'	
	return c
	
def BinaryToDecimal(kn):	
	n=kn.split('.')
	print(n)
	count=0
	c=''
	for i in n:
		#print(i)
		count+=1
		val=int(i,2)
		c+=str(val)
		if(count<4):
			c+='.'	
	return c	

def AvailableAddress(n):
	s=32-n
	x=math.pow(2, s) - 2
	return x
	

def SubnettoMask(n):
	id = ''
	
	for i in range(n):
		id +='1'
		if( n == 32):
			if(len(id) == 8 or len(id) == 17 or len(id) == 26):
				id +='.'
	#print(id)
	if(n < 32):
		z = 32 - n
		for i in range(z):
			id+='0'
	#print(id)
	a=id[0:8]
	b=id[8:16]
	c=id[16:24]
	d=id[24:33]
	print(a + '.' +b+'.' +c+ '.' +d)
	
	
def NetworkAd(i,m):
	if(m<8):
		c=i[:m]
		print(c)
		h=8-m
		for i in range(h):
			c+='0'
		c+='.00000000.00000000.00000000'
	if(m>=8 and m<17):
		c=i[:m+1]
		print(c)
		h=16-m
		for i in range(h):
			c+='0'
		c+='.00000000.00000000'
	if(m>=17 and m<25):
		c=i[:m+2]
		print(c)
		h=24-m
		for i in range(h):
			c+='0'
		c+='.00000000'
	if(m>=25 and m<32):
		c=i[:m+3]
		print(c)
		h=32-m
		for i in range(h):
			c+='0'
	print(c)		
	return BinaryToDecimal(c)
		
def BroadAd(i,m):
	if(m<8):
		c=i[:m]
		print(c)
		h=8-m
		for i in range(h):
			c+='1'
		c+='.11111111.11111111.11111111'
	if(m>=8 and m<17):
		c=i[:m+1]
		print(c)
		h=16-m
		for i in range(h):
			c+='1'
		c+='.11111111.11111111'
	if(m>=17 and m<25):
		c=i[:m+2]
		print(c)
		h=24-m
		for i in range(h):
			c+='1'
		c+='.11111111'
	if(m>=25 and m<32):
		c=i[:m+3]
		print(c)
		h=32-m
		for i in range(h):
			c+='1'
	print(c)				
	return BinaryToDecimal(c)

		
	
def RangeofAddress():
	f='11000000.10101000.00000001.00000100'
	s='11000000.10101000.00000001.00000100'
	print(f[-1])
	f[-1] = f[-1]+1
	x=[str(x) for x in f]
	return x
	


#print(IptoBinary(ip))
#SubnettoMask(subnet)
#print(AvailableAddress(subnet))
#print(NetworkAd(IptoBinary(ip),subnet))
#print(BroadAd(IptoBinary(ip),subnet))
RangeofAddress()
#h=NetworkAd(IptoBinary(ip),subnet)
#print(h)
#print(BinaryToDecimal(h))

















