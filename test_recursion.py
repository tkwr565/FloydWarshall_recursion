import unittest
import version_imperative
import version_recursion

INF = 99999

print("This is the unittest")


class FloydWarshallTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case with sample data
        """
        # first sample with 3x3 matrix
        self.V0 = 3
        self.graph = [
            [0, 2, 9],
            [2, 0, INF],
            [6, INF, 0],
        ]

        # second sample with 6x6 matrix
        self.V1 = 6
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

        # first test with 3x3 sample
        expected_output = version_imperative.floydWarshallImperative(
            self.graph, V=self.V0
        )
        dist = [row[:] for row in self.graph]
        result = version_recursion.floydWarshallRecursive(
            self.graph, dist, 0, 0, 0, V=self.V0
        )
        self.assertEqual(result, expected_output)

        # then test with 6x6 sample
        expected_output = version_imperative.floydWarshallImperative(
            self.graph1, V=self.V1
        )
        dist = [row[:] for row in self.graph1]
        result = version_recursion.floydWarshallRecursive(
            self.graph1, dist, 0, 0, 0, V=self.V1
        )
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

        # first test with 3x3 sample
        output = io.StringIO()
        with redirect_stdout(output):
            version_recursion.printSolutionRecursive(self.graph, V=self.V0)

        expected_output = io.StringIO()
        with redirect_stdout(expected_output):
            version_imperative.printSolution(self.graph, V=self.V0)

        self.assertEqual(expected_output.getvalue(), output.getvalue())

        # then test with 6 x 6 sample
        output = io.StringIO()
        with redirect_stdout(output):
            version_recursion.printSolutionRecursive(self.graph1, V=self.V1)

        expected_output = io.StringIO()
        with redirect_stdout(expected_output):
            version_imperative.printSolution(self.graph1, V=self.V1)

        self.assertEqual(expected_output.getvalue(), output.getvalue())


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
