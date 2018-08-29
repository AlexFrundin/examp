#numbers = [i for i in range(1,10)]
# def add(a,b):
#     return a+b
# numbers = [1,2,3,4,5,6,7]
# num = list(map(add,numbers,numbers))

st="16724618264981hgfeehwgfhwgjf271471827017924gfdhsgfr3327481723"
st_digit=[]
st_symbol=[]
# def parse(h):
#     try:
#         st_digit.append(int(h))
#     except:
#         st_symbol.append(h)
#
# [parse(i) for i in st]
# print(st_digit)
# print(st_symbol)
for i in st:
    try:
        st_digit.append(int(h))
    except:
        st_symbol(h)
for i in st:
    if i.isdigit():
        st_digit.append(int(i))
    else:
        st_symbol.append(i)
