def sum_of_prime(initial,final):
    sum=0
    for i in range(initial,final+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                sum=sum+i
    return(sum)
print(sum_of_prime(1,6))