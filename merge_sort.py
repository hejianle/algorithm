import unittest

class Solution:
    def merge_sort(self, array):
        length = len(array)
        if length <= 1:
            return array
        cut = length // 2
        left = self.merge_sort(array[:cut])
        right = self.merge_sort(array[cut:])
        return self.merge(left, right)

    def merge(self, array1, array2):
        len1 = len(array1)
        len2 = len(array2)
        l = 0
        r = 0
        result = []
        while l < len1 and r < len2:
            if array1[l] < array2[r]:
                result.append(array1[l])
                l = l + 1
            else:
                result.append(array2[r])
                r = r + 1
        if l < len1:
            result += array1[l:]
        if r < len2:
            result +=array2[r:]
        return result

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        array1 = [7, 2, 8, 9, 1, 4, 6, 3, 5]
        array2 = [7, 2, 8, 9, 1, 4, 6, 3, 5]
        result = Solution().merge_sort(array1)
        array2.sort()
        self.assertEqual(result, array2)

    def test_merge(self):
        array1 = [1, 3, 5, 7, 9]
        array2 = [2, 4, 6, 8, 10]
        result = Solution().merge(array1, array2)
        array3 = [i for i in range(1, 11)]
        self.assertEqual(result, array3)

if __name__ == "__main__":
    unittest.main()
