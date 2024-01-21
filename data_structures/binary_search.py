
def binary_search(l1: list, key: int):
    start = l1[0]
    end = len(l1) - 1
    
    while start <= end:
        mid = (start + end)//2
        
        if l1[mid] == key:
            return mid
        
        elif l1[mid] < key:
            start = mid+1
            
        else:
            end = mid - 1 
    
    return mid
        


l1 = [1,2,3,4,5,6,7,8,9]

key = 2

index = binary_search(l1,key)

print(index)