#PROBLEM 1 withou using find()

def countsubStringMatch(target,key):
    key_length = len(key)
    loop = len(target)-key_length + 1   #limits the number of loop according to the length of target and key
    start = 0          #this has be 0 first letter always has index 0
    end = key_length    #this sets index upto which the slicing has to be done
    list_sample = list()
    count = 0
    for i in range(0,loop):
        sample = target[i:end]   #here target[0:4] will give atgc
        list_sample.append(sample)   #adds 4 length string sliced from target
        if sample == key:
            count += 1
            return count
        else:
            return -1
        start += 1
        end += 1
countsubStringMatch("atgacatgcacaagtatgcat", "atgc")

#PROBLEM 1 using find() Second solution for problem 1
#this is shorter and easier and convinient
from string import *
def countsubStringMatch(target,key):
    count = 0  #this keeps the count of the instances the string has appeared in the target
    start = 0
    result = str.find(target,key,start)
    while result != -1:
        count += 1
        start = str.find(target,key,start) + 1
    return count
#problem 1 using recursion
def countsubStringMatchRecursive(target,key):
    count = 0  #initially there are no count
    sample_index = str.find(target,key)
    if sample_index != -1:
        count = 1 + countsubStringMatchRecursive(target[sample_index+1:],key) #here it looks for another match from anext index point after matching first one
        return count
    else:
        return count  #this returns total count
#Problem 2
def subStringMatchExact(target,key):
    indexes_of_key = list()  #obtains list of indexes of string that matches the key
    start = 0
    result = str.find(target,key,start)
    while result != -1:   #loop proceeds only when the key is present in the target else returns None
        indexes_of_key.append(result)
        start = str.find(target,key,start) + 1
        result = str.find(target,key,start)
    return tuple(indexes_of_key)      #returns result in form of tuple which are immutable
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
subStringMatchExact("atgacatgcacaagtatgcat",key10)


#Problem 3
def constrainedMatchPair(firstMatch,secondMatch,length):
    match_pair = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                match_pair += (n,)
    return match_pair

target1 = "atgacatgcacaagtatgcat"
key_to_test = "atg"
def subStringMatchExact(target,key):
    match_pair_tuple = ()
    start = 0
    while str.find(target, key, start) >= 0:
        start = str.find(target,key,start)
        match_pair_tuple += (start,)
        start += 1
    return match_pair_tuple
def subStringMatchOneSub(key,target):
    result = ()
    for location in range(0,len(key)):
        key1 = key[:location]
        key2 = key[location+1:]
        print 'breaking key', key, ' into ' , key1 ,key2
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        matching_pair = constrainedMatchPair(match1,match2,len(key1))
        result = result + matching_pair
        print ('match1', match1)
        print ('match2',match2)
        print 'possible matches for ' + str(key1) +' and ' + str(key2) +  ' start at  ' + str(matching_pair)
    return result
#print (subStringMatchOneSub(key_to_test,target1))