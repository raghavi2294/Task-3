def MinElement(lst):
   min = lst[0]
   for ele in lst:
      if ele < min :
         min = ele
   return min
lst = [100, 1, 5, 80, 20]
print("Smallest element of the list is:", MinElement(lst))