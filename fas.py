# [
#   {
#     "W": 1.1,
#     "data": [
#       {
#         "l": 200,
#         "data": [
#               [0.32125, 178.23752305438424],
#               [0.3225, 177.64317512688294],
#               [0.32375, 177.04882719938166],
#               [0.325, 177.04882719938166]
#                  ]
#       },
#       {
#         "l": 250,
#         "data": [...]
#       }
#      ]
#   }
# ]
#
import copy
import numpy as np

import sys
from scipy import stats
from scipy import interpolate
from sys import argv
import json
import math
import matplotlib.pyplot as plt

def simpleLinearInterpolation (x, a, b):
    if b[1] == a[1]:
        return a[1]
    return a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0])

def findY(n, d):
    min = 0
    max = 0
    more = False
    for i, a in enumerate(d):
        if a[0] > n:
            max = i
            min = i - 1
            break
        if i > 200: # hack
            more = True
    if max == 0:
        if more:
            return d[len(d) - 1][1]
        else:
            return d[0][1]
    return simpleLinearInterpolation(n, d[max], d[min])



script, filename = argv

raw_data = open(filename)

data = json.loads(raw_data.read())

arr_ = []


# for chunk in data:
#     for l in chunk["data"]:
#         print(str(chunk["W"]) + "  " + str(l["l"]))
#         print(l["data"][0][0])

# print(stats.tmean(arr_))
# print(simpleLinearInterpolation(8., [2, 167], [12, 100]))

struct = copy.deepcopy(data)

# step 0.005   count 440  is optimal  mean = 418
r_ = np.arange(0.3, 2.505, 0.005)



for chunk in data:
    for l in chunk["data"]:
        d = l["data"]
        arrayXY = []
        for n in r_:
            arrayXY.append([n, findY(n, d)])
        l["data"] = arrayXY

# for chunk in data:
#     for l in chunk["data"]:
#         d = l["data"]
#         plt.plot([i[0] for i in d], [i[1] for i in d], 'r')

new_ = {}


for a in data[0]["data"][12]["data"]:
    new_[a[0]] = {}
    for v in [200, 250, 300, 400, 500, 600, 700, 800, 1000, 1250, 1500, 1750, 2000]:
    # for v in [1.1, 1.3, 1.6, 2, 2.5, 3, 4, 5]:
        new_[a[0]][v] = []


for chunk in data:
    for l in chunk["data"]:
        for a in l["data"]:
            new_[a[0]][l["l"]].append([chunk["W"], a[1]])

with open('data__.json', 'w') as outfile:
    json.dump(new_, outfile)


for  key, value in new_.iteritems():
    # print len(value)
    for key1, af in value.iteritems():
        plt.plot([i[0] for i in af], [i[1] for i in af], '.r')






# for l in data[0]["data"]:
#     d = l["data"]
#     plt.plot([i[0] for i in d], [i[1] for i in d], 'r')

# t = data[0]["data"][12]["data"]
# y = struct[0]["data"][12]["data"]
#
# plt.plot([i[0] for i in y], [i[1] for i in y], 'g')
# plt.plot([i[0] for i in t], [i[1] for i in t], 'r')
# print [i[1] for i in arrayXY]

# plt.plot([i[0] for i in d], [i[1] for i in d], 'r')
# plt.plot([i[0] for i in arrayXY], [i[1] for i in arrayXY], 'g')
plt.show()