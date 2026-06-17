# # There are several types of data within python 
# # Example: integer,float,bool etc.
# #integer 
a=56
print (type (a))
# floating 
b=7.5
print(type(b))
# #booling 
b=67
print(bool(b))
# bool as long as a value is present or a word will always show true 
#Example 
a=17
print(bool(a))
# # ARETHEMETIC OPRERATORS 
a=4
b=7
# operators show funtions such as 
# addition is denoted +
print(a+b)
# substraction is denoted by -
print(a-b)
# multiplication is denoted by *
print(a*b)
# # divison /
print(a/b)
# exponents are deenoted by **
print(a**b)
# floor divison denoted by (\\)
print(a//b)
# Modules is denoted by %
# Modulus divides the give number and shows reminder 
print(a%b)

# # COMPARISON OPERATORS
# # Equel to ==
# # the results shown in this operators will be shown by booling 
# # example 
a= 3 
b=6
print(a==b)
# not equel to !=
# example 
a=4
b=6
print(a!=b)
# # greaterthan <
print(a<b)
# # lessthan >
print(a>b)
# # greater than or equel to <=
print(a<=b)
# # lessthan or equel to >=
print(a>=b)

# Condition statement 
# helps prove a fuction is working in the given conditions 
# Example 
age=2
if age >= 18 :
    print("Eligible")
else :
    print("not eligible ")
# check if number is odd or even 
num=132345
if num%2==0:
    print("even")
else :
    print("odd")

# multile of 5 
num=50
if num%5==0:
    print("miltiple of 5") 
else:
    print("not multiple of 5")

 # multiple condition 
num=-9
if num>0:
    print("positive")
elif num<0:
    print("negative")

# logical operators 
# it is ued to say if multiple conditions are 
a=10 
b=11
c=100

if a>b and a>c :
    print(" a is the largest ")
elif b>a and b>c :
    print(" b is the largest")
else:
    print("c is the largest")
# another way to use logical operators are by using or 
num=80
if num%2==0 or num//2==40 :
    print("the number given is divisible by 2 ")
# number is mutiple of 3 and 5 
a=30
b=55
if a%3==0 and a%5==0:
    print("a is a multiple of 3 and 5 ")
elif b%5==0 and b%3==0:
    print ("b is multiple of 3 and 5 ")
else :
    print(" a and b are both not multiples of 3 and  5" )

