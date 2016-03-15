# Matrix (summation and difference)
# Python3
# Last update 15.02.2016
print('Matrix: summation and difference\n\n')
try:
	matrix_n = int(input('Enter matrix size (N x N): '))	# Set size matrix
except ValueError:
	print('Wrong value, only integer!')
	input('(pause)')
	exit()
if matrix_n < 1:	# Check
	print('Error, matrix size < 0')
	input('(pause)')
	exit()
matrix_1 = []	# Initialize matrix variables
matrix_2 = []
matrix_3 = []	# matrix_3 is result matrix
for i in range(matrix_n):	# Append in matrix variables N lists
	matrix_1.append([])
	matrix_2.append([])
	matrix_3.append([])
for i in range(matrix_n):
	for j in range(matrix_n):	# Input N values in matrix_1 lists
		print('Enter M1(' + str(i + 1) + '.' + str(j + 1) + ')')
		try:
			matrix_1[i].append(int(input()))
		except ValueError:
			print('Only integer values!')
			input('(pause)')
			exit()
print('Now M2')
for i in range(matrix_n):
	for j in range(matrix_n):	# Input N values in matrix_2 lists
		print('Enter M2(' + str(i + 1) + '.' + str(j + 1) + ')')
		try:
			matrix_2[i].append(int(input()))
		except ValueError:
			print('Only integer values!')
			input('(pause)')
			exit()
print('\n\n\nYou matrix:\n')
for i in range(matrix_n):
	print(matrix_1[i])
print('\n')
for i in range(matrix_n):
	print(matrix_2[i])
print('\n')
print('What you want to do with them?')
print('1 - plus\n2 - minus')
matrix_action = int(input('Enter action No: '))
if matrix_action != 1 and matrix_action != 2:	# Check
	print('Wrong action No!')
	input('(pause)')
	exit()
if matrix_action == 1:
	for i in range(matrix_n):
		for j in range(matrix_n):
			matrix_3[i].append(matrix_1[i][j] + matrix_2[i][j])
elif matrix_action == 2:
	for i in range(matrix_n):
		for j in range(matrix_n):
			matrix_3[i].append(matrix_1[i][j] - matrix_2[i][j])
print('\n\nM1:')
for i in range(matrix_n):
	print(matrix_1[i])
print('\nM2:')
for i in range(matrix_n):
	print(matrix_2[i])
print('\nM3 (result):')
for i in range(matrix_n):
	print(matrix_3[i])
input('\n\n(pause)')
exit()