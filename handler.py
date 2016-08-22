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
from sys import argv
import json

import numpy as np
import matplotlib.pyplot as plt

script, filename = argv

raw_data = open(filename)

data = json.loads(raw_data.read())

# for chunk in data:
#     print("j1/j2 = " + str(chunk["W"]))
#     for l in chunk["data"]:
#         print("W=" + str(chunk["W"]) + ";\t" + "l=" + str(l["l"]) + ";\t\t\t" + "countOfPoints=" + str(len(l["data"])) + ";" )

x = []
y = []


for chunk in data:
    chunk = data[7]
    for l in chunk["data"]:
        for a in l["data"]:
            x.append(a[0])
            y.append(a[1])
        x = np.array(x)
        y = np.array(y)
        plt.plot(x, y, 'g')
        x = []
        y = []
    chunk = data[0]
    for l in chunk["data"]:
        for a in l["data"]:
            x.append(a[0])
            y.append(a[1])
        x = np.array(x)
        y = np.array(y)
        plt.plot(x, y, 'r--')
        x = []
        y = []
    # break


plt.show()

