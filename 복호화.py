import os
maa= input("암호문: ")
ba=maa.split() #입력한 암호문을 공백을 기준으로 나누어 저장함
kegm=ba[0] #저장한 변수중 0번 변수를 kegm에 저장함
na=int(int(ba[1])/95673) #암호키 계산 작업,95673로 나누어 계산함

kegm_s=""
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
