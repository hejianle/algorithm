import unittest

class Solution(object):
    def abs_power(self, a, n):
        result = 1.0
        for i in range(n):
            result = result * a

        return result

    def power(self, a, n):
        if a == 0.0 and n < 0:
            return 0.0
        if n == 0:
            return 1.0
        if n > 0:
            return self.abs_power(a, n)
        if n < 0:
            return 1/self.abs_power(a, -n)


class TestPower(unittest.TestCase):

    def test_positive_n(self):
        a = 1.1
        n = 2
        result = Solution().power(a, n)
        self.assertEqual(result, a * a)

    def test_negtive_n(self):
        a = 1.1
        n = -3
        result = Solution().power(a, n)
        self.assertEqual(result, 1 / (a * a * a))

    def test_zero_a(self):
        a = 0.0
        result = Solution().power(a, 0)
        self.assertEqual(result, 1.0)
        result = Solution().power(a, 1)
        self.assertEqual(result, 0.0)
        result = Solution().power(a, -1)
        self.assertEqual(result, 0.0)

    def test_negtive_a(self):
        a = -1.1

        result = Solution().power(a, -2)
        self.assertEqual(result, 1/(a * a))
        result = Solution().power(a, -3)
        self.assertEqual(result, 1/(a * a * a))
        result = Solution().power(a, 3)
        self.assertEqual(result, (a * a * a))

if __name__ == "__main__":
    unittest.main()

