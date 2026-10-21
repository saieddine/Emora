import numpy as np 
import math

a=np.array([1,2,3])
b=np.array([2,4,5])
dot=np.dot(a,b)
sum_a=0
sum_b=0
for number in a :
    sum_a+=number**2
for number in b:
    sum_b+=number**2
length_a= math.sqrt(sum_a)
length_b= math.sqrt(sum_b)

cos_similarity=dot/(length_a*length_b)
print(cos_similarity)
