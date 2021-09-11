#Sec 1
w1=list("xyz")
w2=[x*n for n in range(1,5) for x in w1]
print(w2)
w3=[x*n for x in w1 for n in range(1,5)]
print(w3)

#Sec 2
no=[2,3,4]
n1=[[x+n] for x in no for n in range(0,3)]
print(n1)

#Sec 3
n2=[2,3,4,5]
n3=[[x+n for n in range(0,4)] for x in n2]
print(n3)

#Sec 4
n4=[1,2,3]
n5=[(b,a) for a in n4 for b in n4]
print(n5)