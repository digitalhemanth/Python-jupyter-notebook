#1. Python Program to Reverse a Number

def numres(num : int) -> int:
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10    
    
    return reversed_num

print(numres(12345))


#2. Python Program to Reverse a number using sclicing 

number  = 11211
if str(number) == str(number)[::-1]:
    print(number)
else:
    print('Not a palindrom')
    
    
    
    
# Python program to check if the number is an Armstrong number or not

num = 153
sum = 0
tmp = num
while tmp>0:
    digit = tmp%10
    sum = sum+digit**3
    tmp //=10
if num==sum:
    print(num)
else:
    print("Try again")