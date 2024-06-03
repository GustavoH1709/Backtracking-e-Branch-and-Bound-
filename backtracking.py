from typing import List

class Backtracking:
    def create_factorial_list(self, num: int) -> List[int]:
        return list(range(1, num + 1))

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:]) 
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans

bt = Backtracking()

factorial_list = bt.create_factorial_list(3)
permutations = bt.permute(factorial_list)
print(permutations)