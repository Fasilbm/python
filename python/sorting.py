#selection sort
'''
arr=[1,5,9,7,6,2]
for i in range(len(arr)-1):
    minmum=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[minmum]:
            minmum=j
    arr[i],arr[minmum]=arr[minmum],arr[i]
    
print(arr)
# insertion sort     
nums=[7,9,6,2,4,5]
for i in range(len(nums)):
     for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)
#Bubble sort
arr=[4,3,2]
for i in range (0,len(arr)):
    swapped=False
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break
print(arr)

#Quick sort
def quick(arr,left,right):
    if left<right:
        pos=posidx(arr,left,right)
        quick(arr,left,pos-1)
        quick(arr,pos+1,right)
def posidx(arr,left,right):
    i=left
    j=right
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],pivot=pivot,arr[i]
    return i


quick(arr,0,len(arr)-1)
print(arr)


#merge_sort
arr=[4,6,1,3,5,7,1,6]
def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i=0
        j=0
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
merge_sort(arr)
print(arr)


brute approch for constant window
nums=[1, 4, 7, 3, 2, 4, 1, 0]
res=[]
k=3
start=0
end=3
for i in range (0,len(nums)-k+1):
    sum=0
    for j in range(start,end):
        sum+=nums[j]
    res.append(sum)
    start+=1
    end+=1
print(*res)


#sliding window approch for constant width

arr=[2,3,2,4,6,6]
k=3
curr_sum=0
start=0
res=[]
for i in range(0,len(arr)):
    curr_sum+=arr[i]
    while i-start==k-1:
        res.append(curr_sum)
        curr_sum-=arr[start]
        start+=1
# attempt to design a dynamic sliding window using a brute force soln
nums=[1,3,1,2,2,3]
target=7
list=[]
head=0
tail=1
for i in range(0,len(nums)):
    if nums[head]>=target:
        print(1)
    while(head!=tail) and tail<len(nums):
        if nums[head]+nums[tail]<target:
            tail+=1
        elif nums[head]+nums[tail]>=target:
            length=tail-head+1
            list.append(length)
            head+=1
            continue
print(min(list))


#optmized dynamic sliding window with time complexity of 
arr=[1,4,4]
curr_sum=0
start=0
target=4
res=len(arr)+1
for i in range(len(arr)):
    curr_sum+=arr[i]
    while curr_sum>=target:
        res=min(i-start+1,res)
        curr_sum-=arr[start]
        start+=1
print(res)

s="abccbcbb"
l=0
char=set()
res=0
for i in range(len(s)):
    while s[i] in char:
        char.remove(s[l])
        l+=1
    char.add(s[i])
    res=max(res,i-l+1)


#[3,3,5,5,6,7]
nums=[1]
k=1
start=0
new=[]
for i in range(0,len(nums)):
    res=[]
    while i-start==k-1:
        for j in range(i-2,i+1):
            res.append(nums[j])
        new.append(max(res))
        start+=1    
print(new)
    
n=int(input())
for i in range(0,n):
    list=[]
    d=int(input())
    for i in range (0,d):
        ele=int(input())
        list.append(ele)
  
    next=1
    count1=0
    count2=0
    for r in range(len(list)-1,-1,-2):
       
        if list[r]%2==0:
            count1+=1
        else:
            count2+=1
    if count1!=0 and count2!=0:
        print('NO')
        next=0
        break
    if next==1:
        count1=0
        count2=0

        for t in range(len(list)-2,-1,-2):
             
             if list[r]%2==0:
                 count1+=1
             else:
                 count2+=1
        if count1!=0 and count2!=0:
            print('NO')
            next=0
            break
    if next==1:
        print('YES')
    

from collections import Counter
def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))


from collections import Counter
nums = [1,1,1,2,2,3]
k = 2
shash=Counter(nums)
new=[]
res=[]
for i in shash:
    new.append(shash[i])
new.sort(reverse=True)
for i in range(k):
   res.append(shash.get(new[k])) 

print(new)

     
arr=[3,3,3,3,5,5,5,2,2,7]
new=[[] for i in range(len(arr)+1)]
res=[]
numsHash={}
for i in arr:
    numsHash[i]=1+numsHash.get(i,0)
for i,j in numsHash.items():
            new[j].append(j)
for i in range(len(arr),0,-1):
            for j in new[i]:
                res.append(j)
                if sum(res)>=len(arr)//2:
                    print(len(res))

from inspect import stack
matrix=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
row1,col1,row2,col2=2,1,4,3
row,col=len(matrix),len(matrix[0])
prefix_matrix=[[0]*(col+1)for i in range(row+1)]
for r in range(row):
            prefix=0
            for c in range(col):
                prefix+=matrix[r][c]
                above=prefix_matrix[r][c+1]
                prefix_matrix[r+1][c+1]=prefix+above
row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
above=prefix_matrix[row1-1][col2]
left=prefix_matrix[row2][col1-1]
bottom_right=prefix_matrix[row2][col2]
top_left=prefix_matrix[row1-1][col1-1]
print(bottom_right-above-left+top_left)
t=[]
s = "dztz"
shifts = [[0,0,0],[1,1,1]]
prefix=[0 for i in range(len(s)+2)]
for i in range(len(shifts)):
    j=(shifts[i][0])
    k=(shifts[i][1])
    if shifts[i][-1]==1:
        prefix[j]+=1
    else:
        prefix[j]+=-1
    
    if shifts[i][-1]==1:
         prefix[k+1]+=-1
    else:
        prefix[k+1]+=1
for i in range(len(prefix)):
        prefix[i]=prefix[i]+prefix[i-1]
for i,c in enumerate(s):
    t.append(chr(((ord(c)-ord('a')+prefix[i])%26)+97))
print("".join(t))
'''
s = "abciiidef"
k = 3
vowels="aeiou"
count=0
start=0
res=0
for i,j in enumerate(s):
    if j in vowels:
        count+=1
    while i-start==k-1:
        res=max(count,res)
        if s[start] in vowels:
            count-=1
        start+=1
print(res)       





    
