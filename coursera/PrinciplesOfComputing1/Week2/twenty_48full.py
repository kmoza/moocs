"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

#function for comparing lists
def cmp_list(dummy_list1,dummy_list2):
    """
    This function will compare two input list for any move happened post merge
    """
    is_list_equal = 0
    for value in range(len(dummy_list1)):
        if dummy_list1[value] == dummy_list2[value]:
            continue
        else:
            is_list_equal = -1
            break
    return is_list_equal

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

    return merge_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._width)]
                     for dummy_row in range(self._height)]

        #create two new tiles with value either 2 or 4 using the new tile function
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "2048_by_kmo"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == UP:
            dummy_is_move_happened = False
            for col in range(self._width):
                dummy_temp_line = []
                for row in range(self._height):
                    dummy_temp_line.append(self._grid[row][col])
                merged_list = merge(dummy_temp_line)
                if cmp_list(dummy_temp_line, merged_list) == 0:
                    continue
                else:
                    #copy the merged column in the grid again
                    for row in range(self._height):
                        self._grid[row][col] = merged_list[row]
                    if not dummy_is_move_happened:
                        dummy_is_move_happened = True

            if dummy_is_move_happened:
                self.new_tile()

        elif direction == DOWN:
            dummy_is_move_happened = False
            for col in range(self._width):
                dummy_temp_line = []
                for row in range(self._height):
                    dummy_temp_line.append(self._grid[row][col])
                dummy_temp_line.reverse()
                merged_list = merge(dummy_temp_line)
                if cmp_list(dummy_temp_line, merged_list) == 0:
                    continue
                else:
                    #copy the merged column in the grid again
                    merged_list.reverse()
                    for row in range(self._height):
                        self._grid[row][col] = merged_list[row]
                    if not dummy_is_move_happened:
                        dummy_is_move_happened = True

            if dummy_is_move_happened:
                self.new_tile()
        elif direction == RIGHT:
            dummy_list_to_be_processed = self._height
            dummy_is_move_happened = False
            for row in range(dummy_list_to_be_processed):
                dummy_temp_line = list(self._grid[row])
                dummy_temp_line.reverse()
                merged_list = merge(dummy_temp_line)
                if cmp_list(dummy_temp_line, merged_list) == 0:
                    continue
                else:
                    merged_list.reverse()
                    self._grid[row] = merged_list
                    if not dummy_is_move_happened:
                        dummy_is_move_happened = True
            if dummy_is_move_happened:
                self.new_tile()

        elif direction == LEFT:
            dummy_list_to_be_processed = self._height
            dummy_is_move_happened = False
            for row in range(dummy_list_to_be_processed):
                dummy_temp_line = list(self._grid[row])
                merged_list = merge(dummy_temp_line)
                if cmp_list(dummy_temp_line, merged_list) == 0:
                    continue
                else:
                    self._grid[row] = merged_list
                    if not dummy_is_move_happened:
                        dummy_is_move_happened = True
            if dummy_is_move_happened:
                self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        #create a new tile randomly with value 2 or 4 (probability 2 90% and 4 10%)
        dummy_random_value = random.randrange(1,10,1)
        if dummy_random_value <= 8:
            dummy_new_tile_value = 2
        else:
            dummy_new_tile_value = 4

        dummy_is_empty_tile_found = False

        while not dummy_is_empty_tile_found:
            dummy_row = random.randrange(0,self._height,1)
            dummy_col = random.randrange(0,self._width,1)
            if self._grid[dummy_row][dummy_col] == 0:
                self._grid[dummy_row][dummy_col] = dummy_new_tile_value
                dummy_is_empty_tile_found = True

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    