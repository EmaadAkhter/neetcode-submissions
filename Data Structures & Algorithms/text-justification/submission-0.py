class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        line,lenght=[],0
        i=0

        while i< len(words):
            
            if len(line) + lenght + len(words[i])>maxWidth:
                ex_space=maxWidth-lenght

                gaps=max(len(line)-1,1)

                sps=ex_space//gaps
                rem=ex_space % gaps

                for j in range(max(1,len(line)-1)):
                    line[j]+=" " * sps
                    if rem :
                        line[j]+=" "
                        rem-=1

                res.append("".join(line))
                
                line,lenght=[],0
            
            line.append(words[i])
            lenght+= len(words[i])
            i+=1
            
        last_line=" ".join(line)
        tr_sps=maxWidth-len(last_line)
        res.append(last_line + " " * tr_sps)

        return res
