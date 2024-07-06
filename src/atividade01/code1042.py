# -*- coding: utf-8 -*-

nums = [int(x) for x in input().strip().split(' ')]
nums_inv = nums[:]

nums_inv.sort()

for i in range(0, 3):
    print(nums_inv[i])
    
print()

for i in range(0, 3):
    print(nums[i])