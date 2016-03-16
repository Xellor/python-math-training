# Matrix (summation and difference)
# Python3
# by Xellor
# Last update 16.03.2016
matrix_n = int(input('Enter matrix size (N x N): '))	# Set size matrix, integer only
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
		matrix_1[i].append(int(input()))
print('Now M2')
for i in range(matrix_n):
	for j in range(matrix_n):	# Input N values in matrix_2 lists
		print('Enter M2(' + str(i + 1) + '.' + str(j + 1) + ')')
		matrix_2[i].append(int(input()))
print('\n')
print('1 - plus; 2 - minus;')
matrix_action = int(input('Enter action No: '))
if matrix_action == 1:
	for i in range(matrix_n):
		for j in range(matrix_n):
			matrix_3[i].append(matrix_1[i][j] + matrix_2[i][j])
elif matrix_action == 2:
	for i in range(matrix_n):
		for j in range(matrix_n):
			matrix_3[i].append(matrix_1[i][j] - matrix_2[i][j])
print('\nM3 (result):')
for i in range(matrix_n):
	print(matrix_3[i])
exit()