#WAP FOR FINDING THE LCM OF THE 2 NUMBERS 
"""
LCM=(a*b)/GCD(a,b)
"""
a1=int(input("Enter Number 1 : "))
b1=int(input("Enter Number 2 : "))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)

print(lcm(a1,b1))
