def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        print(i,j)
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
            print(arr)
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    print(arr)
    return ( i+1 ) 

print(partition([4, 1, 3, 9, 7],0,4))