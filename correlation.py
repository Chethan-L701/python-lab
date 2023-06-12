import math

x = []
y = []
print("Enter the number of data sets ")
n = int(input())
for i in range(n):
    print("Enter the data set ", i+1)
    x.append(int(input("x{}: ".format(i+1))))
    y.append(int(input("y{}: ".format(i+1))))


def mean(data):
    sum = 0
    for i in data:
        sum = sum+i
    return sum/len(data)


def sumation(data):
    sum = 0
    for i in data:
        sum = sum+i
    return sum


def correlation(XYSum, XSquSum, YSquSum):
    return XYSum/math.sqrt(XSquSum*YSquSum)


print(x, y)
print("x\ty\tX\tY\tX*Y\tX^2\tY^2")
xmean = mean(x)
ymean = mean(y)
X = list(map(lambda x: x-xmean, x))
Y = list(map(lambda y: y-ymean, y))
XSum = sumation(X)
YSum = sumation(Y)
XSquSum = sumation(map(lambda x: x*x, X))
YSquSum = sumation(map(lambda y: y*y, Y))
XY = list(map(lambda x, y: x*y, X, Y))
XYSum = sumation(XY)
corr = correlation(XYSum, XSquSum, YSquSum)

for i in range(n):
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}"
          .format(x[i], y[i], X[i], Y[i], XY[i], X[i]**2, Y[i]**2))

print("x mean = {}".format(xmean))
print("y mean = {}".format(ymean))
print("X sum = {}".format(XSum))
print("Y sum = {}".format(YSum))
print("X*Y sum = {}".format(XYSum))
print("X^2 sum = {}".format(XSquSum))
print("Y^2 sum = {}".format(YSquSum))
print("correlation = {}".format(corr))
