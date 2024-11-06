class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=[]
        for i in range (len(word)):
            if word [i]!=ch:
                 stack.append(word[i])
            else:
                s = ch
                while(stack):
                    s += stack.pop()
                return s + word[i+1:]
        return word
                