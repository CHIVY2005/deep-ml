import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	arr = np.array(a,dtype=float)
	if arr.size != new_shape[0] * new_shape[1]:
		return []
	reshape = np.reshape(arr,new_shape)
	return reshape.tolist()