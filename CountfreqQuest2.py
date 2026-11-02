def  count_pairs(arr,D,M):
    freq={}
    ans=0
    for x in arr:
        remM= x % M
        remD= x % D

        need=(D-remD) % D

        ans += freq.get((remM,need),0)

        key=(remM,remD)
        freq[key]=freq.get(key,0)+1
    return ans 
    

arr = [8, 2, 4]
D = 3
M = 4

print(count_pairs(arr,D,M))