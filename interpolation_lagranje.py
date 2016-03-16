# Interpolation (Lagranje method)
# Python3
# by Xellor
# Last update 16.03.2016
x_values = input('Enter Xi values (1,2,3,..,n): ')   # input Xi values,
x_values = x_values.split(',')						 # number of values Xi == Yi
x_values_len = len(x_values)
y_values = input('Enter Yi values (1,2,3,..,n): ')   # inpur Yi values
y_values = y_values.split(',')
y_values_len = len(y_values)
xt = float(input('Enter Xi to find: ')) # input xt (x to find)
p_up = float(1)		# numerator of polynom
p_down = float(1)	# denominator of polynom
p = float(0)
for i in range(x_values_len):
	p_up = 1	# reset data
	p_down = 1
	for j in range(x_values_len):
		x_index = j
		if x_index == i:
			continue
		p_up = p_up * (xt - float(x_values[x_index]))
		p_down = p_down * (float(x_values[i]) - float(x_values[x_index]))
	p = p + float(y_values[i]) * (p_up / p_down)
	print('\n')
print(p)