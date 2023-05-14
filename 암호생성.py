import os
kegm = input("문장: ")
na = int(input("+α 난이도(1~4200): ")) #아스키코드 증가값
ma=95673 #복호화에 사용할 아스키코드 증가값을 암호화 하기위한 수(변경가능)
kegm_s=""
c=''
ac=0
for i in range(len(kegm)): #아스키코드 변경작업
    c=kegm[i]
    ac=ord(c)
    ac+=na
    c=chr(ac)
    kegm_s+=c

naa=na*ma
print("암호화 결과: ",kegm_s,naa)
os.system('pause') #자동좋료르 방지 하기위해서 추가함
