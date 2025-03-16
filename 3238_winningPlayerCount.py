from typing import List

def winningPlayerCount(n, pick: List[List[int]]):
    player_ball_count_dict = {}
    answer = 0
    for i in pick:
        if i[0] < n:
            if i[0] not in player_ball_count_dict.keys():
                player_ball_count_dict[i[0]] = {i[1]: 1}
            else:
                cnt = player_ball_count_dict[i[0]].get(i[1], 0)
                player_ball_count_dict[i[0]].update({i[1]: cnt+1})
    for player, result in player_ball_count_dict.items():
        for ball, count in result.items():
            if count > player:
                answer += 1
                break
    return answer


print(winningPlayerCount(n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]))
#done