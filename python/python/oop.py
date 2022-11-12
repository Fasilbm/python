'''
def sum():
 list = [2,9,11,15,7]
 target=9
 for i in range(len(list)):
        for j in range (i+1,len(list)):
             if list[i]+list[j]==target:
               print([i],[j])

nums=[5,7,6,2,7,5] 
target=6
sorted_List=[]
      
i=len(nums)-1
while i>1:
  j=0
  while j<i:
     if nums[j]>nums[j+1]:
      temp=nums[j]
      nums[j]=nums[j+1]
      nums[j+1]=temp

     else:
       j+=1
  i-=1
for i in range (len(nums)):
  if nums[i]==target:
    sorted_List.append(i)
print(sorted_List)


nums=[2,5,1,5,6,7,8,6]
target=6
nums.sort()
print(nums)
b=[]
def sorting(nums): 
  for i in range(len(nums)):
    if nums[i]==target:
      b.append(i)
      return b
print(sorting(nums))

''' 
list=[1000,9,6,7,3,75,274,65,2,1,5]
'''
def selection_sort(list):
 for i in range(len(list)):
    cur_min=i
    for j in range(i+1,len(list)):
                if list[j]<list[cur_min]:
                  cur_min=j
                    
    list[i],list[cur_min]=list[cur_min],list[i]
 return list
selection_sort(list)
print(list)
      

def insertion_sort(list):
  for i in range(1,len(list)):
    j=i
    while list[j-1]>list[j] and j>0:
      list[j-1],list[j]=list[j],list[j-1]
      j-=1
insertion_sort(list)
print(list)

def merge_sort(list):
  if len(list)>1:
   lft_list=list[0:len(list)//2]
   rht_list=list[len(list)//2:len(list)]

   merge_sort(lft_list)
   merge_sort(rht_list)

   i,j,k=0,0,0

   while i<len(lft_list) and j<len(rht_list):
    if lft_list[i]<rht_list[j]:
      list[k]=lft_list[i]
      i+=1
      k+=1
    else:
      list[k]=rht_list[j]
      j+=1
      k+=1
   while i<len(lft_list):
    list[k]=lft_list[i]
    i+=1
    k+=1
   while j<len(rht_list):
    list[k]=rht_list[j]
    j+=1
    k+=1
merge_sort(list)
print(list)
  '''
list=[1000,9,6,7,3,75,274,65,2,1,5,8]
def quick_sort(list):
  if len(list)<=1:
    return list
  else: 
     pivot=list.pop()

  lft=[]
  rht=[]

  for i in list:
    if i>pivot:
      rht.append(i)
    else:
      lft.append(i)
  return quick_sort(lft)+[pivot]+quick_sort(rht)

print(quick_sort(list))

1000,9,6,7,3,75,274,65,2,1

   1000,9,6,7,3                                75,274,65,2,1

         1000,9,6    7,3              75,274,65  2,1

              1000,9  6    7  3      75,274, 65   2  1
 
          1000 * 9   6    7*   3           75*        274        65      2*        1

           9,3






