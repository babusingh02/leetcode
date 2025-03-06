class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = cur_alt = 0

        for x in gain:
            cur_alt += x
            highest_alt = max(highest_alt, cur_alt)
        
        return highest_alt