print("Question 1")
print("Table of 10")
for n in range(1,11):
    n*=10
    print(n)


print("\n")
print("Question 2")
print("Enter Integer Value for Table")
m=int(input())
for n in range(1,11):
    n*=m
    print(n)


print("\n")
print("Question 3")
print("Table of series from 2 to input values")
print("set input")
a=int(input())
for n in range(2,a+1):
    print("table of ",n)
    for m in range(1,11):
        t=m*n
        print("%s * %s = %s" %(n,m,t))
    print("\n")


