import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
from matplotlib import cm

csv_file = open("data.csv")

reader = csv.reader(csv_file)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_ = []
y_ = []
z_ = []
c_ = []

# exclude headers
reader.next()

for i in reader:
    if float(i[0]) == 1.3:
        break
    x_.append(float(i[1]))
    c_.append(float(i[1]))
    y_.append(float(i[2]))
    z_.append(float(i[3]))

x = []
y = []
z = []
c = []

x.append(x_[0])
y.append(y_[0])
z.append(z_[0])
c.append(c_[0])


for i, o in enumerate(x_):
    if i%5 == 0:
        x.append(x_[i])
        y.append(y_[i])
        z.append(z_[i])
        c.append(c_[i])

xx = []
yy = []
zz = []
cc = []
prev_c = 200.

# for i, w in enumerate(x):
#     if prev_c != c[i]:
#         ax.plot(xx, yy, zz)
#         xx = []
#         yy = []
#         zz = []
#     prev_c = c[i]
#     xx.append(x[i])
#     yy.append(y[i])
#     zz.append(z[i])
#     cc.append(c[i])

X = []
Y = []
Z = []

for i, w in enumerate(x):
    if prev_c != c[i]:
        X.append(xx)
        Y.append(yy)
        Z.append(zz)
        xx = []
        yy = []
        zz = []
    prev_c = c[i]
    xx.append(x[i])
    yy.append(y[i])
    zz.append(z[i])

# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)


plt.show()
