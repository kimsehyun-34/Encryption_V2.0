import os
maa= input("암호문: ")
ba=maa.split()
kegm=ba[0]
na=int(int(ba[1])/95673) #95673

kegm_s=""
kegm2=""
c=''
ac=0
for i in range(len(kegm)): #아스키코드 변경작업
    c=kegm[i]
    ac=ord(c)
    ac-=na
    c=chr(ac)
    kegm_s+=c
print("해독 결과: ",kegm_s)
os.system('pause') #모든 코드가 출력후 자동좋료르 방지 하기위해서 추가함
