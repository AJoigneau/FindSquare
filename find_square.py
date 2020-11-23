import sys
import random

def generate_map(x, y, density):
    output_map = ""
    for i in range(int(y)):
        for j in range(int(x)):
            if (random.randint(0, int(y)) * 2) < int(density):
                output_map += "o"
            else:
                output_map += "."
        output_map += "\n"
    return output_map

def check_map_valid(map_str):
    if len(map_str) < 1:
        return False
    if any(char not in ".ox\n" for char in map_str):
        return False
    if map_str[-1] != "\n":
        return False
    lines = map_str.split("\n")[:-1]
    if not check_lines_length(lines):
        return False
    return True

def check_lines_length(lines):
    it = iter(lines)
    expected_len = len(next(it))
    if not all(len(l) == expected_len for l in it):
        return False
    else:
        return True

def string_to_matrix(map_str):
    return [list(row) for row in map_str.split("\n")[:-1]]

def matrix_to_string(matrix):
    return "\n".join(["".join(row) for row in matrix]) + "\n"

def draw_square(old_matrix, corner_position, size):
    new_matrix = old_matrix.copy()
    row_start = corner_position[0]
    col_start = corner_position[1]
    for row in range(row_start, row_start + size):
        for col in range(col_start, col_start + size):
            new_matrix[row][col] = "x"
    return new_matrix

def keep_top_left_square(corners_list):
    """ It evaluates the distance between the squares and the top-left corner of the map, and keep the closer one
    In case of tie, we privilege the square located on top before the one located on left """
    corners_list.sort(key=lambda x: x[0])
    corners_list.sort(key=lambda x: x[0]+x[1])
    return corners_list[0]

def search_square_from_corner(matrix, row, col):
    size = 0 # size
    nb_rows = len(matrix)
    nb_cols = len(matrix[0])
    while True:
        if row + size + 1 > nb_rows: # if we are too close from right border to find a big square
            break
        if col + size + 1 > nb_cols: # if we are too close from bottom border to find a big square
            break
        border_points_right = [matrix[row+i][col+size] for i in range(size+1)] # border right of new square
        border_points_bottom = [matrix[row+size][col+j] for j in range(size)] # border bottom of new square
        border_points = border_points_right + border_points_bottom
        is_space_empty = all(elem == "." for elem in border_points)
        # if len(obstacles) > 0:
        if not is_space_empty:
            break
        size += 1
    if any(elem == "o" for elem in border_points_right) > 0:
        return size, col+size
    else:
        return size, -1


def find_square(map_str):
    if check_map_valid(map_str) is not True:
        return ("map error\n")
    
    matrix = string_to_matrix(map_str)
    nb_rows = len(matrix)
    nb_cols = len(matrix[0])

    corners_list = [] # list of top-left corners positions for max_size squares : [(row1, col1), (row2, col2)...]
    max_size = 0 # maximum size found for squares
    row = 0
    while row < nb_rows:
        col = 0
        if row + max_size - 1 > nb_rows: # if we are too close from right border to find a big square
            break
        while col < nb_cols:
            if col + max_size - 1 > nb_cols: # if we are too close from bottom border to find a big square
                break
            local_size, index_obstacle_on_right = search_square_from_corner(matrix, row, col)
            if local_size == max_size:
                corners_list.append((row, col))
            elif local_size > max_size:
                max_size = local_size
                corners_list = [(row, col)]

            if index_obstacle_on_right > 0: # If an obstacle is found on right side, we continue research on columns after this obstacle
                col = index_obstacle_on_right
            col += 1
        row += 1
    final_square_corner = keep_top_left_square(corners_list)
        
    new_matrix = draw_square(matrix, final_square_corner, max_size)
    return matrix_to_string(new_matrix)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # if no map is passed as arg, it generates a random map 4x5 with density 3
        initial_map = generate_map(4, 5, 3)
        result_map = find_square(initial_map)
        print(result_map)
    else:
        for map_file in sys.argv[1:]:
            with open (map_file, "r") as myfile:
                initial_map = myfile.read()
        
                # print("INITIAL MAP")
                # print(initial_map)

                result_map = find_square(initial_map)
                # print("RESULT MAP")
                print(result_map)

