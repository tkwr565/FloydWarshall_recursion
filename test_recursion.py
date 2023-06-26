# This is the unittest module to compare the recursion version against the imperative version
# unittest was done for the algorithm calculation function, and the print function
# test was done for 3x3, 4x4 and 6x6 matrices

import unittest
import version_imperative
import version_recursion

INF = 99999


class FloydWarshallTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case with sample data
        """
        self.graph = [[0, 5, INF], [INF, 0, 3], [INF, INF, 0]]
        self.graph0 = [
            [0, INF, 9, 3],
            [3, 0, 6, 2],
            [INF, 2, 0, INF],
            [INF, 5, INF, 0],
        ]
        self.graph1 = [
            [0, 2, 7, 9, 1, INF],
            [INF, 0, INF, 1, 9, 2],
            [2, 1, 0, INF, INF, 8],
            [1, 2, INF, 0, 9, 1],
            [1, 2, INF, INF, 0, 7],
            [INF, 2, 3, 1, 2, 0],
        ]

    def test_floydWarshall(self):
        """
        capture and compare the output of floydwarshall algorithm calculation function of recursion
        and imperative version
        """

        # first test with 4x4 sample
        version_imperative.V = 4
        version_recursion.V = 4
        expected_output = version_imperative.floydWarshallImperative(self.graph0)
        dist = [row[:] for row in self.graph0]
        result = version_recursion.floydWarshallRecursive(self.graph0, dist, 0, 0, 0)
        self.assertEqual(result, expected_output)

        # then test with 3x3 sample
        version_imperative.V = 3
        version_recursion.V = 3
        expected_output = version_imperative.floydWarshallImperative(self.graph)
        dist = [row[:] for row in self.graph]
        result = version_recursion.floydWarshallRecursive(self.graph, dist, 0, 0, 0)
        self.assertEqual(result, expected_output)

        # then test with 6x6 sample
        version_imperative.V = 6
        version_recursion.V = 6
        expected_output = version_imperative.floydWarshallImperative(self.graph1)
        dist = [row[:] for row in self.graph1]
        result = version_recursion.floydWarshallRecursive(self.graph1, dist, 0, 0, 0)
        self.assertEqual(result, expected_output)

    def test_printSolution(self):
        """
        capture and compare the output of print functions of recursion and imperative version
        by printing example graph
        """

        # import io module to create StringIO object
        # use redirect_stout to redirect print value to StringIO object for unittest
        import io
        from contextlib import redirect_stdout

        # first test with 4x4 sample
        version_imperative.V = 4
        version_recursion.V = 4
        output = io.StringIO()
        with redirect_stdout(output):
            version_recursion.printSolutionRecursive(self.graph0)

        expected_output = io.StringIO()
        with redirect_stdout(expected_output):
            version_imperative.printSolution(self.graph0)

        self.assertEqual(expected_output.getvalue(), output.getvalue())

        # first test with 3x3 sample
        version_imperative.V = 3
        version_recursion.V = 3
        output = io.StringIO()
        with redirect_stdout(output):
            version_recursion.printSolutionRecursive(self.graph)

        expected_output = io.StringIO()
        with redirect_stdout(expected_output):
            version_imperative.printSolution(self.graph)

        self.assertEqual(expected_output.getvalue(), output.getvalue())

        # then test with 6x6 sample
        version_imperative.V = 6
        version_recursion.V = 6
        output = io.StringIO()
        with redirect_stdout(output):
            version_recursion.printSolutionRecursive(self.graph1)

        expected_output = io.StringIO()
        with redirect_stdout(expected_output):
            version_imperative.printSolution(self.graph1)

        self.assertEqual(expected_output.getvalue(), output.getvalue())


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
