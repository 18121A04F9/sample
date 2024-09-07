def prime(num):
    count=0
    for i in range(2, num+1):
        if range%i==0:
            count+=1
    if count==2:
        return num
    else:
        return f"{num} is not a prime number"  
        

def comp_prime():
    res= [x for x in range(20) if x!=2 ]
    print(res)

res= prime(10)
print(res)