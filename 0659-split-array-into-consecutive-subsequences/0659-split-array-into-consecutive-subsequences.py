from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Complexity:
        # - Time: O(N)
        #   where `N` is the length of `nums`
        # - Time: O(1)

        # Iterate over the numbers
        # We keep count of the number of subsequences that finish with the previous value
        numIter = iter(nums)
        nextNum = next(numIter)
        num = nextNum - 1  # Dummy value to make the first iteration work fine
        lenOneCount = lenTwoCount = lenThreeAndAboveCount = 0

        while True:
            # If the next number is not consecutive then we need extra action
            if nextNum > num + 1:
                # If there are subsequences of length 1 or 2 then it's impossible.
                if lenOneCount > 0 or lenTwoCount > 0:
                    return False
                # Otherwise, we need to reset the subsequences counts.
                lenThreeAndAboveCount = 0  # At this point, `lenOneCount` and `lenTwoCount` are already 0

            # Count the number of occurrences of the current number
            num, count, endOfListReached = nextNum, 1, False
            for nextNum in numIter:
                if nextNum != num:
                    break
                count += 1
            else:
                endOfListReached = True

            # We must have enough occurrences to extend the subsequences of length 1 and 2 that end with the previous value
            minCountNeeded = lenOneCount + lenTwoCount
            if count < minCountNeeded:
                return False

            # Determine the number of subsequences that finish with the current value
            countExcess = count - (lenOneCount + lenTwoCount + lenThreeAndAboveCount)
            if countExcess >= 0:
                lenOneCount, lenTwoCount, lenThreeAndAboveCount = countExcess, lenOneCount, lenThreeAndAboveCount + lenTwoCount
            else:  # countExcess < 0
                lenOneCount, lenTwoCount, lenThreeAndAboveCount = 0, lenOneCount, lenThreeAndAboveCount + lenTwoCount + countExcess

            if endOfListReached:
                break

        # Once done, we should have no subsequences of length 1 or 2 left
        return lenOneCount == 0 and lenTwoCount == 0