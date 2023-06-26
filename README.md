# FloydWarshall_recursion

This project implements the Floyd Warshall algorithm to find the shortest paths between all pairs of vertices in a given graph. 
It provides the recursive version of the algorithm.

![badge1](https://img.shields.io/github/issues/tkwr565/FloydWarshall_recursion)

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)

## Description

The Floyd Warshall algorithm is a graph algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. It can handle both positive and negative edge weights, but it doesn't work for graphs with negative cycles.

This project provides the recursion implementations of the algorithm:
(The imperative version is also included for comparison through unittest)
- `version_recursion.py`: Recursive implementation of the Floyd Warshall algorithm.

## Installation

1. Clone the repository:
```
git clone git@github.com:tkwr565/FloydWarshall_recursion.git
```

2. (optional) Create and activate a virtual environment
e.g. 
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```

## Usage
The script `version_recursion.py` demonstrates how to use the recursive version of the Floyd Warshall algorithm. You can modify this script or import the function into your own code.
Make sure to modify the `graph` and `V` variables to represent your input graph.

## Tests
The project includes a test file `test_recursion.py` that contains unit tests for the recursive version of the algorithm. 
several version of test were made.
This version test through 3x3, 4x4, and 6x6 matrices by modifing `V` variable in `version_recursion.py` and `version_imperative.py`.
Modify the values in `test_recursion.py` to make your own tests.

