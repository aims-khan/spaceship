print("nultipling even numbers in 2")
print("")
numbers = [1,2,3,4,5,6,7,8,9,10]
result=1
for x in numbers:
    if x %2!=1:
        result= x * 2

    print(result)

print("_______________________________________________________________________")
print("")
print("nultipling even numbers with each other")
print("")
numbers1 = [1,2,3,4,5,6,7,8,9,10]
result1=1
for y in numbers:
    if y %2!=1:
        result1= y * result1

    print(result1)