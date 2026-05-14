# Листинг 6.1
import numpy as np
from scipy import sparse

# Создаем 2D-массив NumPy с единицами по
# главной диагонали и нулями в остальных ячейках
eye = np.eye(4)
print("Массив NumPy")
print(eye)

# Преобразовываем массив NumPy в разреженную
# матрицу SciPy в формате CSR
sparse_matrix = sparse.csr_matrix(eye)
print("Разреженная матрица SciPy в формате CSR:")
print(sparse_matrix)

# Преобразовываем массив NumPy в разреженную
# матрицу SciPy в формате COO
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("Разреженная матрица SciPy в формате COO:")
print(eye_coo)