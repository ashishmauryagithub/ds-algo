def findmaxmin(l,h,arr):
    amax = amin =  arr[l]
    if l==h:
        amax = amin = arr[l]
        return amax,amin
    elif h == l+1:
        if arr[l]>arr[h]:
            amax  = arr[l]
            amin = arr[h]
            return(amax,amin)
        else:
            (amax,amin) = (arr[h],arr[l])
            return(amax,amin)
    else:
        mid = (l+h)//2
        amx1,amn1 = findmaxmin(l,mid,arr)
        amx2,amn2 = findmaxmin(mid+1,h,arr)
    return(max(amx1,amx2),min(amn1,amn2))


l = [i for i in range(1,101)]

print(findmaxmin(0,99,l))

# def kthsmallest(A,B):
    
#     i=0
#     while i < B:
#         a.remove(min(a))
#         print(min(a))
#         i+=1
#     return min(a)
# if __name__ == "__main__":
    
#     B=9
#     A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
#     print(kthsmallest(A,B))