class Solution:
    def minJumps(self, arr, n):
        if arr[0] == 0:
            return -1

        start = 0
        jumps = 0
        while start < len(arr):
            if arr[start] == 0:
                return -1
            jumps += 1
            i, j = start + 1, start + 1 + arr[start]
            # find max in that range and that is going to be next start
            print(start, i, j)
            max_value = arr[i]
            offset = 1
            for k in range(i, j + 1):
                if arr[k] >= max_value:
                    offset += k
                    max_value = arr[k]

            start = start + offset
        return jumps


soln = Solution()
print(soln.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11))
