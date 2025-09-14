nums=[2,7,11,15]
target = 9
answer=[]
for x in range(len(nums)):
    for y in range(len(nums)):
        if (nums[x]+nums[y]==target) and len(answer)<2 and (x!=y):
            answer.append(x)
            answer.append(y)
            print(answer)
