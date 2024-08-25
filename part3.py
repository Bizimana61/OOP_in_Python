

# File: part3.py

import time
from part2 import k_means, get_states
from part1 import read_restaurants

def main():
    filename = 'restaurants.json'
    restaurants = read_restaurants(filename)
    
    start_time = time.time()
    clusters = k_means(restaurants, k=3)
    end_time = time.time()
    
    print(f"Clustering took {end_time - start_time:.2f} seconds.")
    
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i+1}: {len(cluster)} restaurants")
        print("States in this cluster:", get_states(cluster))
        print("")

if __name__ == "__main__":
    main()
