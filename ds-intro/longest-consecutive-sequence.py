def _longest_concecutive_sequence(arr):
    dt = {} 
    vis = {}

    for num in arr:
          dt[num] = True 

    ml = 0
    for num in dt.keys():
        if num+1 in vis:
            continue

        l=1
        while num+1 in dt:
            vis[num+1] = True
            l+=1  
            num+=1

        ml = max(l, ml)

    return ml

def longest_concecutive_sequence(arr):
    dt = {} 
    vis={}

    for num in arr:
          dt[num] = True 

    ml = 0
    for num in dt:
        if num in vis:
            continue

        while num - 1 in dt:
            num -= 1
        
        l = 1
        while num+1 in dt:
            vis[num] = True
            num+=1
            l += 1

        ml = max(l, ml)

    return ml
        
inp = [1,4,2,7,5,6,8,11,12,88,85,86,3,87,89,90]
print(longest_concecutive_sequence(inp))

