# Interpolation (lagranje method)
# Python3
# Last update 15.02.2016
print('Interpolation (lagranje)\n\n')
x_values = input('Enter Xi values (1,2,3,..,n): ')   # input Xi values
x_values = x_values.split(',')
x_values_len = len(x_values)
print(str(x_values_len) + ' positions')
y_values = input('Enter Yi values (1,2,3,..,n): ')   # inpur Yi values
y_values = y_values.split(',')
y_values_len = len(y_values)
print(str(y_values_len) + ' positions\n\n')
if x_values_len != y_values_len:  # lenght check <len(Xi == Yi)>
    print('Error, different length of Xi and Yi')
    print('Xi = ' + str(x_values_len) + '\nYi = ' + str(y_values_len))
    input('(pause)')
    exit()
try:
    xt = float(input('Enter Xi to find: ')) # input xt (x to find)
    print('\n\n')
except ValueError:
    print('Error, wrong input value!')
    input('(pause)')
    exit()
# Polenom Lagranja
polinom_up = ''
polinom_down = ''
p_up = float(1)
p_down = float(1)
p = float(0)
for i in range(x_values_len):
	p_up = 1
	p_down = 1
	for j in range(x_values_len):
		x_index = j
		if x_index == i:
			continue
		p_up = p_up * (xt - float(x_values[x_index]))
		p_down = p_down * (float(x_values[i]) - float(x_values[x_index]))
		polinom_up = polinom_up + '(' + str(xt) + ' - ' + str(float(x_values[x_index])) + ')'
		polinom_down = polinom_down + '(' + str(x_values[i]) + '-' + str(x_values[x_index]) + ')'
	p = p + float(y_values[i]) * (p_up / p_down)
	print('   ' + str(polinom_up))
	print(str(y_values[i]) + ' * -----------')
	print('   ' + str(polinom_down))
	print('\n')
	polinom_up = ''
	polinom_down = ''
print(p)
input()