class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i == ']':
                str1=''
                while(stack and stack[-1]!='['):
                    str1=stack.pop()+str1
                if stack:
                    stack.pop()
                n=''
                while(stack and stack[-1].isdigit()):
                    n=stack.pop()+n
                new_str=int(n)*str1
                stack.append(new_str)


            else:
                stack.append(i)
            out_str=''
            for i in stack:
                out_str+=i
        return out_str
        