import unittest

class Solution(object):
    def shell_sort(self, array):
        length = len(array)
        inc = int(length/2)
        while inc >0:
            for i in range(inc):
                for j in range(i+inc, length, inc):
                    key = array[j]
                    k = j
                    while k > i:
                        if key < array[k-inc]:
                            array[k] = array[k-inc]
                            array[k-inc] = key
                        k = k - inc
            inc = int(inc/2)
        return array

class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        array = [2, 8, 9, 4, 6, 3, 1, 7, 5]
        array_1 = Solution().shell_sort(array)
        array_2 = sorted(array)
        self.assertEqual(array_1, array_2)

if __name__ == "__main__":
    unittest.main()
