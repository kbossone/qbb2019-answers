#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

def sim( n,p,trials,s):
    pops= n
    # a_freq= 0.5
    trials= 1000
    gen_list=[]
    for gen in range(trials):
        a_freq= p
        gen_counter= 0
        while True:
            numoffspring = np.random.binomial(n=(pops*2), p= a_freq)
            a_freq = (numoffspring * (1 + s)) / (( 2 * pops) - numoffspring + numoffspring * ( 1 + s ))
            gen_counter += 1
            #print(a_freq)
            if (a_freq == 0) or (a_freq==1):
                break
        gen_list.append(gen_counter)
    return(gen_counter)


# Plots histogram for part1
# fig, ax=plt.subplots(tight_layout=True)
# plt.hist(gen_list)
# ax.set_xlabel("Number of generations")
# fig.savefig("Part1")
# plt.show()
# plt.close(fig)

# Part2 stuff
# sizes = [5,10,100,1000,10000]
# values = []
# for number in sizes:
#     values.append(sim(number,0.5,1000))
#     print(values)
# fig, ax=plt.subplots(tight_layout=True)
# plt.scatter(x=sizes,y=values)
# ax.set_xlabel("Population size")
# ax.set_ylabel("Number of generations")
# fig.savefig("Part2")
# plt.show()
# plt.close(fig)

# Part 3 stuff
# a_freq= [0.1, 0.3, 0.5, 0.7, 0.9]
# values={}
# for val in a_freq:
#     a= sim(100, val, 100)
#     values[val]= a
#
# for key in a_freq:
#     for j in values[key]:
#         plt.scatter(x=key, y=j, alpha= 0.3)
# plt.show()

# Part 4 stuff
sel = []
 
for i in range(200):
    sel.append(0.002 * i - 0.2)
    
gen = []
for j in sel:
    k = sim(200, 0.5, 1, j)
    gen.append(k)

fig, ax = plt.subplots()
ax.scatter(sel, gen, s= 4)
ax.set_xlabel("Selection coefficient")
ax.set_ylabel("Number of generations")
fig.savefig("Part4.png")
plt.close(fig)