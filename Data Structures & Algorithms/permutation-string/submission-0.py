class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_c,s2_c=[0]*26,[0]*26
        for i in range(len(s1)):
            s1_c[ord(s1[i])-ord('a')]+=1
            s2_c[ord(s2[i])-ord('a')]+=1
        
        matchs=0

        for i in range(26):
            matchs+=(1 if s1_c[i] == s2_c[i] else 0)

        l=0
        for r in range(len(s1),len(s2)):
            if matchs == 26:
                return True

            index = ord(s2[r])-ord('a')
            s2_c[index]+=1
            if s1_c[index]==s2_c[index]:
                matchs +=1

            elif s1_c[index]+1==s2_c[index]:
                matchs -=1

            index = ord(s2[l])-ord('a')
            s2_c[index]-=1
            if s1_c[index]==s2_c[index]:
                matchs +=1

            elif s1_c[index]-1==s2_c[index]:
                matchs -=1
            l+=1
        return matchs == 26
