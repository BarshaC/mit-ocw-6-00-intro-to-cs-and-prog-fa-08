def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # End of year 1 -->   F[0] = salary * save * 0.01
    # End of year 2 -->   F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
    # End of year 3 --> F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01
    
    # TODO: Your code here.
    answer = [0]
    for each in range(0,years):
        #print each
        temp = answer[-1] * (1 + 0.01 * growthRate) + salary * save * 0.01
        answer.append(temp)
        #print answer
    del answer[0]
    print (answer)

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    salary     = 40000
    save       = 12
    growthRate = 7
    years      = 20
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)

    salary     = 80000
    save       = 12
    growthRate = 7
    years      = 20
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
testNestEggFixed()
