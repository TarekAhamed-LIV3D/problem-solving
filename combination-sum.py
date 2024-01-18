def combinationSum2(candidates, target):
    res = []
    candidates.sort()
            
    def dfs(summ, index, path):
        if summ > target:
            return
        if summ == target:
            res.append(path)
            return 
        for i in range(index, len(candidates)):
            dfs(summ+candidates[i], i, path+[candidates[i]])
    dfs(0,0,[])
    return res

candidates2 = [2, 3, 5]
target2 = 8
result2 = combinationSum2(candidates2, target2)

print("\nExample 2:")
print(result2)