#We import our libs:
import numpy as np
import matplotlib.pyplot as plt
from numba import jit


@jit
def solver(N):
    # Make the initial guess for solution matrix
    V = np.zeros((N,N))

    # Solver:
    iterations = 0
    eps = 1e-10 # Convergence threshold
    error = 1e4 # Large dummy error
    while iterations < 1e4 and error > eps:
        V_temp = np.copy(V)
        error = 0
        # we make this accumulate in the loop
        for j in range(1,N-1):
            for i in range(1,N-1):
                V[i,j] = 0.25*(V[i+1,j] + V[i-1,j] + V[i,j-1] + V[i,j+1] + rho[i,j]*ds**2)
                error += abs(V[i,j]-V_temp[i,j])
            iterations += 1
    print("iterations =", iterations)
    return V


# Set dimensions of the problem:
L = 1.0
N = 21
ds = L/N

# Define arrays used for plotting:
x = np.linspace(0,L,N)
y = np.copy(x)
X, Y = np.meshgrid(x,y)

# Make the charge density matrix:
rho0 = 1.0
rho = np.zeros((N,N))
rho[int(round(N/2.0)),int(round(N/2.0))] = rho0
# for j in range(round(N/2.0)-int(N/20.0),round(N/2.0)+int(N/20.0)):
#     rho[round(N/2.0)-int(N/30.0),j] = rho0
#     rho[round(N/2.0)+int(N/30.0),j] = -rho0

# Solver:
V = solver(N)

# Plotting:
eps = 3
zoomX = X[round(N/2.0)-eps:round(N/2.0)+eps]
zoomY = Y[round(N/2.0)-eps:round(N/2.0)+eps]
zoomV = V[round(N/2.0)-eps:round(N/2.0)+eps]
plt.figure(figsize=(5,3))
CS = plt.contour(zoomX, zoomY, zoomV, 30) # Make a contour plot
plt.clabel(CS, inline=1, fontsize=10)
plt.title("PDE solution of a point charge")
CB = plt.colorbar(CS, extend="both")
plt.show()

# Print matrix:
print(zoomV)
