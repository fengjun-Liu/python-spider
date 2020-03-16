def merge_sort(lst):
  if len(lst)<=1:
    return lst
  middle=int(len(lst)/2)
  left=merge_sort(lst[:middle])
  right=merge_sort(lst[middle:])
  merged=[]
  while left and right:
    merged.append(left.pop(0) if abs(left[0])<=abs(right[0]) else right.pop(0))
  merged.extend(right if right else left)
  return merged

alist=list(map(int,input().split()))
print(merge_sort(alist))