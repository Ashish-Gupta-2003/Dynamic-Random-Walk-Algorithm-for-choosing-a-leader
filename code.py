import random
import os

# Constants
NUM_NODES = 54
NUM_EDGES = 29
ITERATIONS = 100000000
SEED = 15042022

# Initialize variables
a = [[0] * NUM_EDGES for _ in range(NUM_NODES)]
coin = [0] * NUM_NODES
count = 0

# Read data from files
for i in range(NUM_NODES):
    file_name = f"data/{i + 1}.txt"
    try:
        with open(file_name, 'r') as in_file:
            for j in range(NUM_EDGES):
                line = in_file.readline().strip()
                if line:
                    a[i][j] = int(line)
                else:
                    raise ValueError(f"File {file_name} has insufficient data")
    except FileNotFoundError:
        print(f"File {file_name} not found")
        continue
    except ValueError as e:
        print(e)
        continue

# Set random seed for reproducibility
random.seed(SEED)

# Perform random walk
row = 0
while count < ITERATIONS:
    next_node = a[row][random.randint(0, NUM_EDGES - 1)]
    if next_node != 0:
        coin[next_node - 1] += 1
        row = next_node - 1
        count += 1

# Sort results
sorted_coin = sorted((value * 1000 + index + 1 for index, value in enumerate(coin)), reverse=True)

# Print results
for index, value in enumerate(sorted_coin):
    print(f"\n {index + 1} : {value // 1000}")

# Print the leader
leader_index = sorted_coin[0] % 1000 - 1
print(f"\nLeader is node {leader_index + 1} with {coin[leader_index]} votes")
