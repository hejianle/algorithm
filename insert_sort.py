class Solution(object):

    def insert_sort(self, array):
        length = len(array)
        for i in range(1, length):
            key = array[i]
            j = i;
            while j > 0:
                if key < array[j-1]:
                    array[j] = array[j-1]
                    array[j-1] = key
                j -= 1
                print(j)
        return array


if __name__ == "__main__":
    array = [5, 3, 2, 4, 8, 12, 9]
    print(array)
    Solution().insert_sort(array)
    print(array)
