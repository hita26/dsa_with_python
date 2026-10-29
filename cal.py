class operation:
    def sum(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b

    def sq(self,a):
        return a*a

    def cb(self,a):
        return a*a*a

o=operation()

print("1=sum")
print("2=sub")
print("3=mul")
print("4=div")
print("5=square")
print("6=cube")

ch=int(input("enter urr choice"))

if ch==1:
    a=float(input("enter ur 1st value"))
    b=float(input("enter ur 2nd value"))
    print("sum=",o.sum(a,b))
elif ch==2:
    a=float(input("enter ur 1st value"))
    b=float(input("enter ur 2nd value"))
    print("sub=",o.sub(a,b))
elif ch==3:
    a=float(input("enter ur 1st value"))
    b=float(input("enter ur 2nd value"))
    print("mul=",o.mul(a,b))
elif ch==4:
    a=float(input("enter ur 1st value"))
    b=float(input("enter ur 2nd value"))

    if b!=0:
        print("div =",o.div(a,b))
    else:
        print("canot div by zero")
    

elif ch==5:
    a=float(input("enter ur 1st value"))
    print("sum=",o.sq(a))
elif ch==6:
    a=float(input("enter ur 1st value"))
    
    print("sum=",o.cb(a))
else:
    print("invaild")
