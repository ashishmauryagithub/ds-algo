# import test

def getMinMax(arr):
    n=len(arr)
    if(n%2 == 0):
        amax = max(arr[0],arr[1])
        amin = min(arr[0],arr[1])
        i=2
    else:
        amax = amin = arr[0]
        i=1
    while(i<n-1):
        if arr[i]<arr[i+1]:
            amax = max(amax,arr[i+1])
            amin = min(amin,arr[i])
        else:
            amax = max(amax,arr[i])
            amin = min(amin,arr[i+1])
        i+=2
    return (amax,amin)

# Driver Code
if __name__ =='__main__':
     
    arr = [1000, 11, 445, 1, 330, 3000]
    # arr = test.l
    mx, mn = getMinMax(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)
     
# This code is contributed by Kaustav