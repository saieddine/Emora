def dot_product(a,b):
    if len(a)!=len(b):
        raise ValueError("the lenghts of the arrays is different, can't dot product")
    i=0
    dot_sum=0
    while i<len(a):
        dot_sum+=a[i]*b[i]
        i+=1
    return dot_sum
array_a=[1,2,3]
array_b=[2,3,4]
print(dot_product(array_a, array_b))    
