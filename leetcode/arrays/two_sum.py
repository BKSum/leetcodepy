from typing import List

class SolutionTwo:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        nums.sort()
        leftPointer = 0
        rightPointer = len(nums)-1
        while leftPointer < rightPointer:
            tempSum = nums[leftPointer] + nums[rightPointer]
            if tempSum == target:
                return [leftPointer, rightPointer]
            elif tempSum < target:
                leftPointer+=1
            else:
                rightPointer-=1
        return[]
