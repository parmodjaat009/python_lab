class Solution:

    # Search function
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    # Power function
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result = result * x

            x = x * x
            n = n // 2

        return result


# Main program
obj = Solution()

# Search
nums = [1, 3, 5, 7, 9, 11]
target = 7

index = obj.search(nums, target)

print("Array:", nums)
print("Target:", target)
print("Index:", index)

# Power
x = 2
n = 5

answer = obj.myPow(x, n)

print("Base:", x)
print("Exponent:", n)
print("Power:", answer)