# This is python practice problem for learning sake https://codingbat.com/prob/p145834
# Given a string, return the count of the number of times that a 
# substring length 2 appears in the string and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring)
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2 (str):
    count = 0
    leng = len(str)
    if leng <2:
     return (count)
    laststr = str[leng-2] + str[leng-1]
    for i in range (leng-2):
        sub = str[i] + str [i+1]
        if sub == laststr:
            count=count + 1
    return (count)

print (last2('hixxhi'))
print (last2('xaxxaxaxx'))
print(last2('q1'))
print (last2('axxxaaxx'))