# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    # Your code goes here...
    # return ""
    a = data.split("\n")
    a.pop()
    datalist =[]
    for i in a:
        x = i.split(",")
        datalist.append(x)
    namelist =[]
    maxlist = []

    for i in datalist:
        namelist.append(i[0])
        i.pop(0)
        for j in i:
            j = int(j)
        m = max(i)
        maxlist.append(m)

    # x =  namelist[maxlist.index(max(maxlist))]
    x = max(maxlist)
    res =[]
    i = 0
    while i<len(maxlist):
        print('==============================')
        print(maxlist[i], x)
        if maxlist[i] == x:
            print('------------',i)
            res.append(namelist[i])
            i+=1
        else:
            i+=1

        # if len(res)==1:
        #     return res[0]
        # else:
        # print(res)
        print(maxlist, namelist, res)
        return ','.join(res)
# print(topScorer(data))

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''

# print(topScorer(data))
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
print(topScorer(data))
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
