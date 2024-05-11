#Bai15
'''def max_num(list):
    return max(list) #ham co trong python lay gia tri lon nhat trong list

list_num=[1,5,2,5,4,7,2,24]
print(max_num(list_num))'''

#Bai16
'''def numblist(list_numb, reverse=True):
    if reverse :
        list_numb_sorft = sorted(list_numb) #ham tang dan gia tri
        return (list_numb_sorft)
    else:
        list_numb_sorft = sorted(list_numb, reverse=True) #ham giam dan gia tri gia tri
        return(list_numb_sorft)
    
list_numb=[1,5,2,4,6,4]
print('day so ban dau:',list_numb)
list_giam = numblist(list_numb,reverse=False)
list_tang = numblist(list_numb)
print('day so giam dan:',list_giam)
print('day so tang dan:',list_tang)'''

#Bai17
'''def merge(list1, list2, tangdan = True):
    kq=[]
    i=0
    j=0
    if tangdan:
        while i<len(list1) and j<len(list2):
            if list1[i] <= list2[j]:
                kq.append(list1[i])
                i+=1
            else:
                kq.append(list2[j])
                j+=1
    else:
        while i<len(list1) and j<len(list2):
            if list1[i] > list2[j]:
                kq.append(list1[i])
                i+=1
            else:
                kq.append(list2[j])
                j+=1
    kq.extend(list1[i:])
    kq.extend(list2[j:])
    return kq


list1=[1,4,6]
list2=[2,7,8]

list3=[6,4,1]
list4=[8,7,2]

tangdan = merge(list1, list2)
giamdan = merge(list3, list4, tangdan=False)

print('danh sach 1:',list1)
print('danh sach 2:',list2)
print('danh sach tang dan',tangdan)
print('danh sach 3:',list3)
print('danh sach 4:',list4)
print('danh sach giam dan:',giamdan)
'''

#Bai18
'''def botrung(list):
    kq=[]
    for i in list:
        if i not in kq:
            kq.append(i)
    return kq

list = ['Apple', 'Apple', 4,4 ,6,7,7]
print(botrung(list))'''

#Bai19
'''def sum1(list):
    kq=0
    for i in list:
        kq+=i
    return kq
list = [1,5,2,3]
tong=sum1(list)
print('tong cua list la:',tong)'''

#Bai20
'''def tich(list):
    kq=1
    for i in list:
        kq*=i
    return kq
list = [1,5,2,3]
tong=tich(list)
print('tong cua list la:',tong)'''

#Bai21
'''def nghich(list):
    return list[::-1]

list="Hello World!"
dao=nghich(list)
print('chuoi nghich la:', dao)'''

#Bai22
'''def giaithua(n):
    if n == 0 :
        return 1
    else:
        return n*giaithua(n-1)
    
n = int(input('nhap n so nguyen: '))
tong=giaithua(n)
print('ket qua:',tong)'''

#Bai23
'''def tower_of_hanoi(n, A, B, C):
    if n > 0:
        # Di chuyển (n-1) tầng tháp từ cột nguồn tới cột trung gian
        tower_of_hanoi(n-1, A, C, B)
        
        # Di chuyển tầng tháp cuối cùng từ cột nguồn tới cột đích
        print(f"Di chuyển tầng tháp {n} từ cột {A} sang cột {B}")
        
        # Di chuyển (n-1) tầng tháp từ cột trung gian tới cột đích
        tower_of_hanoi(n-1, C, B, A)

n = 3 
tower_of_hanoi(n, 'A', 'B', 'C')
'''

#Bai24
'''def nhiphan(n):
    if n == 0:
        return ['']
    else:
        strings = []
        for str in nhiphan(n-1):
            strings.append(str + '0')
            strings.append(str + '1')
        return strings

n = int(input('nhap so bit:'))
nhiphan = nhiphan(n)
for str in nhiphan:
    print(str)'''

#Bai25
'''def daidien(list):
    kq=[]
    for i in list:
        if i not in kq:
            kq.append(i)
    return kq

list = ['Apple', 'Apple', 4,4 ,6,7,7,8,2,4,'bod','bod']
print(daidien(list))'''

