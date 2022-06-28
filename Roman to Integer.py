class Solution:
    def romanToInt(self, s: str) -> int:
        
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l = len(s)
        if l==1:
            return d[s[0]] 
        total=d[s[l-1]]
        for i in range(l-1,-1,-1):
            if((i-1)<0):
                return total
            if(d[s[i]] <= d[s[(i-1)]]):
                total+=d[s[i-1]]
            else:
                total-=d[s[i-1]]
                
        return total
            
            
            
            
