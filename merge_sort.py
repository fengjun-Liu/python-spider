def merge_sort(lst):
  if len(lst)<=1:
    return lst
  middle=int(len(lst)/2)
  left=merge_sort(lst[:middle])
  right=merge_sort(lst[middle:])
  merged=[]
  while left and right:
    merged.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
  merged.extend(right if right else left)
  return merged

data_lst=[6,202,100,301,38,8,1]
print(merge_sort(data_lst))