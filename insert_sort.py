class Solution(object):

    def insert_sort(self, array):
        length = len(array)
        for i in range(1, length):
            key = array[i]
            j = i-1;
            while j >=0:
                if key < array[j]:
                    array[j + 1] = array[j]
                    array[j] = key
                j -= 1
        return array


if __name__ == "__main__":
    array = [5, 3, 2, 4, 8, 12, 9]
    print(array)
    Solution().insert_sort(array)
    print(array)
