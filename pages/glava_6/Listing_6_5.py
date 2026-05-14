# Листинг 6.5
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.datasets import load_iris

# Загрузить набор данных
iris_dataset = load_iris()

# Построить матрицу рассеяния с библиотекой seaborn
df = sb.load_dataset('iris')
sb.set_style("ticks")
sb.pairplot(df, hue='species', diag_kind="kde", kind="scatter", palette="husl")
plt.show()