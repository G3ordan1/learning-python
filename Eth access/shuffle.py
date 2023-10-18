import random

words = ["camera", "rhythm", "feature", "layer", "coconut", "ready", "need", "final", "north", "can", "early", "story", "stable", "report", "group", "depend", "employ", "problem", "monitor", "interest", "logic", "sausage", "toilet", "pencil"]

# Shuffle the list 1000 times
shuffled_lists = []
for i in range(100000):
    random.shuffle(words)
    shuffled_lists.append(words[:])

# Write the shuffled lists to a file
with open("shuffled_lists.txt", "w") as f:
    for l in shuffled_lists:
        f.write(" ".join(l) + "\n")

