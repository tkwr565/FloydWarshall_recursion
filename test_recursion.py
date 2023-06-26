import unittest
import version_imperative
import version_recursion

INF = 99999


class FloydWarshallTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case with sample data
        """
        self.graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0],
        ]

    def test_floydWarshall(self):
        """
        capture and compare the output of floydwarshall algorithm calculation function of recursion
        and imperative version
        """
        expected_output = version_imperative.floydWarshallImperative(self.graph)
        #        print(self.graph)
        dist = [row[:] for row in self.graph]
        result = version_recursion.floydWarshallRecursive(self.graph, dist, 0, 0, 0)
        #        print(result)
        #        print(expected_output)
        self.assertEqual(result, expected_output)

    def test_printSolution(self):
        """
        capture and compare the output of print functions of recursion and imperative version
        by printing example graph
        """
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()
        with redirect_stdout(output):
            version_recursion.printSolutionRecursive(self.graph)

        expected_output = io.StringIO()
        with redirect_stdout(expected_output):
            version_imperative.printSolution(self.graph)

        self.assertEqual(expected_output.getvalue(), output.getvalue())


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
