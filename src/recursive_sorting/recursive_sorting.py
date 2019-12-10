# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # TO-DO
    arr = []
    a,b = 0,0
    while a<len(arrA) and b < len(arrB):
        if arrA[a]<arrB[b]:
            arr.append(arrA[a])
            a+=1
        else:
            arr.append(arrB[b])
            b+=1
    if a==len(arrA): arr.extend(arrB[b:])
    else: arr.extend(arrA[a:])
    
    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <=1: return arr

    #split the list in half / call the merge sort recursiveley
    lgt = int(len(arr) / 2)
    left, right = merge_sort(arr[:lgt]), merge_sort(arr[lgt:])

    return merge(left, right)


   


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
