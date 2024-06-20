largest number in array
#brute force
arr.sort()
return arr[n-1]
#optimized
max=arr[0]
for i in range(n):
   if (arr[i]>max):
           max=arr[i]
return max
