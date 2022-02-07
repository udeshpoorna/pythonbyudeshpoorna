num = input("ENTER THE NUMBER:")
list_num = list(map(int, num))
h = sum (list_num)
niven=int(num)%h
div=int(num)/h
if int(niven)==0:
    print(div)
else:
    print("0")

