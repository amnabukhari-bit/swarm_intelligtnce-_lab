import numpy as np
import matplotlib.pyplot as plt
import random

def sphere(x, y):
    """Sphere benchmark function."""
    return x**2 + y**2

def rastrigin(x, y):
    """Rastrigin benchmark function."""
    A = 10
    return 2 * A + (x**2 - A * np.cos(2 * np.pi * x)) + (y**2 - A * np.cos(2 * np.pi * y))

def ackley(x, y):
    """Ackley benchmark function."""
    term1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))
    term2 = -np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))
    return term1 + term2 + np.e + 20

def random_search(func, bounds, iterations=1000):
    """Performs a simple random search to find the minimum of a function within bounds."""
    best_score = float('inf')
    best_point = None
    for i in range(iterations):
        x = random.uniform(bounds[0], bounds[1])
        y = random.uniform(bounds[0], bounds[1])
        score = func(x, y)
        if score < best_score:
            best_score = score
            best_point = (x, y)
    return best_point, best_score

# Execution logic runs only when this file is run directly
if __name__ == "__main__":
    print("Running random search evaluations...\n")
    
    # 1. Sphere Numeric Results
    best_point, best_score = random_search(sphere, (-5, 5))
    print(f'Sphere -> Best point: {best_point} | Best score: {best_score}')

    # 2. Rastrigin Numeric Results
    best_point, best_score = random_search(rastrigin, (-5.12, 5.12))
    print(f'Rastrigin -> Best point: {best_point} | Best score: {best_score}')

    # 3. Ackley Numeric Results
    best_point, best_score = random_search(ackley, (-32.768, 32.768))
    print(f'Ackley -> Best point: {best_point} | Best score: {best_score}')
    print("-" * 60)

    # Plotting Logic
    print("Generating landscape plots...")
    
    # Sphere Plot
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    Z = sphere(X, Y)
    plt.figure(figsize=(6, 5))
    plt.contourf(X, Y, Z, levels=30, cmap='viridis')
    plt.colorbar(label='f(x, y)')
    plt.title('Sphere Function Landscape')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    # Rastrigin Plot
    x = np.linspace(-5.12, 5.12, 200)
    y = np.linspace(-5.12, 5.12, 200)
    X, Y = np.meshgrid(x, y)
    Z = rastrigin(X, Y)
    plt.figure(figsize=(6, 5))
    plt.contourf(X, Y, Z, levels=30, cmap='viridis')
    plt.colorbar(label='f(x, y)')
    plt.title('Rastrigin Function Landscape')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    # Ackley Plot
    x = np.linspace(-32.768, 32.768, 200)
    y = np.linspace(-32.768, 32.768, 200)
    X, Y = np.meshgrid(x, y)
    Z = ackley(X, Y)
    plt.figure(figsize=(6, 5))
    plt.contourf(X, Y, Z, levels=30, cmap='viridis')
    plt.colorbar(label='f(x, y)')
    plt.title('Ackley Function Landscape')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()