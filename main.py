import math
import tkinter as tk


root = tk.Tk()
root.title(" GUI Subnet calculator")
root.geometry("600x400")
root.config(bg='#05c1ff')

ip = tk.StringVar(root)
ips = tk.StringVar(root)
subnet = tk.IntVar(root)
nad = tk.StringVar(root)
bad = tk.StringVar(root)
avips = tk.StringVar(root)
rang = tk.StringVar(root)


#ip=input("Enter IP Address : ")
#subnet=int(input("Enter Subnet Mask : "))


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
	#print(n)
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
	return(a + '.' +b+'.' +c+ '.' +d)
	
	
def NetworkAd(i,m):
	if(m<8):
		c=i[:m]
		#print(c)
		h=8-m
		for i in range(h):
			c+='0'
		c+='.00000000.00000000.00000000'
	if(m>=8 and m<17):
		c=i[:m+1]
		#print(c)
		h=16-m
		for i in range(h):
			c+='0'
		c+='.00000000.00000000'
	if(m>=17 and m<25):
		c=i[:m+2]
		#print(c)
		h=24-m
		for i in range(h):
			c+='0'
		c+='.00000000'
	if(m>=25 and m<32):
		c=i[:m+3]
		#print(c)
		h=32-m
		for i in range(h):
			c+='0'
			
	return c

def BroadAd(i,m):
	if(m<8):
		c=i[:m]
		#print(c)
		h=8-m
		for i in range(h):
			c+='1'
		c+='.11111111.11111111.11111111'
	if(m>=8 and m<17):
		c=i[:m+1]
		#print(c)
		h=16-m
		for i in range(h):
			c+='1'
		c+='.11111111.11111111'
	if(m>=17 and m<25):
		c=i[:m+2]
		#print(c)
		h=24-m
		for i in range(h):
			c+='1'
		c+='.11111111'
	if(m>=25 and m<32):
		c=i[:m+3]
		#print(c)
		h=32-m
		for i in range(h):
			c+='1'
			
	return c

def RangeofAddress(fntwrk,fbroadcast):
     return fntwrk+"-"+fbroadcast
     
     
def clean():
    ip.set('')
    ips.set('')
    subnet.set('')
    nad.set('')
    bad.set('')
    avips.set('')
    rang.set('')
    
def subnetcalculate():
    ipj = ip.get()
    mask = subnet.get()
    ipl = IptoBinary(ipj)
    ips.set(f"{ipl}")
    ipadd = IptoBinary(ipj)
    #print(ipadd)
    ntadrress = NetworkAd(ipadd, mask)
    print(ntadrress)
    fntwrk = BinaryToDecimal(ntadrress)
    nad.set(f"{fntwrk}")
    broadcast = BroadAd(ipadd, mask)
    fbroadcast=BinaryToDecimal(broadcast)
    bad.set(f"{fbroadcast}")
    subnets = AvailableAddress(mask)
    avips.set(f"{subnets}")
    range = RangeofAddress(fntwrk,fbroadcast)
    rang.set(f"{range}")


tk.Label(root, text="IP Address").grid(row=0, column=0)
ipfield = tk.Entry(root, textvariable=ip)
ipfield.grid(row=0, column=1)

tk.Label(root, text="Subnet").grid(row=1, column=0)
subnetfield = tk.Entry(root, textvariable=subnet)
subnetfield.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=subnetcalculate).grid(row=2, column=0)
tk.Button(root, text="Clear", command=clean).grid(row=2, column=1)

tk.Label(root, text="IP Address").grid(row=3, column=0)
ntfield = tk.Entry(root, textvariable=ips)
ntfield.grid(row=3, column=1)

tk.Label(root, text="Network Address").grid(row=4, column=0)
ntfield = tk.Entry(root, textvariable=nad)
ntfield.grid(row=4, column=1)

tk.Label(root, text="Broadcast Address").grid(row=5, column=0)
bdfield = tk.Entry(root, textvariable=bad)
bdfield.grid(row=5, column=1)

tk.Label(root, text="Available No IP").grid(row=6, column=0)
avipsfield = tk.Entry(root, textvariable=avips)
avipsfield.grid(row=6, column=1)

tk.Label(root, text="Range").grid(row=7, column=0)
rangfield = tk.Entry(root, textvariable=rang)
rangfield.grid(row=7, column=1)

root.mainloop()


#print(IptoBinary(ip))
#SubnettoMask(subnet)
#print(AvailableAddress(subnet))
#NetworkAd(IptoBinary(ip),subnet)
