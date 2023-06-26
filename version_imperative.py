# Imperative version python code for Floyd Warshall Algorithm
# based on https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# code modify to be used in unittest


INF = 99999


def floydWarshallImperative(graph, V):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def printSolution(dist, V):
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


def floydWarshall(graph, V):
    dist = floydWarshallImperative(graph, V)
    printSolution(dist, V)


if __name__ == "__main__":
    V0 = 4
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    floydWarshall(graph, V=V0)
# This code is contributed by Mythri J L
