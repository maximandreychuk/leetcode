# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.

def move_zeros(lst):
    start_idx=0
    for idx in range(len(lst)):
        if lst[idx]!=0:
            lst[start_idx]=lst[idx]
            start_idx+=1
    for i in range(start_idx,len(lst)):
        lst[i]=0
    return lst
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))