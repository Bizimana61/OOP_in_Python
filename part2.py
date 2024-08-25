

# part2.py

import random
from utils import distance, mean
from part1 import read_restaurants

def get_states(restaurants):
    return sorted(list(set(restaurant.state for restaurant in restaurants)))

def find_closest(location, centroids):
    closest_centroid = min(centroids, key=lambda centroid: distance(location, centroid))
    return closest_centroid

def group_by_centroid(restaurants, centroids):
    clusters = {centroid: [] for centroid in centroids}
    for restaurant in restaurants:
        loc = (restaurant.latitude, restaurant.longitude)
        closest_centroid = find_closest(loc, centroids)
        clusters[closest_centroid].append(restaurant)
    return list(clusters.values())

def find_centroid(cluster):
    latitudes = [restaurant.latitude for restaurant in cluster]
    longitudes = [restaurant.longitude for restaurant in cluster]
    centroid = (mean(latitudes), mean(longitudes))
    return centroid

def k_means(restaurants, k, max_iterations=1000):
    centroids = random.sample([(restaurant.latitude, restaurant.longitude) for restaurant in restaurants], k)
    for _ in range(max_iterations):
        clusters = group_by_centroid(restaurants, centroids)
        new_centroids = [find_centroid(cluster) for cluster in clusters]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters

def run_tests():
    # Example JSON structure
    
    restaurants=read_restaurants("restaurants.json")
    # Test get_states
    states = get_states(restaurants)
    assert 'PA' in states
    assert 'NJ' in states
    assert 'DE' in states

    # Test find_closest
    closest = find_closest((39.95378, -75.155), [(39.9509, -75.144), (39.95378, -75.155)])
    assert closest == (39.95378, -75.155)

    # Test group_by_centroid
    centroids = [(39.95378, -75.155), (39.9509, -75.144)]
    clusters = group_by_centroid(restaurants, centroids)
    assert len(clusters) == 2

    # Test find_centroid
    centroid = find_centroid(clusters[0])
    assert centroid == (36.59654018761831, -90.33000869693451)

    # Test k_means
    clusters = k_means(restaurants, 2)
    assert len(clusters) == 2

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
