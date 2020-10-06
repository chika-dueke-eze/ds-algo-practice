def canMakeTriangle(arr):
    final_array = []
    for i in range(len(arr)-2):
        if (arr[i]+arr[i+1] > arr[i+2]) & (arr[i]+arr[i+2] > arr[i+1]) & (arr[i+1]+arr[i+2] > arr[i]):
            final_array.append(1)
        else:
            final_array.append(0)
    return final_array
