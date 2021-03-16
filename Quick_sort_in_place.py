"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    def rec(array, i, ind):
        pivot = array[ind]
        j = array[i]
        if j >= pivot and i<ind:
            array[ind] = j
            array[i] = array [ind-1]
            array[ind-1] = pivot
            ind=ind-1
            return rec(array, i, ind)
        elif i==ind:
            return ind
        elif j<pivot:
            i += 1
            return rec(array,i, ind)
    

    def quick_sort(array, start =0, end = (len(array)-1) ):
    
        if end-start ==1 and array[end]<=array[start]:
                a = array[start]
                array[start] = array[end]
                array[end] = a
                
                
        elif end-start>1:
            pi = rec(array, start, end)
            quick_sort(array, start, end =(pi-1))
            start = pi+1
            quick_sort(array, start, end)
           
            
        else:
            return 

    
    quick_sort(array)
    return array
    
    
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]    
print quicksort(test)

