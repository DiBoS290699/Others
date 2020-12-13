import matplotlib.pyplot as plt


count_elements = [32, 64, 128]

CUDA = [0.000337, 0.000341, 0.000267]
single_thread = [0.000173, 0.001222, 0.010611]


acceleration = [single_thread[0] / CUDA[0], single_thread[1] / CUDA[1], single_thread[2] / CUDA[2]]


plt.plot(count_elements, acceleration, label="acceleration", color='orange')
plt.grid()
plt.legend()
plt.xlabel("Размерность матрицы NxN", size=15)
plt.ylabel('Отношение времени посл. алгорита к времени CUBLAS', size=15)
plt.show()
