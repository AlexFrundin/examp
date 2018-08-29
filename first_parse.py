stroka="154fjgkjadsghfkjsdgfk676573hfjdjsf90900jfdh"
stroka2="teyrt7658236587fhdj734hjhhj9999"
stroka3="7321878244612476127461286481641286"
stroka4="kjkhfjahdskjgahskljghkasjhgkjah"

def create_array(st):
    i=0
    mas=[]
    while i<len(st):
        if st[i].isdigit():
            tmp=i
            while st[i].isdigit():
                i+=1
                if i>=len(st):
                    break
            mas.append(st[tmp:i])
        i+=1
    return mas

array = create_array(stroka)

for i in range(len(array)):
    array[i]=int(array[i])
    print(type(array[i]))
