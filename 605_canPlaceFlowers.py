def canPlaceFlowers(flowerbed, n):
    cnt, tail = 0,1
    while tail < len(flowerbed)-1:
        if flowerbed[tail] == 0 and flowerbed[tail-1] == 0 and flowerbed[tail+1]==0:
            cnt+=1
            tail+=2
        else:
            tail += 1
    if flowerbed[0] == 0 and flowerbed[1] == 0 and flowerbed[2] == 1:
        cnt+=1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0 and flowerbed[-3] == 1:
        cnt+=1
    return cnt >= n





print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)) # t
print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)) # f
print(canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2)) # f
print(canPlaceFlowers([1,0,0,0,0,0,1], 2)) # t
print(canPlaceFlowers([1,0,1,0,1,0,1], 1)) # f