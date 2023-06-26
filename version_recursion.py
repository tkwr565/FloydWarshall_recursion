# Recursion version python code for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as a large enough value
INF = 99999


# Recursive function to calculate the shortest paths using Floyd-Warshall algorithm
def floydWarshallRecursive(
    graph: list[list[int]], dist: list[list[int]], k: int, i: int, j: int
) -> list[list[int]]:
    """
    Recursively calculates the shortest paths between all pairs of vertices using the Floyd-Warshall algorithm.

    Args:
        graph (list[list[int]]): The input graph represented as an adjacency matrix.
        dist (list[list[int]]): The distance matrix representing the current shortest distances between vertices.
        k (int): The current intermediate vertex being considered.
        i (int): The current source vertex being considered.
        j (int): The current destination vertex being considered.

    Returns:
        list[list[int]]: The updated distance matrix with the shortest distances between all pairs of vertices.
    """

    # Base case: If k has reached V, return the final distance matrix
    if k == V:
        return dist

    # Cacluate the new distance through the intermediate vertex k,
    # Update the distance matrix if new distance is shorter
    if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]

    # Recurse by incrementing k and traversing all vertices for i and j:
    # First recurse through j (columns of matrix)
    if j < V - 1:
        dist = floydWarshallRecursive(graph, dist, k, i, j + 1)
    # Then recurse through i (rows of matrx)
    elif i < V - 1:
        dist = floydWarshallRecursive(graph, dist, k, i + 1, 0)
    # Finally increment k, and recurse over again
    else:
        dist = floydWarshallRecursive(graph, dist, k + 1, 0, 0)

    return dist


# Function to print the solution matrix
def printSolutionRecursive(dist, i=0, j=0):
    """
    Recursively prints the matrix of shortest distances between every pair of vertices.

    Args:
        dist (list[list[int]]): The distance matrix representing the shortest distances.
        i (int): The current row index (default: 0).
        j (int): The current column index (default: 0).
    """

    # Base case: If j has reached the end of the row, move to the next row
    if j == V:
        print()
        printSolutionRecursive(dist, i + 1, 0)
        return

    # Base case: If i has reached the end of the matrix, return
    if i == V:
        return

    # Before printing the result, print the statement line
    if i == 0 and j == 0:
        print(
            "Following matrix shows the shortest distances between every pair of vertices"
        )

    # Print the current distance
    if dist[i][j] == INF:
        print("%7s" % ("INF"), end=" ")
    else:
        print("%7d\t" % (dist[i][j]), end=" ")

    # Recurse to the next column
    printSolutionRecursive(dist, i, j + 1)


# Function to initialize the graph and call the recursive function
def floydWarshall(graph):
    # Create a copy of the graph to use as the distance matrix
    dist = [row[:] for row in graph]

    # Call the recursive function to calculate the shortest paths
    dist = floydWarshallRecursive(graph, dist, 0, 0, 0)

    # Print the solution
    printSolutionRecursive(dist)


# Driver's code
if __name__ == "__main__":
    # Sample graph
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]

    # Call the function
    floydWarshall(graph)
