"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of cities
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of cities)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def sortUSA():
    '''Return all the cities in the USA in alphabetical order'''
    USAlist= locations['North America']['USA']
    USAlist.sort()
    return USAlist

def alphaAsia():
    
    '''Return all the cities in Asia continent in alphabetical order'''
    Asialist= locations['Asia']
    countrydictlist=[]
    citylist=[]
    countrydictlist.append(locations['Asia'])
    for dictionary in countrydictlist:
        countrylist = list(dictionary.keys())
        citylist_ = list(dictionary.values())
        # citylist_.append
    for i in range(0,len(citylist_)):
        citylist.append(citylist_[i][0])
    citylist.sort()
    # for i in citylist:
    result =[]
    for i in citylist:
        
        print(i)
        x= ''
        x += i 
        print(x)
        x += " - " 
        x+= countrylist[(citylist.index(i))]
        print('x:',x)
        result.append(x)
        print(result)
            # x = i
        
    
    return result
    

    # return ['Bangalore - India', 'Shanghai - China']



# Note: Check for test cases to understand the output format.
locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia']={'India':['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa']={'Egypt':['Cairo']}
locations['Asia']['China']=['Shanghai']

print(sortUSA(), alphaAsia())