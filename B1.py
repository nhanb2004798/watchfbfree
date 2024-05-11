#Bai1
#print("Hello World!")

#Bai2
'''a=7
b=2
print("phep cong:")
print("%d + %d = %d" %(a,b,a+b))

print("phep tru:")
print("%d - %d = %d" %(a,b,a-b))

print("phep nhan:")
print("%d * %d = %d" %(a,b,a*b))

print("phep chia:")
print("%d : %d = %.1f" %(a,b,a/b))

print("chia lay du:")
print("%d / %d = %d" %(a,b,a%b))

print("mu:")
print("%d ** %d = %d" %(a,b,a**b))
'''
#Bai3
'''str = input("nhap ten: ")
print("Hi",str)
'''
#Bai4
'''
bk=float(input("nhap ban kinh hinh tron:"))
pi=3.14
print("dien tich hinh tron S = %d*%d*%.2f=%.2f"%(bk,bk,pi,bk*bk*pi))
print("chu vi hinh tron C = (%d*2)*%.2f=%.2f"%(bk,pi,bk*2*pi))'''

#Bai5
'''n=int(input("nhap so nguyen duong n:"))
#tinh s
s=0
for i in range(1,n+1):
    s+=i
print ("s=%d"%s)
#tinh s1
s1=0
for i in range(1,2*n,2):
    s1+=i
print ("s1=%d"%s1)
#tinh s2
s2=0
for i in range(2,2*n+1,2):
    s2+=i
print ("s2=%d"%s2)
#tinh s3
s3=0
for i in range(1,n+1):
    s3+=i**2
print ("s3=%d"%s3)
#tinh s4
s4=0
for i in range(0,n+1):
    s4+=1/(2**i)
print ("s4=%.2f"%s4)'''

#Bai6
'''n=int(input("Nhap so nguyen: "))
nhiphan=""
while n>0:
    nhiphan=str(n%2)+nhiphan
    n=n//2
print(nhiphan)'''

#Bai7
'''import math
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
c=float(input("Nhap c: "))

if a==0:
    if b==0:
        if c==0:
            print("phuong trinh vo so nghiem!!!")
        else:
            print("phuong trinh vo nghiem!!!")
    else:
        if c == 0:
            print("phuong trinh co nghiem x = 0")
        else:
            print("phuong trinh co nghiem x = "-c/b)
else:
    delta = b**2-4*a*c
    if delta < 0:
        print("phuong trinh vo nghiem!!!")
    elif delta==0:
        print("phuong trinh co nghiem kep x1 = x2 = "-(b/(2*a)))
    else:
        print ("phuong trinh co 2 nghiem phan biet:")
        print("x1 = ",(-(b)+ math.sqrt(delta))/(2*a))
        print("x2 = ",(-(b)- math.sqrt(delta))/(2*a))'''

#Bai8
'''str=input("Nhap 1 chuoi:")
print("do dai cua chuoi:",len(str))
print("ky tu dau:",str[0])
print("ky tu cuoi",str[-1])
i=int(input("nhap vi tri i:"))
j=int(input("nhap vi tri j:"))
print("cac ky tu tu vi tri i=%d den vi tri j=%d la:" %(i,j),str[i:j+1])'''

#Bai9
'''str = input("nhap chuoi:")
tanso={}
for kytu in str:
    if kytu!=" " :
        if kytu in tanso:
            tanso[kytu]+=1
        else:
            tanso[kytu]=1
print (tanso)'''

#Bai10
'''str = input("nhap chuoi cac so, cach nhau boi dau ; :")
so = str.split(";")
tong=0
for i in so:
    i = int(i)
    tong += i
print (tong)'''

#Bai11
'''def add_tags (tag,name):
    print("<%s>%s</%s>" %(tag,name,tag))
add_tags('i', 'Python')
add_tags('b', 'Python Tutorial')'''
#Bai12
'''def dem_string(chuoicha, chuoicon):
    return chuoicha.count(chuoicon)
chuoicha = input("Nhap chuoi cha: ")
chuoicon = input("Nhap chuoi con: ")
print(dem_string(chuoicha,chuoicon))'''
#Bai13
'''def themdongdau(str,strdongdau):
    dong = str.split("\n")
    for i in range (len(dong)):
        dong[i] = strdongdau + dong[i]
    return "\n".join(dong)
print(themdongdau("Su\nPham\nCan\nTho","+++ "))'''
#Bai14
def kiemtradoixung(str):
    strdaonguoc = "".join(reversed(str))
    if str == strdaonguoc:
        return print ("%s la doi xung"%str)
    else:
        return print("%s khong la doi xung"%str)
str = input("nhap chuoi: ")
print(kiemtradoixung(str))

    
