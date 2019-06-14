print("Welcome to Jugaadu Calculator")
print("enter A Number")
a=int(input())
print("Choose any one operation to perform on a and b")
print("add --> For addition\nsub --> For subtraction \nmul --> For Multiply \ndiv --> For Division \nmod --> For Modulus")
choose=str(input())
print("Enter Second Number")
if choose=="add":
    b=int(input())
    print(a+b)
elif choose=="sub":
    b=int(input())
    print(a-b)
elif choose=="mul":
    b=int(input())
    print(a*b)
elif choose=="div":
    b=int(input())
    print(a/b)
elif choose=="mod":
    b=int(input())
    print(a%b)
else:
    print("\t\t Invalid Operation")
    print("Please Open Your Headlight(Eyes) And Type Correct Operation.  \n\t\t   ThankYou")
    
