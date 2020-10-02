def shapeArea(n):
    fmrArea = 0          #variable that signifies former area, base value = 0
    area = 1             # base area
    for i in range(n):
        area = 4*(fmrArea) + area
        fmrArea += 1    #increase value of fmrArea by 1 after every iteration
    return area
    
