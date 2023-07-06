# 1. Read the inputs
nums = input().split(' ')

n = nums[0]
m = nums[1]
k = nums[2]

# 2. Evaluate the parameters
if int(n)/int(k) >= int(m):
    print("Iron fist Ketil")
else:
    print("King Canute")