#Bai26
'''def printPascal(n):
	for line in range(1, n + 1): #hien thi dong thu line
		C = 1; #mac dinh mong dong cot 1 gia tri mac dinh la 1
		for cot in range(1, line + 1): #cot thu 1..line+1
			print(C, end = " ")
			C = int(C * (line - cot) / cot) #cong thuc
		print("")
n = 5
printPascal(n)'''

#Bai27
'''def tamgiaccan(n):
    for line in range(1,n+1):
        print("* "*line)
    for line in range(n-1,0,-1): #for int line=n-1; line > 0 ; line--
        print("* "*line)

n = 5
tamgiaccan(n)'''

#Bai28
#Viết các hàm tính trả về phần tử trung vị (median), giá trị trung bình (mean), độ lệch chuẩn (standard deviation) của danh sách các giá trị.
'''def median(list):
    list.sort()
    if len(list)%2==0:
        return (list[int(len(list)/2)]+list[int(len(list)/2)-1])/2
    else:
        return list[int(len(list)/2)]

def mean(list):
    return sum(list)/len(list)

def standard_deviation(list):   
    mean1 = mean(list)
    sum1 = 0
    for i in list:
        sum1 += (i-mean1)**2
    return (sum1/len(list))**0.5

list = [1,5,2,3,4,6,7,8,9,10]
print('list:',list)
print('median:',median(list))
print('mean:',mean(list))
print('standard deviation:',standard_deviation(list))'''


#Bai29
'''def cuuchuong():
    for i in range(1,10):
        for j in range(1,10):
            print(j ,"*", i ,"=",i*j,end="  ")
        print(' ')

cuuchuong()'''

#Bai30
'''def chu(n):
    for line in range(1,n+1):
        print(str(line)*line)

n=int(input("nhap n so: "))
chu(n)'''

#Bai31
'''def gt_tu_dien(danhsach):
    kq=0
    for value in danhsach.values():
        kq+=value
    return kq

danhsach={'a':1,'b':2,'c':3, 'd':7}
sum=gt_tu_dien(danhsach)
print('tong cac gia tri trong tu dien la:',sum)'''

#Bai32
'''def tich_tu_dien(danhsach):
    kq=1
    for value in danhsach.values():
        kq*=value
    return kq

danhsach = {'a':5, 'gf':9, 'nv':12}
tich = tich_tu_dien(danhsach)
print('tich cac gia tri trong tu dien:',tich)'''

#Bai33
'''def tao_tudien():
    tudien = {}
    n = int(input('nhap so luong tu dien:'))
    for i in range(n):
        key = input('nhap khoa:')
        value = input('nhap gia tri cua khoa:')
        tudien[key] = value
    return tudien

def sort_tudien(list, reverse=False):
    if reverse:
        kq = sorted(list.values(),reverse=True)
        return kq
    else:
        kq = sorted(list.values())
        return kq

list = tao_tudien()
tong_giamdan = sort_tudien (list,reverse=True)
tong_tangdan = sort_tudien (list)
print('key va gia tri trong tu dien:',list)
print('gia tri giam dan:',tong_giamdan)
print('gia tri tang dan:',tong_tangdan)'''

#bai34
'''def concatenate(tudien1, tudien2):
    kq = tudien1.copy()
    kq.update(tudien2)
    return kq

tudien1 = {1:10, 2:20}
tudien2 = {3:30, 4:40}
tudiennoi = concatenate(tudien1, tudien2)
print('tu dien 1:',tudien1)
print('tu dien 2:',tudien2)
print('tu dien noi:',tudiennoi)'''

#bai35
'''def merge(tudien1, tudien2):
    kq = tudien1.copy()
    kq.update(tudien2)
    return kq

tudien1 = {'a':100, 'b':200}
tudien2 = {'a':300, 'y':200}
tudiennoi = merge(tudien1, tudien2)
print('tu dien 1:',tudien1)
print('tu dien 2:',tudien2)
print('tu dien noi:',tudiennoi)'''

