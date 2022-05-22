import os
maa= input("암호문: ")
ba=maa.split()
kegm=ba[0]
na=int(int(ba[1])/9567) #9567

kegm_s=""
kegm2=""
c=''
ac=0
for i in range(len(kegm)):
    c=kegm[i]
    ac=ord(c)
    ac-=na
    c=chr(ac)
    kegm_s+=c
print("해독 결과: ",kegm_s)
os.system('pause')