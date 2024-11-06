class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_occ=[0]*10
        g_occ=[0]*10
        bulls=0
        cows=0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls +=1
            else:
                s_occ[int(secret[i])] += 1
                g_occ[int(guess[i])] += 1
        for i in range(10):
            cows +=min(s_occ[i],g_occ[i])
        return str(bulls) +'A'+str(cows)+'B'






        