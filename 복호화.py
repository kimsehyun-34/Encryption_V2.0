na= int(input("난이도: "))
kegm = input("암호문: ")

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