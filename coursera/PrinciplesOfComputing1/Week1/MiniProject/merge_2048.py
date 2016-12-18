"""
Merge function for 2048 game.
"""
def slide_list_to_beigning(line):
    """
    Slide function to slide the tiles to the beginning of the list
    """
    #initialize the list to be returned with all 0's
    merge_list = [0]*len(line)

    line_length = len(line)
    line_elem_index = 0
    merge_elem_index = 0

    while line_elem_index < line_length:
        lst_index = 0
        if line[line_elem_index] != 0:
            merge_list[merge_elem_index] = line[line_elem_index]
        else:
            #find the next non zero element in the list and then copy over
            lst_index = line_elem_index
            while (lst_index < line_length and line[lst_index] == 0 ):
                lst_index = lst_index + 1
            if lst_index < line_length:
                merge_list[merge_elem_index] = line[lst_index]

            if lst_index > 0:
                #find the distance of non-zero element from line element index
                lst_index = lst_index - line_elem_index

        line_elem_index = line_elem_index + lst_index + 1
        merge_elem_index = merge_elem_index + 1

    return merge_list

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    #return the same list if the line has only single element in this case there is nothing to merge
    if len(line) < 2:
        merge_list = line
        return merge_list

    #Step 1: Iterate over the input and create an output list that has all of the non-zero tiles slid over to the beginning of the list with the appropriate number of zeroes at the end of the list.
    merge_list = slide_list_to_beigning(line)

    #Step 2: Iterate over the list created in the previous step and create another new list in which pairs of tiles in the first list are replaced with a tile of twice the value and a zero tile
    added_list = [0]*len(line)

    #create a list with all 0
    line_length = len(line)

    merge_elem_index = 0
    added_list_index = 0
    while merge_elem_index < line_length :
        if (merge_elem_index + 1) < line_length and  merge_list[merge_elem_index] == merge_list[merge_elem_index+1]:
            added_list[added_list_index] = merge_list[merge_elem_index] * 2
            merge_elem_index = merge_elem_index + 2
            added_list_index = merge_elem_index
        else:
            added_list[added_list_index] = merge_list[merge_elem_index]
            merge_elem_index = merge_elem_index + 1
            added_list_index = merge_elem_index

    merge_list = slide_list_to_beigning(added_list)

    # replace with your code
    return merge_list

INPUT_LINE = [2, 0, 2, 4]
FINAL_LIST = merge(INPUT_LINE)
print FINAL_LIST

INPUT_LINE = [0, 0, 2, 2]
FINAL_LIST = merge(INPUT_LINE)
print FINAL_LIST

INPUT_LINE = [2, 2, 0, 0]
FINAL_LIST = merge(INPUT_LINE)
print FINAL_LIST

INPUT_LINE = [2, 2, 2, 2, 2]
FINAL_LIST = merge(INPUT_LINE)
print FINAL_LIST

INPUT_LINE = [8, 16, 16, 8]
FINAL_LIST = merge(INPUT_LINE)
print FINAL_LIST

INPUT_LINE = [32, 4, 4, 2]
FINAL_LIST = merge(INPUT_LINE)
print FINAL_LIST