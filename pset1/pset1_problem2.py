import math    #import some math modules which we will use here

def nthprime(n):
    sum = math.log(2) #as 2 is first prime and not included the following loop
    for num in range(3,n,2):
        check = 0   
        for divider in range(1,num+1):
            if num%divider == 0: check += 1 
        if check == 2:  #here check remains 2 only and only for primes as primes are divided exactly by 1 and themselves only  
            sum = sum + math.log(num)
    print ("Sum of logs of primes equals " + str(sum))
    print ("Number is " + str(n))
    print ("Ratio of sums of logs of prime to number n will equal to " + str(sum/n))
nthprime(int(raw_input("Enter the number up to which log of primes is to be summed up ")))

#Some observation of this problem
#greater the number you enter the closer the value of the ratio
#the ratio rises non monotonically 
