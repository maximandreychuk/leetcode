def findRestaurant(list1, list2):
    r, a = ["ABC", len(list1)+len(list2)], []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if i+j<=r[1]:
                    r[0], r[1] = list1[i], i+j
                    a.append(list1[i])
    return a


print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"])) #Shogun
print(findRestaurant(["happy","sad","good"], list2 = ["sad","happy","good"])) # "happy","sad"
print(
    findRestaurant(
        ["Shogun","Piatti","Tapioca Express","Burger King","KFC"],
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])) # ["Piatti"]