kegm = input("문장: ")
na = int(input("난이도(~600): ")) #아스키 코드 증가값 조절가능 (난이도)

kegm_s=""
kegm2=""
c=''
ac=0
for i in range(len(kegm)):
    c=kegm[i]
    ac=ord(c)
    ac+=na #아스키 코드 +30 
    c=chr(ac)
    kegm_s+=c

print("암화 결과: ",kegm_s)
print("난이도 :",na)