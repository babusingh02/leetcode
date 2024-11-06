class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char not in seen:
                while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return ''.join(stack)