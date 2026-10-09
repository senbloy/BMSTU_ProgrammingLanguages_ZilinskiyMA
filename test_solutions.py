"""Проверки варианта 9: эталонные значения, границы и ошибочные данные."""
import math
import unittest
from Laboratory_work_01.solution import calculate
from Laboratory_work_02.solution import graph_value, contains
from Laboratory_work_03.solution import grid, atan_series, shots
from Laboratory_work_04.solution import analyze
from Laboratory_work_05.solution import smooth, below_diagonal_sum
from Laboratory_work_06.solution import process
from Laboratory_work_07.solution import exact_area, monte_carlo, curve_data


class SolutionsTest(unittest.TestCase):
    def test_formula_reference(self):
        cases = [(0, 0, 0), (0, math.pi, 4), (math.pi/2, -math.pi/2, -4),
                 (0, math.pi/2, 0), (math.pi, math.pi/2, 0)]
        for alpha, beta, expected in cases:
            for value in calculate(alpha, beta):
                self.assertAlmostEqual(value, expected, places=12)
        for alpha, beta in [(0.4, 1.2), (-2.3, 0.8), (9, -11)]:
            first, second = calculate(alpha, beta)
            self.assertAlmostEqual(first, second, places=12)

    def test_piecewise_graph(self):
        for x, expected in [(-7, 0), (-5, 2), (-3, 4), (-2.5, 4), (-2, 4),
                            (-1, 1), (0, 0), (1, 1), (2, 4), (3, 2), (4, 0)]:
            self.assertEqual(graph_value(x), expected)
        self.assertIsNone(graph_value(-7.001))
        self.assertIsNone(graph_value(4.001))

    def test_target_boundaries(self):
        for point in [(-2, 0), (0, -2), (-1, -1), (0, 0), (1, 0), (0, 1), (0, 2), (1, 1)]:
            self.assertTrue(contains(*point, 2), point)
        for point in [(1, -1), (-1, 1), (2, 1), (-2.001, 0), (0, 0.999)]:
            self.assertFalse(contains(*point, 2), point)

    def test_grid_and_shots(self):
        self.assertEqual(list(grid(-1, 1, 0.5)), [-1, -0.5, 0, 0.5, 1])
        self.assertEqual(list(grid(1, -1, -1)), [1, 0, -1])
        self.assertEqual(len(list(grid(0, 0.3, 0.1))), 4)
        data = list(shots(2, 9))
        self.assertEqual(len(data), 10)
        self.assertEqual(data, list(shots(2, 9)))

    def test_atan_accuracy_and_count(self):
        for eps in (1e-3, 1e-6):
            for x in (-1, -0.8, -0.2, 0, 0.3, 0.8, 1):
                result, count = atan_series(x, eps)
                self.assertLessEqual(abs(result-math.atan(x)), eps+1e-12)
                self.assertGreaterEqual(count, 1)
        self.assertEqual(atan_series(0), (0.0, 1))

    def test_array_reference(self):
        original = [0, 2, -3, 0, -1, 4, 0]
        self.assertEqual(analyze(original), (4, -4.0, [2, -3, -1, 4, 0, 0, 0]))
        self.assertEqual(original, [0, 2, -3, 0, -1, 4, 0])
        self.assertEqual(analyze([-5, 2, 3])[0], -5)
        self.assertEqual(analyze([1, 2])[1], 0)
        self.assertIsNone(analyze([0, -1, 2])[1])
        self.assertEqual(analyze([0, 0]), (0, None, [0, 0]))

    def test_smoothing_reference(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = smooth(matrix)
        expected = [[11/3, 19/5, 13/3], [23/5, 5, 27/5], [17/3, 31/5, 19/3]]
        for row, target in zip(result, expected):
            for value, wanted in zip(row, target):
                self.assertAlmostEqual(value, wanted)
        self.assertAlmostEqual(below_diagonal_sum(result), 23/5+17/3+31/5)
        self.assertEqual(matrix[0], [1, 2, 3])
        constant = [[-3]*10 for _ in range(10)]
        self.assertEqual(smooth(constant), constant)
        self.assertEqual(below_diagonal_sum(smooth(constant)), 135)
        self.assertEqual(smooth([[1, 2]]), [[2, 1]])

    def test_file_versions(self):
        self.assertIn("z1 = 4", process("1", f"0 {math.pi}"))
        self.assertIn("Сумма: -4", process("4", "7\n0 2 -3 0 -1 4 0"))
        self.assertIn("Сглаженная матрица", process("5", "2 2\n1 2\n3 4"))
        for task, text in [("1", "0"), ("4", "3 1 2"), ("5", "2 2 1")]:
            with self.assertRaises(ValueError):
                process(task, text)

    def test_area_independent_quadrature(self):
        # Независимый эталон: составная формула средней точки, без поиска корней.
        count = 100000
        for radius in (0.25, 0.7, 1, 2, 4):
            width = radius / count
            integral = math.fsum(max(0, math.sqrt(radius**2-((i+0.5)*width)**2)
                                     - ((i+0.5)*width-1)**2) * width for i in range(count))
            reference = math.pi*radius**2/4 + integral
            self.assertAlmostEqual(exact_area(radius), reference, delta=2e-5)
        self.assertAlmostEqual(exact_area(0.25), math.pi*0.25**2/4)

    def test_monte_carlo_and_graph_points(self):
        data, estimated, reference, error = monte_carlo(2, 10000, 9)
        self.assertEqual(len(data), 10000)
        self.assertLess(error, 5)
        self.assertAlmostEqual(error, abs(estimated-reference)/reference*100)
        for task, bounds in [("1", (-7, 4)), ("3", (-1, 1))]:
            points = curve_data(task, *bounds)
            self.assertEqual(points[0][0], bounds[0])
            self.assertEqual(points[-1][0], bounds[1])
            self.assertTrue(all(math.isfinite(y) for _, y in points))

    def test_invalid_inputs(self):
        calls = [lambda: calculate(math.nan, 0), lambda: graph_value(math.inf),
                 lambda: contains(0, 0, 0), lambda: list(grid(0, 1, 0)),
                 lambda: list(grid(0, 1, -1)), lambda: atan_series(1.1),
                 lambda: atan_series(0, 0), lambda: analyze([]),
                 lambda: analyze([math.nan]), lambda: smooth([[1]]),
                 lambda: smooth([[1, 2], [3]]), lambda: monte_carlo(2, 10001),
                 lambda: exact_area(-1), lambda: curve_data("3", -2, 1)]
        for call in calls:
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
