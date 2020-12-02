class sub_palindrome :
    def palindrome_check_slow(self,s:str) -> bool :
        traverse=int(len(s)/2)
        max_length =len(s)-1
        for i in range(0,traverse):
            if s[i]==s[max_length-i]:
                continue
            else : 
                return False
        return True
    def palindrome_check(self,s:str) -> bool :
        return True if s==s[::-1] else False
    def check_substring(self,s: str) ->str:
        max_position=len(s)
        for window in range(max_position,0,-1):
            for pos in range(0,max_position-window+1):
                if self.palindrome_check(s[pos:pos+window]):
                    return s[pos:pos+window]
        return s[0] if len(s)>0 else s
    def update_palindrome(self,ans:str,tmp:str) -> str :
        if self.palindrome_check(tmp):
            return tmp if len(tmp) > len(ans) else ans
        return ans
    def get_middle_palindrome(self,s:str,l:int,r:int) -> str :
        for window in range(r-l,1,-1):
            for pos in range(l,r-window+1):
                if self.palindrome_check(s[pos:pos+window]):
                    return (pos,pos+window)
        else:
            return (r-1,r)
    def expand_middle_palindrome(self,s:str,l:int,r:int):
        i=l
        j=r
        size=len(s)
        ans=''
        while (i>=0 and j<size):
            tmp=s[i:j]
            ans=self.update_palindrome(ans,tmp)
            i=i-1
            j=j+1
        return ans
    def substring_divide(self,s:str) -> str :
        size=len(s)
        limit=6
        ans=''
        if size>=limit:
            n=size//limit
            div=[]
            for i in range(0,n):
                div.append(limit*i)
            div.append(size)
            centers=list()
            for i in range(0,n):
                result=self.get_middle_palindrome(s,div[i],div[i+1])
                if result:
                    centers.append(result)
            for i in centers:
                tmp=self.expand_middle_palindrome(s,i[0],i[1])
                ans = tmp if len(ans) < len(tmp) else ans 
            if ans :
                return ans 
            else :
                return s[0] if len(s)>0 else s
        else :
            return self.check_substring(s)
                        

if __name__=="__main__":
    import time
    solution=sub_palindrome()
    string=input('provide a string :')
    start=time.time()
    print('sub_string result is : ' + solution.substring_divide(string))
    stop=time.time()
    print('solution in seconds : ', stop-start)