#equations for this case uses diophantine equation 6a + 9b + 20c = n
#where n is the number of nuggets which can be given with the possible packages of 6, 9 and 20.

#Problem 1

def diophantine(nug):
    sum = 0
    min = 0
    max = 61
    small = 6
    medium = 9
    large = 20
    l = tuple()
    #print ("These combinations make the required packages :")
    for n in range(0,70):
        a_bound = int((n/small) + 1)
        b_bound = int((n/medium) + 1)
        c_bound = int((n/large) + 1)
        for a in range(0,a_bound):
            #limits loop for the values of a,b and c taken
            for b in range(0,b_bound):
                for c in range(0,c_bound):
                    if 6 * a + 9 * b + 20 * c == n and n not in l and n >= nug[0] and n <= nug[-1]:
                    #print(str(sum) + " = " + "6 *" + str(a) + " +  9 *" + str(b) +  " +  20 * "  + str(c))
                        l += (n,)

    return l
list1 = (50,51,52,53,54,55)
list1 = (56,57,58,59,60)
diophantine(list1)
#Problem 2
#When x can be generated x + 1 , x + 2, x + 3... can be generated.
#which proves the numbers infinite such number starting from x can be generated
#hence following 50,51,52,53,54 were possible to generated hence other following numbers are also possible to generate

#Problem 3
def largest_pack():
    num  = 0
    check_lst = []
    min = 0
    max = 61
    small = 6
    medium = 9
    large = 20
    for n in range(min,max):  #makes sure there is no exhaustive looping
        a_bound = int((n/small) + 1)
        b_bound = int((n/medium) + 1)
        c_bound = int((n/large) + 1)
        for a in range(0,a_bound):
            for b in range(0,b_bound):
                for c in range(0,c_bound):
                     if 6 * a + 9 * b + 20 * c == n and n not in check_lst:
                        check_lst.append(n)
                        check_lst.sort()
    for i in range(0,61):
        if i not in check_lst:
            num = i
    return ("The largest package that can be generated is " + str(num))
largest_pack()

#Problem 4
packages = (6,9,20)
packages2 = (16,19,20)
packages3 = (7,15,20)
packages4 = (11,16,20)
packages5 = (4,9,16)
packages6 = (9,12,50)

six_packages = (packages,packages2,packages3,packages4,packages5,packages6)
packages_to_be_tested = len(six_packages)

def largest_possible_package(packages):
    check_lst = []
    small = packages[0]
    medium = packages[1]
    large = packages[2]
    for n in range(0,200):  #as stated in question- will be checking possible nuggests of 200
        for a in range(0, int((n/small) + 1)):
            for b in range(0,int((n/medium) + 1)):
                for c in range(0,int((n/large) + 1)):
                    if packages[0] * a + packages[1] *b + packages[2] * c == n and n not in check_lst:
                        check_lst.append(n)
                        check_lst.sort()
    for i in range(0,200):
        if i not in check_lst:
            num = i
    return num
def test_all_packages():
    for index in range(packages_to_be_tested):
        answer = largest_possible_package(six_packages[index])
        print ("Given package sizes " + str(packages[0]) + ","  + str (packages[1]) + 'and ' + str(packages[2]) + " the largest number of nuggets that cannot be baught is: " + str(answer))
test_all_packages()










            