#bai36
'''def combine(tudien1, tudien2):
    kq = {}
    for key in tudien1:
        if key in tudien2:
            kq[key] = tudien1[key] + tudien2[key]
        else:
            kq[key] = tudien1[key]
    for key in tudien2:
        if key not in kq:
            kq[key] = tudien2[key]
    return kq

tudien1 = {'a':100, 'b':200}
tudien2 = {'a':300, 'y':200}
tudiennoi = combine(tudien1, tudien2)
print('tu dien 1:',tudien1)
print('tu dien 2:',tudien2)
print('tu dien noi:',tudiennoi)'''

#bai37
'''def delete(tudien):
    kq = {}
    for key, value in tudien.items():
        if value not in kq.values():
            kq[key] = value
    return kq

tudien = {'a': 200, 'b': 200, 'c': 420, 'd': 300, 'e': 420}
tudienxoa = delete(tudien)
print('tu dien:',tudien)
print('tu dien noi:',tudienxoa)'''

#bai38
'''class sinhvien:
        def __init__(self, hoten, gioitinh):
            self.hoten = hoten
            self.gioitinh = gioitinh
        def diemdanh(self):
            print('Tôi là sinh viên')

class cntt(sinhvien):
        def diemdanh(self):
            print('Tôi là sinh viên CNTT')

class ttmmt(sinhvien):
        def diemdanh(self):
            print('Tôi là sinh viên TT-MMT')

sv1_sinhvien = sinhvien("Phan Van Chuan", "Nam")
sv2_cntt = cntt('Nguyen Thi Thu', 'Nu')
sv3_ttmmt = ttmmt('Le Quang Vinh', 'Nam')

sv1_sinhvien.diemdanh()
sv2_cntt.diemdanh()
sv3_ttmmt.diemdanh()'''

#Bai39
'''def doc_file(ten_teptin):
    try:
        f = open (ten_teptin, 'r', encoding='utf-8')
        print(f.read())
        f.close()
    except:
        print('khong tim thay file')

ten_teptin = "D:/tài liệu học kì 1 2023-2024/Python/test.txt"
doc_file(ten_teptin)'''

#Bai40
'''def doc_ndongtep(ten_teptin, n):
    try:
        f = open (ten_teptin, 'r', encoding='utf-8')
        for i in range(n):
            print(f.readline())
        f.close()
    except:
        print('khong tim thay file')

ten_teptin = "D:/tài liệu học kì 1 2023-2024/Python/test2.txt"
n = 6
doc_ndongtep(ten_teptin,n)'''

#Bai41
'''def noi_chuoi(ten_teptin, chuoi):
    try:
        f = open (ten_teptin, 'a', encoding='utf-8')
        f.write(chuoi)
        f.close()
        print('da noi chuoi vao cuoi tep tin')
    except:
        print('khong tim thay file')

ten_teptin = "D:/tài liệu học kì 1 2023-2024/Python/test.txt"
chuoi = 'them chuoi nay vao cuoi tep tin'
noi_chuoi(ten_teptin,chuoi)'''

#Bai42
'''def doc_ndongtep(ten_teptin, n):
    try:
        f = open (ten_teptin, 'r', encoding='utf-8')
        list = f.readlines()
        for i in range(len(list)-n,len(list)):
            print(list[i])
        f.close()
    except:
        print('khong tim thay file')

ten_teptin = "D:/tài liệu học kì 1 2023-2024/Python/test2.txt"
n=7
doc_ndongtep(ten_teptin,n)'''

#Bai43
'''def dem_dong_tu(ten_teptin):
    try:
        f = open (ten_teptin, 'r', encoding='utf-8')
        dong = 0
        tu = 0

        for line in f:
            dong += 1
            tu += len(line.split())

        f.close()

        print("Số dòng:", dong)
        print("Số từ:", tu)

    except:
        print('khong tim thay file')

ten_teptin = "D:/tài liệu học kì 1 2023-2024/Python/test2.txt"
dem_dong_tu(ten_teptin)'''

#Bai44
'''def tanso(ten_teptin):
    try:
        f = open (ten_teptin, 'r', encoding='utf-8')
        list = f.read().split()
        dict = {}
        for i in list:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        f.close()
        for key, value in dict.items():
            print(key, ':', value)
    except:
        print('khong tim thay file')

ten_teptin = "D:/tài liệu học kì 1 2023-2024/Python/test.txt"
tanso(ten_teptin)'''
        
