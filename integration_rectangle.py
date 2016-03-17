# Integration by rectangle
# Python3
# by Xellor
# Last update 17.03.2016
print("Enter values for ax^2+bx+c")
a1 = int(input("Enter a "));
b1 = int(input("Enter b "));
c1 = int(input("Enter c "));
def f(x):
      return a1*x**2+b1*x+c1;
a = int(input("Enter 1-st point: "));
b = int(input("Enter 2-st: point: "));
e = int(input("Enter Epsilon: "));
ss = 0
n = (b - a) / e
x1 = a
for i in range(int(n)):
      s = f(x1) * e
      ss = ss + s
      x1 = x1 + e
print (ss)