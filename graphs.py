import matplotlib.pyplot as plt
import numpy as np
from IPython.display import FileLink

# Nastavitve grafov
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 12

# Podatki
x = np.linspace(0, 10, 500)  # Prilagodite območje in korak x, kot želite
f1 = np.cos(x)
f2 = f1 ** 2
g1 = np.cos(x) * np.exp(-0.1 * x)
g2 = g1 ** 2

# Narišemo grafe f_1(x) in f_2(x) ter g_1(x) in g_2(x) na enem grafu
fig, axes = plt.subplots(1, 2, figsize=(15, 6.5))

# Prvi panel
axes[0].plot(x, f1, label='$f_1(x) = \\cos(x)$')
axes[0].plot(x, f2, label='$f_2(x) = (f_1(x))^2$')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('Grafa $f_1(x)$ in $f_2(x)$')
axes[0].legend()

# Drugi panel
axes[1].plot(x, g1, label='$g_1(x) = \\cos(x) \\cdot e^{-0.1x}$')
axes[1].plot(x, g2, label='$g_2(x) = (g_1(x))^2$')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_title('Grafa $g_1(x)$ in $g_2(x)$')
axes[1].legend()

# Izvoz slike v jpg format
plt.savefig('zdruzena_grafa.jpg', dpi=300, bbox_inches='tight')

# Prikažemo graf
plt.show()

# Generate a download link for the combined image
FileLink('zdruzena_grafa.jpg')

