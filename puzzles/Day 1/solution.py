# Day 1
# https://adventofcode.com/2024/day/1

import pandas as pd

l1 = []
l2 = []
with open('advent-of-code-2024\puzzles\Day 1\input.txt') as f:
    for line in f.readlines():
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[-1]))

l1.sort()
l2.sort()
# print(l1)
# print("\n")
# print(l2)

df = pd.DataFrame({'l1':l1, 
                   'l2':l2}) 
df['distance'] = abs(df['l1'] - df['l2'])

print("Solution pt. 1 : ", df['distance'].sum())
