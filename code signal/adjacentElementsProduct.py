def adjacentElementsProduct(inputArray):
    x = -1
    y = 0
    lst = []
    for i in range(len(inputArray)-1):
        x += 1
        y += 1
        adj_sum = inputArray[x] * inputArray[y]
        lst.append(adj_sum)
    lst.sort(reverse=True)
    return lst[0]
