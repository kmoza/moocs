def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    loop_count = 25
    while loop_count > 0:
        sum_of_lastthree = 0
        list_length = len(lst)
        sum_of_lastthree = lst[list_length-1] + lst[list_length-2]+lst[list_length-3]
        lst.append(sum_of_lastthree)
        loop_count = loop_count-1

sum_three = [0,1,2]
appendsums(sum_three)
print sum_three[10]
print sum_three[20]