Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> name = "YK"
height_m = 2
weight_kg = 90
bmi = weight_kg / (height_m * height_m)
print ("bmi:")
bmi:
print (bmi)
22.5
if bmi < 25:
    print (name)
    print ("is not overweight")
else:
    print (name)
    print ("is overweight")
    
YK
is not overweight


name = "JOHN"
height_m = 1.75
weight_kg = 75
bmi = weight_kg / (height_m * height_m)
print ("bmi: ")
bmi: 
print (bmi)
24.489795918367346
if bmi < 25:
    print (name)
    print ("is not overweight")
else:
    print (name)
    print ("is overweight")
    
JOHN
is not overweight


name = "JANE"
height_m = 1.5
weight_kg = 65
bmi = weight_kg / (height_m * height_m)
print (bmi)
28.88888888888889
if bmi < 25:
    print (name)
    print ("is not overweight")
else:
    print (name)
    print ("is overweight")
    
JANE
is overweight