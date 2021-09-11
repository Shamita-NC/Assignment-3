#Problem1.1
def mult(n1,n2):
    return n1*n2

def myreduce(func,seq):
    result=seq[0]
    for i in seq[1:]:
        result=func(result,i)
    return result

print(myreduce(mult,[1,2,3,4]))