# Interpolation (linear method)
# Python3
# by Xellor
# Last update 16.03.2016
x_values = input('Enter Xi values (1,2,3,..,n): ')   # input Xi values,
x_values = x_values.split(',')                       # number of values Xi == Yi
x_values_len = len(x_values)
y_values = input('Enter Yi values (1,2,3,..,n): ')   # inpur Yi values
y_values = y_values.split(',')
y_values_len = len(y_values)
xt = float(input('Enter Xt (Xi to find): ')) # input xt (x to find)
x1 = float(xt)
x2 = float(xt)
for i in range(x_values_len):     # search x1, y1
    if float(x_values[i]) < x1:
        continue
    else:
        x1 = float(x_values[i - 1])
        y1 = float(y_values[i - 1])
        break
for i in range(x_values_len):     # search x2, y2
    if float(x_values[i]) < x2:
        continue
    else:
        x2 = float(x_values[i])
        y2 = float(y_values[i])
        break
y_find = y1 + ((y2 - y1) / (x2 - x1)) * (xt - x1)   # calculation of Xt
print('Yi founded: ' + str(y_find))
exit()