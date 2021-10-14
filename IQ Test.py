while True:
    
    iq = input("IQ Level= ")
    if int(iq)<=69:
        print("您的智力缺陷")
    elif 79>=int(iq)>=70:
        print("您的智力不足")
    elif 89>=int(iq)>=80:
        print("您的智力中下")
    elif 109>=int(iq)>=90:
        print("您的智力中等")
    elif 119>=int(iq)>=110:
        print("您的智力中上")
    elif 139>=int(iq)>=120:
        print("您的智力优秀")
    elif int(iq)>=140:
        print("您是天才")
    else:
        print("出错")