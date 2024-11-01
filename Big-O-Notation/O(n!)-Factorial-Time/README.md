# O(n!) - Factorial Time Complexity

**O(n!) time complexity**, or **factorial time complexity**, describes algorithms where the number of operations grows factorially with each increase in input size. Factorial growth is incredibly fast, making these algorithms impractical for even moderately large inputs.

## Key Points of O(n!)

- **Extremely Fast Growth**: Factorial time complexity grows faster than exponential time, resulting in massive time requirements as `n` increases.
- **Common in Permutation Problems**: O(n!) often arises in problems involving permutations or combinations, where all possible arrangements are explored.
- **Unfeasible for Large Inputs**: Due to its rapid growth, factorial time complexity is typically limited to small inputs, as even a slight increase can make the algorithm infeasible.

## Examples of O(n!) Algorithms

### 1. Permutations of a List

Generating all possible permutations of a list requires exploring every possible arrangement, leading to factorial time complexity.

```python
from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))
```

- For a list of `n` elements, there are `n!` possible permutations, resulting in O(n!) complexity.

### 2. Traveling Salesman Problem (TSP) - Brute Force Solution

In the Traveling Salesman Problem, a salesperson must visit each city once and return to the starting city. The brute-force solution examines every possible route, resulting in O(n!) complexity.

```python
import itertools

def tsp_brute_force(cities, distance_matrix):
    min_distance = float('inf')
    best_route = None
    for route in itertools.permutations(cities):
        distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        if distance < min_distance:
            min_distance = distance
            best_route = route
    return best_route, min_distance
```

- This brute-force approach calculates the distance for each permutation of cities, resulting in O(n!) complexity.

---

## Visualizing O(n!)

In an O(n!) algorithm, the runtime grows at a factorial rate, as shown in the graph below:

```
Time
│
│                 /
│               /
│            /
│        /
│   /
│/
└───────────────────
        Input Size (n)
```

## Why O(n!) is So Expensive

- **Infeasible Growth**: Even for small values of `n`, factorial growth leads to an unmanageable number of operations.
- **Avoid if Possible**: O(n!) complexity indicates the need for optimization. If possible, look for heuristic or approximate algorithms instead.

### Summary

O(n!), or factorial time complexity, describes algorithms that grow factorially with the input size. This growth rate quickly becomes impractical, and O(n!) algorithms are generally used only for very small inputs or when optimized solutions are unavailable.
