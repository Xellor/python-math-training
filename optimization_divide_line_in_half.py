# Optimization (divide line in half)
# Python3
# by Xellor
# Last update 17.03.2016
m = int(input("Enter <1> - min; <-1> - max: "));
print("Enter values for: ax^2+bx+c")
a = int(input("Enter a "));
b = int(input("Enter b "));
c = int(input("Enter c "));
f = lambda x: a * x ** 2 + b * x + c;
x1 = float(input("Enter 1-st point: "));
x2 = float(input("Enter 2-st point: "));
e = float(input("Enter Epsilon: "));
while True:
      x = (x1 + x2) / 2
      n = x - e
      m = x + e
      if f(n) * m < f(m) * m:
            x2 = x
      else:
          x1 = x
      if (x2 - x1) < e:
            break
x = (x2 + x1) / 2
print("Point: " + str(x) + " cut: " + str(f(x)))