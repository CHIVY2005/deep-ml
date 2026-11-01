import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	new_arr = []
	for row in matrix:
		row = [val*scalar for val in row]
		new_arr.append(row)
	return new_arr

	pass