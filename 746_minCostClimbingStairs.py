def minCostClimbingStairs(cost):
    if cost[0]<cost[1]:
        credit = cost[0]
        tail = 0
        while tail < len(cost)-2:
            if cost[tail+1] < cost[tail+2]:
                tail+=1
                credit+=cost[tail]
            else:
                tail += 2
                credit += cost[tail]
            print(credit)
    else:
        credit = cost[1]
        tail = 1
        while tail < len(cost)-2:
            if cost[tail + 1] < cost[tail + 2]:
                tail += 1
                credit += cost[tail]
            else:
                tail += 2
                credit += cost[tail]
    return credit

print(minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
print(minCostClimbingStairs(cost = [10,15,20]))