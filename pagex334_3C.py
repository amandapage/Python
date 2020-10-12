import math
def shortestDist(alist):
    dist = 0
    distances = []
    for pair1 in range(len(alist)-1):
        x1 = alist[pair1][0]
        y1 = alist[pair1][1]
        for pair2 in range(pair1+1,len(alist)):
            x2 = alist[pair2][0]
            y2 = alist[pair2][1]
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            distances.append(dist)
    return min(distances)


            
        
        
