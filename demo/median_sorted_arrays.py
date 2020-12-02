
def merge(nums1,nums2):
    i=0;
    j=0;
    a=len(nums1)
    b=len(nums2)
    ans=list()
    while ((i<a) or (j<b)):
    if ((i<a) and (j<b) and (nums1[i]<nums2[j])):
        ans.append(nums1[i])
        i=i+1
    elif (j>=b):
        ans.append(nums1[i])
        i=i+1
    else:
        ans.append(nums2[j])
        j=j+1
    return ans

def median(arr):
  if len(arr)%2:
    return (arr[int(len(arr)/2)])
  else:
    return (arr[len(arr)//2-1]+arr[len(arr)//2])/2

if __name__=='__main__':
    nums1 = [1,4,6]
    nums2 = [2,4,5]
    print(median(merge(nums1,nums2)))