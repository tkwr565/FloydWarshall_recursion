# FloydWarshall_recursion

This project implements the Floyd Warshall algorithm to find the shortest paths between all pairs of vertices in a given graph. 
It provides the recursive version of the algorithm.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

## Description

The Floyd Warshall algorithm is a graph algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. It can handle both positive and negative edge weights, but it doesn't work for graphs with negative cycles.

This project provides two implementations of the algorithm:

- `floydWarshallIterative(graph)`: Iterative implementation of the Floyd Warshall algorithm.
- `floydWarshallRecursive(graph)`: Recursive implementation of the Floyd Warshall algorithm.