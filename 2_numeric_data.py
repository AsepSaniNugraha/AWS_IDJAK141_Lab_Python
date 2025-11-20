print("Python has three numeric types: int, float, and complex")

myInteger=1
print(myInteger)
print(type(myInteger))
print(str(myInteger) + " is of the data type " + str(type(myInteger)))

myFloat=3.14
print(myFloat)
print(type(myFloat))
print(str(myFloat) + " is of the data type " + str(type(myFloat)))

myComplex=5j
print(myComplex)
print(type(myComplex))
print(str(myComplex) + " is of the data type " + str(type(myInteger)))

myBoolean1=True
print(myBoolean1)
print(type(myBoolean1))
print(str(myBoolean1) + " is of the data type " + str(type(myBoolean1)))

myBoolean0=False
print(myBoolean0)
print(type(myBoolean0))
print(str(myBoolean0) + " is of the data type " + str(type(myBoolean0)))

print("+++++++++++")
myData=[1,3.14,5j,True,False]

for data in myData:
    print(data)
    print(type(data))
    print(f"{data} is of the data type {type(data)}\n")