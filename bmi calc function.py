Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import random
import sys
import os

name1 = "YK"
height_m1 = 1.5
weight_kg1 = 50

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 1.9
weight_kg3 = 95

def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print ("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
    
result1 = bmi_calculator(name1, height_m1, weight_kg1)
bmi: 22.22222222222222

result2 = bmi_calculator(name2, height_m2, weight_kg2)
bmi: 21.604938271604937

result3 = bmi_calculator(name3, height_m3, weight_kg3)
bmi: 26.315789473684212

print (result1)
YK is not overweight
print (result2)
YK's sister is not overweight
print (result3)
YK's brother is overweight