import os
import random

a = str(input("입력: "))
if a == "e":
    kegm = input("문장: ")
    na = random.randrange(152, 1150)
    ma = 95673
    kegm_s = ""
    kegm2 = ""
    c = ""
    ac = 0
    for i in range(len(kegm)):
        c = kegm[i]
        ac = ord(c)
        ac += na
        c = chr(ac)
        kegm_s += c

    naa = na * ma
    print("암호화 결과: ", kegm_s, naa)
elif a == "d":
    maa = input("암호문: ")
    ba = maa.split()
    kegm = ba[0]
    na = int(int(ba[1]) / 95673)  # 95673

    kegm_s = ""
    kegm2 = ""
    c = ""
    ac = 0
    for i in range(len(kegm)):
        c = kegm[i]
        ac = ord(c)
        ac -= na
        c = chr(ac)
        kegm_s += c
    print("해독 결과: ", kegm_s)

os.system("pause")
