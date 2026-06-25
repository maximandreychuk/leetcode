def stableMountains(height, threshold):
    result = []
    for i in range(1,len(height)):
        if height[i-1] > threshold:
            result.append(i)
    return result


print(stableMountains(height = [1,2,3,4,5], threshold = 2))
#done