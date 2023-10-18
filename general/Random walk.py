import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
all_walks = []

def steps(n):
    random_walk = [0]
    for _ in range(n):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        # Implement clumsiness
        if np.random.rand() <= 0.001:  # There is a 0.1% chance of falling down the stairs
            step = 0
        random_walk.append(step)
    return random_walk


for i in range(250):
    all_walks.append(steps(100))
print(all_walks)
# Create and plot np_aw_trandom_walk = [0]
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, ]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
