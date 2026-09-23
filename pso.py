import random

# Seed set to roll number digits (99) to keep outputs reproducible across runs
random.seed(7)

# Objective cost function with known global optimum located at x = 7
def f(x):
    return (x - 7)**2 + 4

# Initialize particle locations uniformly across the entire search space
positions = [random.uniform(0, 14) for _ in range(6)]

# Set initial particle velocities to zero so motion starts from rest
velocities = [0 for _ in range(6)]

# Shallow copy positions to track each particle's private historic best independently
pbest_pos = positions[:]

# Identify the swarm-wide best initial candidate based on function evaluation
gbest_pos = min(pbest_pos, key=f)

# PSO hyperparameters: inertia weight (w), cognitive pull (c1), and social pull (c2)
w, c1, c2 = 0.6, 1.5, 1.5
iterations = 50

for it in range(iterations):
    for i in range(6):
        # Stochastic scaling factors drawn uniformly from [0, 1)
        r1, r2 = random.random(), random.random()

        # Update step balancing momentum, cognitive attraction, and swarm influence
        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (pbest_pos[i] - positions[i])
            + c2 * r2 * (gbest_pos - positions[i])
        )

        # Step particle forward using newly computed velocity vector
        positions[i] = positions[i] + velocities[i]

        # Greedy update: retain new coordinate only if fitness improves
        if f(positions[i]) < f(pbest_pos[i]):
            pbest_pos[i] = positions[i]

    # Re-evaluate and record the overall leader position for the current generation
    gbest_pos = min(pbest_pos, key=f)

print("Swarm converged near x =", gbest_pos)