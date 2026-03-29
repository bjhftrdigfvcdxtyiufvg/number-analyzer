type=["Prime","Odd","Even","Armstrong","Perfect square","Palindrome","natural number","whole number","perfect number","Strong number"]
print("enter a number")
number=int(input())
def digits(n): 
    dig=[]
    while n>0:
        dig.append(n%10)
        n=n//10
   
    return (dig)
   
def prime(n):
    count=0
    for x in range(1,n+1,1):
        if n%x==0:
            count+=1
        else:
            continue
    if count==2:
        return (True)
    else :
        return (False)
def armstrong(n):
    sum=0
    dig=digits(n)
    for y in range(0,len(dig),1):
        sum+=(dig[y]*dig[y]*dig[y])
    if n==sum:
        return (True)
    else :
        return(False)
def perfectSquare(n):
    dig=digits(n)
    for c in range(1,(n//2)+1,1):
        if c*c==n:
            return (True)
        else :
            continue
def palindrome(n):
       dig=digits(n)
       
       rev=0
       for r in range(0,len(dig),1):
         rev=rev*10+dig[r]
       if rev==n:
         return (True)
       else:
         return(False)

if prime(number)==True:
    print(type[0])
if  armstrong(number)==True:
    print(type[3])
if perfectSquare(number)==True:
    print(type[4])    
if palindrome(number)==True:
    print(type[5])



    



        

