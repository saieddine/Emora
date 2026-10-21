import numpy as np
import math 

def vector_lenght(numbers):
    sum=0
    for number in numbers:
        sum+=number**2
    result=math.sqrt(sum)
    return result
a=np.array([1,2,3])
b=np.array([2,3,4])
print(vector_lenght(a))
print(vector_lenght(b))
cos_similarity=np.dot(a,b)/(vector_lenght(a)*vector_lenght(b))
print(cos_similarity)

