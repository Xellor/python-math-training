# Interpolation (linear method)
# Python3
# Last update 13.02.2016
print('Interpolation (linear)\n\n')
x_values = input('Enter Xi values (1,2,3,..,n): ')   # input Xi values
x_values = x_values.split(',')
x_values_len = len(x_values)
print(str(x_values_len) + ' positions')
y_values = input('Enter Yi values (1,2,3,..,n): ')   # inpur Yi values
y_values = y_values.split(',')
y_values_len = len(y_values)
print(str(y_values_len) + ' positions')
if x_values_len != y_values_len:  # lenght check <len(Xi == Yi)>
    print('Error, different length of Xi and Yi')
    print('Xi = ' + str(x_values_len) + '\nYi = ' + str(y_values_len))
    input('(pause)')
    exit()
try:
    xt = float(input('Enter Xi to find: ')) # input xt (x to find)
except ValueError:
    print('Error, wrong input value!')
    input('(pause)')
    exit()
x1 = float(xt)
x2 = float(xt)
for i in range(x_values_len):     # search x1, y1
    try:
        if float(x_values[i]) < x1:
            continue
        else:
            x1 = float(x_values[i - 1])
            y1 = float(y_values[i - 1])
            break
    except ValueError:
        print('Error, wrong input value!')
        input('(pause)')
        exit()
for i in range(x_values_len):     # search x2, y2
    if float(x_values[i]) < x2:
        continue
    else:
        try:
            x2 = float(x_values[i])
            y2 = float(y_values[i])
        except ValueError:
            print('Error, wrong input value!')
            input('(pause)')
            exit()
        break
try:
    y_find = y1 + ((y2 - y1) / (x2 - x1)) * (xt - x1)
except NameError:
    print('Wrong value in Xi (to find)!')
    input('(pause)')
    exit()
except ZeroDivisionError:
    print('Wrong syntasys')
    input('(pause)')
    exit()
print('Yi founded: ' + str(y_find)) # output result
input('(pause)')
exit()