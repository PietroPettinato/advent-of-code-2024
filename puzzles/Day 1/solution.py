# Day 1
# https://adventofcode.com/2024/day/1

import pandas as pd


####################
######  pt 1  ######
####################

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


####################
######  pt 2  ######
####################

df['l1_freq'] = df['l1'].map(df['l2'].value_counts())
# df['l2_freq'] = df['l2'].map(df['l2'].value_counts())

df['l1_sim'] = df['l1'] * df['l1_freq']
# df['l2_sim'] = df['l2'] * df['l2_freq']

# print(df)
print("Solution pt. 2 : ", int(df['l1_sim'].sum()))
