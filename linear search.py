def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return 0

arr = [1,23,43,45,34]
print(search(arr, 45))