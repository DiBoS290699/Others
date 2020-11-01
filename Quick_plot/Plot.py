import matplotlib.pyplot as plt


count_process = [1, 16, 24]

omp_static = [5.327, 4.847, 4.973]
omp_dynamic = [5.677, 6.249, 6.741]
omp_guided = [5.421, 4.161, 4.651]

mpi_multiply = [25.673, 9.703, 11.311]
mpi_not_multiply = [26.346, 9.245, 11.911]

omp_static_acceleration = [1, omp_static[0]/omp_static[1], omp_static[0]/omp_static[2]]
omp_dynamic_acceleration = [1, omp_dynamic[0]/omp_dynamic[1], omp_dynamic[0]/omp_dynamic[2]]
omp_guided_acceleration = [1, omp_guided[0]/omp_guided[1], omp_guided[0]/omp_guided[2]]

mpi_multiply_acceleration = [1, mpi_multiply[0]/mpi_multiply[1], mpi_multiply[0]/mpi_multiply[2]]
mpi_not_multiply_acceleration = [1, mpi_not_multiply[0]/mpi_not_multiply[1], mpi_not_multiply[0]/mpi_not_multiply[2]]

plt.plot(count_process, mpi_multiply_acceleration, label="mpi_multiply_acceleration", color='orange')
plt.plot(count_process, mpi_not_multiply_acceleration, label="mpi_not_multiply_acceleration", color='green')
plt.grid()
plt.legend()
plt.xlabel("Количество процессов", size=15)
plt.ylabel('Коэффициент изменения скорости', size=15)
plt.show()
