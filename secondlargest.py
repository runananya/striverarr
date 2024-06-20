#Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.
#brute force
arr.sort()
return arr[n-2]
#optimized
max=-1
secmax=-1
if (n<2):
   return -1
for i in range(n):
    if(arr[i]>max):
           secmax=max
           max=arr[i]
     elif(arr[i] > secmax and arr[i] != max):
           secmax=arr[i]
return secmax
