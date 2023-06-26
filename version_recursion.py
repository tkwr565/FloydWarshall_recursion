# Number of vertices in the graph
V = 4

# Define infinity as a large enough value
INF = 99999


# Recursive function to calculate the shortest paths using Floyd-Warshall algorithm
def floydWarshallRecursive(graph, dist, k, i, j):
    # Base case: If k has reached V, return the final distance matrix
    if k == V:
        return dist

    # Update the distance matrix
    if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]

    # Recurse by incrementing k and traversing all vertices for i and j
    if j < V - 1:
        dist = floydWarshallRecursive(graph, dist, k, i, j + 1)
    elif i < V - 1:
        dist = floydWarshallRecursive(graph, dist, k, i + 1, 0)
    else:
        dist = floydWarshallRecursive(graph, dist, k + 1, 0, 0)

    return dist


# Function to print the solution matrix
def printSolution(dist):
    print(
        "Following matrix shows the shortest distances between every pair of vertices"
    )
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=" ")
            if j == V - 1:
                print()


# Function to initialize the graph and call the recursive function
def floydWarshall(graph):
    # Create a copy of the graph to use as the distance matrix
    dist = [row[:] for row in graph]

    # Call the recursive function to calculate the shortest paths
    dist = floydWarshallRecursive(graph, dist, 0, 0, 0)

    # Print the solution
    printSolution(dist)


# Driver's code
if __name__ == "__main__":
    # Sample graph
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]

    # Call the function
    floydWarshall(graph)
