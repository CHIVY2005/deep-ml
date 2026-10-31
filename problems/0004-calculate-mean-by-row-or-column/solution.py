import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    arr = np.array(matrix)
    
    # Lấy đúng số hàng và số cột
    so_hang = len(matrix)
    so_cot = len(matrix[0]) if so_hang > 0 else 0
    
    if mode == 'column':
        # Tính toán bằng numpy trước, sau đó ép kiểu sang list rồi GÁN thẳng (không dùng append)
        means = (np.sum(arr, axis=0) / so_hang).tolist()
    elif mode == 'row':
        # Tương tự cho hàng
        means = (np.sum(arr, axis=1) / so_cot).tolist()
    else:
        means = []
        
    return means
