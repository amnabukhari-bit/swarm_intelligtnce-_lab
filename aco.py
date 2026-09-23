import random
random.seed(7)
paths = {'Path A' : 10, 'Path B' : 15, 'Path C' : 8, 'Path D': 12}
pheromone = {p : 1.0 for p in paths}
evaporation = 0.5
iterations = 100
ants_per_iteration = 10

for iteration in range(iterations):
  for ant in range(ants_per_iteration):
    total = sum(pheromone[p]*(1/paths[p]) for p in paths)
    weight = [pheromone[p]*(1/paths[p])/total for p in paths]
    chosen = random.choices(list(paths.keys()), weights=weight)[0]
    pheromone[chosen] += 1 / paths[chosen]

  for p in pheromone:
    pheromone[p] = pheromone[p] * evaporation

best = max(pheromone , key=pheromone.get)
print("Colony converged on:", best)


