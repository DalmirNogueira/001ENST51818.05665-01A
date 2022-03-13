from numpy import random
from datetime import datetime
import sys
x=random.randint(100000, size=(100000))
sys.setrecursionlimit(len(x))
x2=x.copy()
x3=x.copy()
x4=x.copy()
x5=x.copy()
#print(x)


print("RANDOM")

start_time = datetime.now() 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = x
bubbleSort(arr)
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

x=arr
    
print('Duration bubbleSort: {}'.format(end_time - start_time))


start_time = datetime.now() 
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
arr = x2
insertionSort(arr)
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")
    
print('Duration insertionSort: {}'.format(end_time - start_time))

start_time = datetime.now() 
arr3=x3
for i in range(len(arr3)):
      
    min_idx = i
    for j in range(i+1, len(arr3)):
        if arr3[min_idx] > arr3[j]:
            min_idx = j
                 
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]

end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration selectionSort: {}'.format(end_time - start_time))

start_time = datetime.now() 

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0    
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

 
 
def mergeSort(arr, l, r):
    if l < r:

        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 

arr = x4
n = len(arr)
mergeSort(arr, 0, n-1)


end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration mergeSort: {}'.format(end_time - start_time))


start_time = datetime.now() 
#y=random.randint(len(x5))
y=len(x5)//2
print (y)
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[y]     
 
    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
  
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, low, high )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
  
arr = x5
n = len(arr)
quickSort(arr, 0, n-1)
    
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration quickSort: {}'.format(end_time - start_time))

print("ASCENDING")

x2=x.copy()
x3=x.copy()
x4=x.copy()
x5=x.copy()

start_time = datetime.now() 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = x
bubbleSort(arr)
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

x=arr
    
print('Duration bubbleSort: {}'.format(end_time - start_time))


start_time = datetime.now() 
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
arr = x2
insertionSort(arr)
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")
    
print('Duration insertionSort: {}'.format(end_time - start_time))

start_time = datetime.now() 
arr3=x3
for i in range(len(arr3)):
      
    min_idx = i
    for j in range(i+1, len(arr3)):
        if arr3[min_idx] > arr3[j]:
            min_idx = j
                 
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]

end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration selectionSort: {}'.format(end_time - start_time))

start_time = datetime.now() 

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0    
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

 
 
def mergeSort(arr, l, r):
    if l < r:

        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 

arr = x4
n = len(arr)
mergeSort(arr, 0, n-1)


end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration mergeSort: {}'.format(end_time - start_time))


start_time = datetime.now() 
#y=random.randint(len(x5))
y=len(x5)//2
#print(y)
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[y]     
 
    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
  
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, low, high )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
  
arr = x5
n = len(arr)
quickSort(arr, 0, n-1)  

end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration quickSort: {}'.format(end_time - start_time))


print("DESCENDING")

x=x[::-1]
x2=x.copy()
x3=x.copy()
x4=x.copy()
x5=x.copy()

start_time = datetime.now() 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = x
bubbleSort(arr)
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")
    
print('Duration bubbleSort: {}'.format(end_time - start_time))


start_time = datetime.now() 
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
arr = x2
insertionSort(arr)
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")
    
print('Duration insertionSort: {}'.format(end_time - start_time))

start_time = datetime.now() 
arr3=x3
for i in range(len(arr3)):
      
    min_idx = i
    for j in range(i+1, len(arr3)):
        if arr3[min_idx] > arr3[j]:
            min_idx = j
                 
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]

end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration selectionSort: {}'.format(end_time - start_time))

start_time = datetime.now() 

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0    
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

 
 
def mergeSort(arr, l, r):
    if l < r:

        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 

arr = x4
n = len(arr)
mergeSort(arr, 0, n-1)


end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration mergeSort: {}'.format(end_time - start_time))


start_time = datetime.now() 
#y=random.randint(len(x5))
y=len(x5)//2
#print (y)
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[y]     
 
    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
  
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, low, high )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
  
arr = x5
n = len(arr)
quickSort(arr, 0, n-1)
    
end_time = datetime.now()

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("% d" % arr[i],end=" ")

print('Duration quickSort: {}'.format(end_time - start_time))
