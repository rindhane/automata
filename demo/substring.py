class Solution:
    def big_string(self,string,ans):
        if len(string)>len(ans):
            return string
        else:
            return ans
    def traverse(self,string):
        start=list()
        for i in string:
            if i in start:
                yield ''.join(start)
                tmp=start[::-1]
                start=tmp[0:tmp.index(i)]
                start.reverse()
                start.append(i)
            else:
                start.append(i)
        yield ''.join(start)
    def fast_traverse(self,string):
        start=set()
        for i in string:
            if i in start:
                yield ''.join(start)
                start=set()
                start.update(i)
            else:
                start.update(i)
        yield ''.join(start)
    def get_substring(self,string):
        ans=''
        try :
            string_iter=self.traverse(string=string)
            while True:
                tmp=next(string_iter)
                ans=self.big_string(tmp,ans)
        except StopIteration:
            pass
        finally:    
            return ans
    def lengthOfLongestSubstring(self, s) :
        ans=0
        try :
            string_iter=self.fast_traverse(string=s)
            while True:
                tmp=next(string_iter)
                tmp =len(tmp)
                ans= ans if tmp < ans else tmp
        except StopIteration:
            pass
        finally:    
            return ans
        

if __name__=="__main__":
    string=input('Enter the string')
    sol=Solution()
    print(sol.lengthOfLongestSubstring(s=string))
    print(sol.get_substring(string=string))