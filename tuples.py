length = int(input())
nums = input().split(" ")
t = tuple()
for num in nums:
    t = t + (int(num),)
print(hash(t))