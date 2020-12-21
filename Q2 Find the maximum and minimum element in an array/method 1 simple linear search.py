class Pair:
    def __init__(self):
        self.min=0
        self.max=0

def getMinMax(arr,n):
    minmax = Pair()

    if n==1:
        minmax.min = arr[0]
        minmax.max = arr[0]
    # if n==2:
    #     if arr[0]>arr[1]:
    #         minmax.min,minmax.max = arr[1],arr[0]
    if arr[0]>arr[1]:
        minmax.min,minmax.max = arr[1],arr[0]
    else:
        minmax.min,minmax.max = arr[0],arr[1]

    # minmax.min=1
    for i in range(2,n):
        if arr[i]<minmax.min:
            minmax.min=arr[i]
        elif arr[i]>minmax.max:
            minmax.max = arr[i]

    return minmax



# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
 
# This code is contributed by
# sanjeev2552