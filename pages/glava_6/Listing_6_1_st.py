# Листинг 6.1
import streamlit as st
import numpy as np
from scipy import sparse

# Создаем 2D-массив NumPy с единицами по
# главной диагонали и нулями в остальных ячейках
eye = np.eye(4)
st.write("Массив NumPy")
with st.container(width=250):
    st.write(eye)

# Преобразовываем массив NumPy в разреженную
# матрицу SciPy в формате CSR
sparse_matrix = sparse.csr_matrix(eye)
st.write("Разреженная матрица SciPy в формате CSR:")
st.write(sparse_matrix)

# Преобразовываем массив NumPy в разреженную
# матрицу SciPy в формате COO
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))

st.write("Разреженная матрица SciPy в формате COO:")
st.write(eye_coo)