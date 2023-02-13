#Grids 1-4 are 2x2
grid1 = [
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 1, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[0, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 2, 3, 4],
		[2, 1, 4, 3],
		[3, 4, 2, 1],
		[4, 3, 1, 2]]

grid4 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

#Grids 4-7 are 3x3
grid5 = [
		[1, 2, 3, 4, 5, 6, 7, 8, 9,],
		[2, 3, 4, 5, 6, 7, 8, 9, 1,],
		[3, 4, 5, 6, 7, 8, 9, 1, 2,],
		[4, 5, 6, 7, 8, 9, 1, 2, 3,],
		[5, 6, 7, 8, 9, 1, 2, 3, 4,],
		[6, 7, 8, 9, 1, 2, 3, 4, 5,],
		[7, 8, 9, 1, 2, 3, 4, 5, 6,],
		[8, 9, 1, 2, 3, 4, 5, 6, 7,],
		[9, 1, 2, 3, 4, 5, 6, 7, 8,]]

grid6 = [
		[6, 1, 7, 8, 4, 2, 5, 3, 9,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

grid7 = [
		[6, 1, 9, 8, 4, 2, 5, 3, 7,],
		[7, 4, 5, 3, 6, 9, 1, 8, 2,],
		[8, 3, 2, 1, 7, 5, 4, 6, 9,],
		[1, 5, 8, 6, 9, 7, 3, 2, 4,],
		[9, 6, 4, 2, 3, 1, 8, 7, 5,],
		[2, 7, 3, 5, 8, 4, 6, 9, 1,],
		[4, 8, 7, 9, 5, 6, 2, 1, 3,],
		[3, 9, 1, 4, 2, 8, 7, 5, 6,],
		[5, 2, 6, 7, 1, 3, 9, 4, 8,]]

#grids 8-10 are 2x3
grid8 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid9 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 5, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]

grid10 = [
		[1, 2, 6, 5, 4, 3],
		[5, 3, 4, 6, 2, 1],
		[6, 1, 3, 4, 5, 2],
		[2, 4, 5, 3, 1, 6],
		[4, 6, 1, 2, 3, 5],
		[3, 5, 2, 1, 6, 4]]


grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), 
		(grid5, 3, 3), (grid6, 3, 3), (grid7, 3, 3),
		(grid8, 2, 3), (grid9, 2, 3), (grid10, 2, 3)]

expected_outputs = [False, False, False, True, False, False, True, False, False, True]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

#To complete the first assignment, please write the code for the following function
def check_solution(grid_in):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	grid_input =grid_in[0]
	number_of_rows = 0
	i = len(grid_input[0])
	if i == 4:
		number_of_rows += 4
	elif i == 6:
		number_of_rows += 6
	else:
		number_of_rows += 9
	row = 0
	result = True
	while row < number_of_rows:
		for position in range(len(grid_input[row])):
			if grid_input[row].count(grid_input[row][position]) > 1:
				result = False
		row += 1
	list_subgrid = []
	# Checking the sub grids
	if number_of_rows == 4:
		for k in range(0, 4, 2):
			for j in range(0, 4, 2):
				sub_grid = [grid_input[k][j], grid_input[k][j + 1], grid_input[k + 1][j], grid_input[k + 1][j + 1]]
				list_subgrid.append(sub_grid)
				sub_grid_number = 0
				for sub_position in range(len(list_subgrid)):
					if list_subgrid[sub_grid_number].count(list_subgrid[sub_grid_number][sub_position]) > 1:
						result = False
					else:
						sub_grid_number += 1
	elif number_of_rows == 6:
		for k in range(0, 6, 2):
			for j in range(0, 6, 3):
				sub_grid = [grid_input[k][j], grid_input[k][j + 1], grid_input[k][j + 2], grid_input[k + 1][j],
							grid_input[k + 1][j + 1], grid_input[k + 1][j + 2]]
				list_subgrid.append(sub_grid)
				sub_grid_number = 0
				for sub_position in range(len(list_subgrid)):
					if list_subgrid[sub_grid_number].count(list_subgrid[sub_grid_number][sub_position]) > 1:
						result = False
					else:
						sub_grid_number += 1
	else:
		for k in range(0, 9, 3):
			for j in range(0, 9, 3):
				sub_grid = [grid_input[k][j], grid_input[k][j + 1], grid_input[k][j + 2], grid_input[k + 1][j],
							grid_input[k + 1][j + 1], grid_input[k + 1][j + 2], grid_input[k + 2][j],
							grid_input[k + 2][j + 1], grid_input[k + 2][j + 2]]
				list_subgrid.append(sub_grid)
				sub_grid_number = 0
				for sub_position in range(len(list_subgrid)):
					if list_subgrid[sub_grid_number].count(list_subgrid[sub_grid_number][sub_position]) > 1:
						result = False
					else:
						sub_grid_number += 1
	# checking the columns
	list_column = []
	for p in range(number_of_rows):
		list_column.append(grid_input[p][0])
		for m in range(len(list_column)):
			if list_column.count(list_column[m]) > 1:
				result = False
	print(result)
	return result





'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():
	'''
	This function will call the check_solution function on each of the provided grids,
	comparing the answer to the expected output. Each correct output is given 10 'points
	'''

	points = 0

	print("Running test script for coursework 1")
	print("====================================")

	#Loop through the grids and expected outputs together
	for (i, (grid, output)) in enumerate(zip(grids, expected_outputs)):

		#Compare output to expected output
		print("Checking grid: %d" % (i+1))
		checker_output = check_solution(grid)

		if checker_output == expected_outputs[i]:
			#Output is correct - yay!
			print("grid %d correct" % (i+1))
			points = points + 5
		else:
			#Output is incorrect - print both output and expected output.
			print("grid %d incorrect" % (i+1))
			print("Output was: %s, but expected: %s" % (checker_output, expected_outputs[i]))

	print("====================================")
	print("Test script complete, Total points: %d" % points)

if __name__ == "__main__":
	main()