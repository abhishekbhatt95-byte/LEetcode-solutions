class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)

        for num in nums:
            rev = 0
            x = num

            while x:
                rev = rev * 10 + x % 10
                x //= 10

            s.add(rev)

        return len(s)