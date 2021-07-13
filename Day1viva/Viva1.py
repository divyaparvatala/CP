def generate_series(n):
    
    for i in range(1, n+1):
        alist =[]
        count = 0
        while count<i:
            alist.append(i+count)
            count+=1
    print(alist)

        
def series(n):
    for i in range(1, n+1):
        print(generate_series(i))

print(series(5))

# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9 