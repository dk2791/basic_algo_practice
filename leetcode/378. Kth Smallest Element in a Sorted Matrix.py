class Solution:
    def kthSmallest(self, matrix, k):
        from functools import reduce
        array = reduce(lambda x, y: x+y, matrix)
        return sorted(array)[k-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
    print(sol.kthSmallest(matrix=[[-5]], k=1))
