import numpy as np 
import math 
def dot_product(a,b):
    if len(a)!=len(b):
        raise ValueError("the lenghts of the arrays is different, can't dot product")
    i=0
    dot_sum=0
    while i<len(a):
        dot_sum+=a[i]*b[i]
        i+=1
    return dot_sum
def vector_lenght(numbers):
    sum_of_squares=0
    for number in numbers:
        sum_of_squares+=number**2
    result=math.sqrt(sum_of_squares)
    return result
def cos_similarity(a,b):
    length_a=vector_lenght(a)
    length_b=vector_lenght(b)
    if length_a==0 or length_b==0:
        raise ValueError("can't devide by zero")
    cosine_similarity=dot_product(a,b)/(length_a*length_b)
    return cosine_similarity
a=[1,2,3]
b=[2,3,4,5]
print(cos_similarity(a,b))

