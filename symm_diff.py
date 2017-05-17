def symm_diff(list1, list2):
    """
    Input: two lists
    Output: the symmetric difference between the lists
            (elements that appear in one list but not both)
    """
    newList = []

    for i in list1:
        found = False
        for j in list2:
            if i==j:
                found = True
        if found == False:
            newList.append(i)
    for j in list2:
        found = False
        for i in list1:
            if i==j:
                found = True
        if found == False:
            newList.append(j)

    return newList

print(symm_diff([1,4], [1,2,3,4,5]))
